import { createReadStream, existsSync, mkdirSync, statSync } from "node:fs";
import { writeFile } from "node:fs/promises";
import { createServer } from "node:http";
import { extname, resolve } from "node:path";
import { spawn } from "node:child_process";

const root = resolve(new URL("..", import.meta.url).pathname);
const chrome = process.env.CHROME_PATH || "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome";
const output = resolve(root, "showcase/ops-ai-console/screens");
const mime = {
  ".css": "text/css; charset=utf-8",
  ".html": "text/html; charset=utf-8",
  ".js": "text/javascript; charset=utf-8",
  ".png": "image/png"
};

if (!existsSync(chrome)) {
  console.error(`Chrome not found: ${chrome}`);
  process.exit(2);
}

mkdirSync(output, { recursive: true });

const server = createServer((request, response) => {
  const url = new URL(request.url || "/", "http://127.0.0.1");
  const relative = decodeURIComponent(url.pathname).replace(/^\/+/, "");
  let file = resolve(root, relative || "showcase/ops-ai-console/index.html");
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

await new Promise((ready) => server.listen(0, "127.0.0.1", ready));
const port = server.address().port;
const debugPort = 9342;
const chromeProcess = spawn(chrome, [
  "--headless=new",
  "--disable-gpu",
  "--hide-scrollbars",
  "--no-first-run",
  "--no-default-browser-check",
  `--remote-debugging-port=${debugPort}`,
  `--user-data-dir=/tmp/ops-ai-console-${process.pid}`,
  "about:blank"
], { stdio: ["ignore", "ignore", "pipe"] });

let chromeError = "";
chromeProcess.stderr.on("data", (chunk) => {
  chromeError += chunk.toString();
});

async function waitForDebugger() {
  for (let attempt = 0; attempt < 60; attempt += 1) {
    try {
      const response = await fetch(`http://127.0.0.1:${debugPort}/json/version`);
      if (response.ok) return;
    } catch {
      // Chrome starts asynchronously.
    }
    await new Promise((wait) => setTimeout(wait, 100));
  }
  throw new Error(`Chrome debugger unavailable\n${chromeError}`);
}

await waitForDebugger();
const pageResponse = await fetch(
  `http://127.0.0.1:${debugPort}/json/new?${encodeURIComponent(`http://127.0.0.1:${port}/showcase/ops-ai-console/index.html`)}`,
  { method: "PUT" }
);
const page = await pageResponse.json();
const socket = new WebSocket(page.webSocketDebuggerUrl);
await new Promise((ready, reject) => {
  socket.addEventListener("open", ready, { once: true });
  socket.addEventListener("error", reject, { once: true });
});

let nextId = 1;
const pending = new Map();
socket.addEventListener("message", (event) => {
  const message = JSON.parse(event.data);
  if (!message.id || !pending.has(message.id)) return;
  const { ready, reject } = pending.get(message.id);
  pending.delete(message.id);
  if (message.error) reject(new Error(message.error.message));
  else ready(message.result);
});

function call(method, params = {}) {
  const id = nextId++;
  return new Promise((ready, reject) => {
    pending.set(id, { ready, reject });
    socket.send(JSON.stringify({ id, method, params }));
  });
}

async function evaluate(expression) {
  const result = await call("Runtime.evaluate", {
    expression,
    returnByValue: true,
    awaitPromise: true
  });
  if (result.exceptionDetails) throw new Error(result.exceptionDetails.text);
  return result.result.value;
}

async function waitFor(expression, label) {
  for (let attempt = 0; attempt < 60; attempt += 1) {
    if (await evaluate(expression)) return;
    await new Promise((wait) => setTimeout(wait, 100));
  }
  throw new Error(`Timed out waiting for ${label}`);
}

async function navigate(path) {
  await call("Page.navigate", { url: `http://127.0.0.1:${port}${path}` });
  await waitFor("document.readyState === 'complete' && document.querySelector('main')", path);
}

async function screenshot(name) {
  await evaluate("document.activeElement instanceof HTMLElement && document.activeElement.blur()");
  const result = await call("Page.captureScreenshot", { format: "png", captureBeyondViewport: false });
  await writeFile(resolve(output, `${name}.png`), Buffer.from(result.data, "base64"));
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

  await navigate("/showcase/ops-ai-console/daily.html");
  check("daily desktop overflow", await evaluate("document.documentElement.scrollWidth <= innerWidth"));
  await evaluate("document.querySelector('#tab-logs-button').click()");
  check("daily evidence tabs", await evaluate("document.querySelector('#tab-logs').hidden === false && document.querySelector('#tab-metrics').hidden === true"));
  await evaluate("document.querySelector('[data-open-dialog=\"approvalDialog\"]').click()");
  check("daily approval dialog", await evaluate("document.querySelector('#approvalDialog').open"));
  await evaluate("document.querySelector('#approvalDialog [data-close-dialog]').click()");
  await evaluate("document.querySelector('#tab-metrics-button').click()");
  await screenshot("daily");

  await navigate("/showcase/ops-ai-console/incident.html");
  check("incident desktop overflow", await evaluate("document.documentElement.scrollWidth <= innerWidth"));
  check("incident timeline", await evaluate("document.querySelectorAll('.timeline-event').length === 5"));
  await screenshot("incident");

  await navigate("/showcase/ops-ai-console/agent-replay.html");
  check("agent desktop overflow", await evaluate("document.documentElement.scrollWidth <= innerWidth"));
  await evaluate("const range=document.querySelector('#traceRange'); range.value='5'; range.dispatchEvent(new Event('input',{bubbles:true}));");
  check("agent replay step", await evaluate("document.querySelectorAll('.trace-step:not(.is-hidden)').length === 5"));
  await screenshot("agent-replay");

  await call("Emulation.setDeviceMetricsOverride", {
    width: 390,
    height: 844,
    deviceScaleFactor: 1,
    mobile: true
  });
  await navigate("/showcase/ops-ai-console/daily.html");
  check("mobile daily overflow", await evaluate("document.documentElement.scrollWidth <= innerWidth"));
  await evaluate("document.querySelector('[data-nav-toggle]').click()");
  check("mobile nav", await evaluate("getComputedStyle(document.querySelector('#globalNav')).display !== 'none'"));

  await navigate("/showcase/ops-ai-console/index.html");
  check("gallery mobile overflow", await evaluate("document.documentElement.scrollWidth <= innerWidth"));
  await call("Emulation.setDeviceMetricsOverride", {
    width: 1440,
    height: 900,
    deviceScaleFactor: 1,
    mobile: false
  });
  await navigate("/showcase/ops-ai-console/index.html");
  check("gallery desktop overflow", await evaluate("document.documentElement.scrollWidth <= innerWidth"));
  await screenshot("index");
} finally {
  socket.close();
  chromeProcess.kill("SIGTERM");
  server.close();
}

if (failures.length) {
  console.error(`\n${failures.length} showcase checks failed`);
  process.exit(1);
}
console.log("\nOps showcase captured");

