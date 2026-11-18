import { createReadStream, existsSync, readFileSync, statSync } from "node:fs";
import { createServer } from "node:http";
import { extname, resolve } from "node:path";
import { spawn } from "node:child_process";

const root = resolve(new URL("..", import.meta.url).pathname);
const index = JSON.parse(readFileSync(resolve(root, "styles/index.json"), "utf8"));
const expectedStyles = index.styles.length;
const expectedCore = index.styles.filter((s) => s.tier === "core").length;
const chrome = process.env.CHROME_PATH || "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome";
const mime = {
  ".css": "text/css; charset=utf-8",
  ".html": "text/html; charset=utf-8",
  ".js": "text/javascript; charset=utf-8",
  ".json": "application/json; charset=utf-8",
  ".png": "image/png",
  ".md": "text/markdown; charset=utf-8"
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
const events = [];

socket.addEventListener("message", (event) => {
  const message = JSON.parse(event.data);
  if (message.id && pending.has(message.id)) {
    const { resolveCall, rejectCall } = pending.get(message.id);
    pending.delete(message.id);
    if (message.error) rejectCall(new Error(message.error.message));
    else resolveCall(message.result);
  } else if (message.method) {
    events.push(message);
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

async function waitFor(expression, label) {
  for (let attempt = 0; attempt < 60; attempt += 1) {
    if (await evaluate(expression)) return;
    await new Promise((resolveWait) => setTimeout(resolveWait, 100));
  }
  throw new Error(`Timed out waiting for ${label}`);
}

async function screenshot(path) {
  const result = await call("Page.captureScreenshot", { format: "png", captureBeyondViewport: false });
  const { writeFile } = await import("node:fs/promises");
  await writeFile(path, Buffer.from(result.data, "base64"));
}

const failures = [];
function check(name, condition, detail = "") {
  if (condition) {
    console.log(`ok ${name}`);
  } else {
    failures.push(`${name}${detail ? `: ${detail}` : ""}`);
    console.error(`FAIL ${name}${detail ? `: ${detail}` : ""}`);
  }
}

try {
  await call("Page.enable");
  await call("Runtime.enable");
  await call("Emulation.setDeviceMetricsOverride", {
    width: 1440,
    height: 900,
    deviceScaleFactor: 1,
    mobile: false
  });
  await call("Page.navigate", { url: `http://127.0.0.1:${port}/catalog/index.html` });
  await waitFor(`document.readyState === 'complete' && document.querySelectorAll('.style-row').length === ${expectedStyles}`, "catalog");

  check("desktop rows", await evaluate("document.querySelectorAll('.style-row').length") === expectedStyles);
  check("desktop preview", await evaluate("document.querySelector('#previewFrame').src.includes('/preview/')"));
  check("desktop no overflow", await evaluate("document.documentElement.scrollWidth <= innerWidth"));
  await evaluate("document.querySelector('input[name=\"tier\"][value=\"core\"]').click()");
  check("core filter", await evaluate("document.querySelectorAll('.style-row').length") === expectedCore);
  await evaluate("document.querySelector('input[name=\"tier\"][value=\"all\"]').click()");
  await screenshot("/tmp/design-library-desktop.png");

  for (const slug of ["developer-docs", "enterprise-data", "adaptive-companion"]) {
    await call("Page.navigate", { url: `http://127.0.0.1:${port}/preview/${slug}.html` });
    await waitFor("document.readyState === 'complete' && document.querySelector('h1')", slug);
    check(`${slug} no overflow`, await evaluate("document.documentElement.scrollWidth <= innerWidth"));
    await screenshot(`/tmp/${slug}.png`);
  }

  await call("Emulation.setDeviceMetricsOverride", {
    width: 1440,
    height: 900,
    deviceScaleFactor: 1,
    mobile: false
  });
  await call("Page.navigate", {
    url: `http://127.0.0.1:${port}/catalog/index.html?q=${encodeURIComponent("正在发生重大事故，需要时间线和交接")}`
  });
  await waitFor("document.readyState === 'complete' && document.querySelector('.style-row')", "recommendation");
  check(
    "incident recommendation",
    await evaluate("document.querySelector('.style-row .style-name').textContent.trim()") === "Incident Room"
  );

  await evaluate("document.querySelectorAll('[data-compare]')[0].click(); document.querySelectorAll('[data-compare]')[1].click(); document.querySelector('#openCompare').click();");
  await waitFor("document.querySelector('#compareDialog').open", "comparison dialog");
  check("comparison count", await evaluate("document.querySelectorAll('.compare-column').length") === 2);
  await screenshot("/tmp/design-library-compare.png");

  await call("Emulation.setDeviceMetricsOverride", {
    width: 390,
    height: 844,
    deviceScaleFactor: 1,
    mobile: true
  });
  await new Promise((resolveWait) => setTimeout(resolveWait, 200));
  check("mobile filters folded", await evaluate("getComputedStyle(document.querySelector('.filter-panel')).display === 'none'"));
  check("mobile inspector folded", await evaluate("getComputedStyle(document.querySelector('.inspector')).display === 'none'"));
  check("mobile detail visible", await evaluate("getComputedStyle(document.querySelector('.mobile-detail')).display !== 'none'"));
  check("mobile no overflow", await evaluate("document.documentElement.scrollWidth <= innerWidth"));
  await evaluate("document.querySelector('#compareDialog').close()");
  await evaluate("document.querySelector('#filterToggle').click()");
  check("mobile filters open", await evaluate("getComputedStyle(document.querySelector('.filter-panel')).display !== 'none'"));
  await screenshot("/tmp/design-library-mobile.png");
} finally {
  socket.close();
  processHandle.kill("SIGTERM");
  server.close();
}

if (failures.length) {
  console.error(`\n${failures.length} browser checks failed`);
  process.exit(1);
}
console.log("\nBrowser smoke passed");

