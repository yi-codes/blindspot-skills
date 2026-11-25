import { createReadStream, existsSync, statSync } from "node:fs";
import { createServer } from "node:http";
import { extname, resolve } from "node:path";
import { spawn } from "node:child_process";
import { mkdir, writeFile } from "node:fs/promises";

const root = resolve(new URL("..", import.meta.url).pathname);
const outDir = process.argv[2] || "/tmp/design-library-samples";
await mkdir(outDir, { recursive: true });

const chrome = process.env.CHROME_PATH || "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome";
const mime = {
  ".css": "text/css; charset=utf-8",
  ".html": "text/html; charset=utf-8",
  ".js": "text/javascript; charset=utf-8",
  ".json": "application/json; charset=utf-8",
  ".png": "image/png",
  ".woff2": "font/woff2",
  ".woff": "font/woff"
};

if (!existsSync(chrome)) {
  console.error(`Chrome not found: ${chrome}`);
  process.exit(2);
}

const server = createServer((request, response) => {
  const url = new URL(request.url || "/", "http://127.0.0.1");
  const relative = decodeURIComponent(url.pathname).replace(/^\/+/, "");
  let file = resolve(root, relative || "catalog/index.html");
  if (!file.startsWith(root)) {
    response.writeHead(403).end("Forbidden");
    return;
  }
  if (existsSync(file) && statSync(file).isDirectory()) {
    file = resolve(file, "index.html");
  }
  if (!existsSync(file) || !statSync(file).isFile()) {
    response.writeHead(404).end("Not found");
    return;
  }
  response.writeHead(200, { "content-type": mime[extname(file)] || "application/octet-stream" });
  createReadStream(file).pipe(response);
});

await new Promise((resolveReady) => server.listen(0, "127.0.0.1", resolveReady));
const port = server.address().port;
const debugPort = 9341;
const profile = `/tmp/design-library-chrome-${process.pid}`;
const processHandle = spawn(chrome, [
  "--headless=new",
  "--disable-gpu",
  "--disable-dev-shm-usage",
  "--disable-extensions",
  "--disable-background-networking",
  "--single-process",
  "--no-sandbox",
  "--hide-scrollbars",
  "--no-first-run",
  "--no-default-browser-check",
  `--remote-debugging-port=${debugPort}`,
  `--user-data-dir=${profile}`,
  "about:blank"
], { stdio: ["ignore", "ignore", "pipe"] });

let browserError = "";
processHandle.stderr.on("data", (chunk) => {
  browserError += chunk.toString();
});

async function waitForDebugger() {
  for (let attempt = 0; attempt < 60; attempt += 1) {
    try {
      const response = await fetch(`http://127.0.0.1:${debugPort}/json/version`);
      if (response.ok) return;
    } catch {
      // Chrome starts asynchronously.
    }
    await new Promise((resolveWait) => setTimeout(resolveWait, 100));
  }
  throw new Error(`Chrome debugger unavailable\n${browserError}`);
}

await waitForDebugger();
const pageResponse = await fetch(
  `http://127.0.0.1:${debugPort}/json/new?${encodeURIComponent(`http://127.0.0.1:${port}/catalog/index.html`)}`,
  { method: "PUT" }
);
const page = await pageResponse.json();
const socket = new WebSocket(page.webSocketDebuggerUrl);
await new Promise((resolveOpen, rejectOpen) => {
  socket.addEventListener("open", resolveOpen, { once: true });
  socket.addEventListener("error", rejectOpen, { once: true });
});

let nextId = 1;
const pending = new Map();
socket.addEventListener("message", (event) => {
  const message = JSON.parse(event.data);
  if (message.id && pending.has(message.id)) {
    const { resolveCall, rejectCall } = pending.get(message.id);
    pending.delete(message.id);
    if (message.error) rejectCall(new Error(message.error.message));
    else resolveCall(message.result);
  }
});

function call(method, params = {}) {
  const id = nextId;
  nextId += 1;
  return new Promise((resolveCall, rejectCall) => {
    pending.set(id, { resolveCall, rejectCall });
    socket.send(JSON.stringify({ id, method, params }));
  });
}

async function evaluate(expression) {
  const response = await call("Runtime.evaluate", {
    expression,
    returnByValue: true,
    awaitPromise: true
  });
  if (response.exceptionDetails) {
    throw new Error(response.exceptionDetails.text);
  }
  return response.result.value;
}

async function screenshot(path) {
  const result = await call("Page.captureScreenshot", { format: "png", captureBeyondViewport: false });
  await writeFile(path, Buffer.from(result.data, "base64"));
}

const samples = [
  ["catalog", "catalog/index.html"],
  ["bauhaus", "preview/bauhaus.html"],
  ["bento-grid", "preview/bento-grid.html"],
  ["vaporwave", "preview/vaporwave.html"],
  ["frutiger-aero", "preview/frutiger-aero.html"],
  ["memphis", "preview/memphis.html"],
  ["constructivism", "preview/constructivism.html"],
  ["blueprint", "preview/blueprint.html"],
  ["gallery-wall", "preview/gallery-wall.html"],
  ["newsprint-grid", "preview/newsprint-grid.html"],
  ["riso-zine", "preview/riso-zine.html"],
  ["sketch-notes", "preview/sketch-notes.html"],
  ["pixel-arcade", "preview/pixel-arcade.html"],
  ["deco-ceremony", "preview/deco-ceremony.html"]
];

try {
  await call("Page.enable");
  await call("Runtime.enable");
  await call("Emulation.setDeviceMetricsOverride", {
    width: 1280,
    height: 1400,
    deviceScaleFactor: 1,
    mobile: false
  });
  for (const [name, rel] of samples) {
    await call("Page.navigate", { url: `http://127.0.0.1:${port}/${rel}` });
    for (let attempt = 0; attempt < 80; attempt += 1) {
      if (await evaluate("document.readyState") === "complete") break;
      await new Promise((resolveWait) => setTimeout(resolveWait, 100));
    }
    await new Promise((resolveWait) => setTimeout(resolveWait, 300));
    const path = resolve(outDir, `${name}.png`);
    await screenshot(path);
    console.log(`shotted ${name} -> ${path}`);
  }
} finally {
  socket.close();
  processHandle.kill("SIGTERM");
  server.close();
}
console.log(`\nDone: ${samples.length} samples`);
