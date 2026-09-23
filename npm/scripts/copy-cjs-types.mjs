// tsup bundles the JS; tsc emits the declarations (bundled .d.ts files lose names that are both
// an interface and a namespace, e.g. ZerogpuApi.ChatMessage). The package is "type": "module", so
// CommonJS consumers get a copy of the declarations marked as CommonJS.
import { cpSync, writeFileSync } from "node:fs";

cpSync("dist/types", "dist/types-cjs", { recursive: true });
writeFileSync("dist/types-cjs/package.json", JSON.stringify({ type: "commonjs" }) + "\n");
