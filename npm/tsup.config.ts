import { defineConfig } from "tsup";

export default defineConfig({
  entry: ["../sdks/typescript/index.ts"],
  format: ["cjs", "esm"],
  // Declarations come from tsc (see tsconfig.build.json).
  dts: false,
  sourcemap: false,
  minify: true,
  clean: true,
  treeshake: true,
  splitting: false,
  outDir: "dist",
});
