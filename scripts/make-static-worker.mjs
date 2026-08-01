import { mkdirSync, readFileSync, writeFileSync } from "node:fs";
import { join } from "node:path";

const root = process.cwd();
const page = readFileSync(join(root, "site", "index.html"), "utf8");
const worker = `const page = ${JSON.stringify(page)};

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    if ((request.method === "GET" || request.method === "HEAD") &&
        (url.pathname === "/" || url.pathname === "/index.html")) {
      return new Response(request.method === "HEAD" ? null : page, {
        headers: {
          "content-type": "text/html; charset=utf-8",
          "cache-control": "private, max-age=0, must-revalidate",
          "x-content-type-options": "nosniff",
          "x-frame-options": "SAMEORIGIN"
        }
      });
    }
    return env.ASSETS.fetch(request);
  }
};
`;

mkdirSync(join(root, ".open-next"), { recursive: true });
writeFileSync(join(root, ".open-next", "worker.js"), worker);
