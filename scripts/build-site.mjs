import { copyFileSync, mkdirSync, readFileSync, writeFileSync } from "node:fs";
import { join } from "node:path";

const root = process.cwd();
const output = join(root, "dist");
const page = readFileSync(join(root, "site", "index.html"), "utf8");
const worker = `const page = ${JSON.stringify(page)};

export default {
  async fetch(request) {
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
    return new Response("Not found", { status: 404 });
  }
};
`;

mkdirSync(join(output, "server"), { recursive: true });
mkdirSync(join(output, ".openai"), { recursive: true });
copyFileSync(join(root, "site", "index.html"), join(output, "index.html"));
copyFileSync(
  join(root, ".openai", "hosting.json"),
  join(output, ".openai", "hosting.json"),
);
writeFileSync(join(output, "server", "index.js"), worker);
