import { copyFileSync, mkdirSync } from "node:fs";
import { join } from "node:path";

const root = process.cwd();
const output = join(root, "dist");

mkdirSync(output, { recursive: true });
copyFileSync(join(root, "site", "index.html"), join(output, "index.html"));
