import { defineConfig } from "tsup";

export default defineConfig({
  entry: ["../sdks/typescript/index.ts"],
  format: ["cjs", "esm"],
  dts: {
    compilerOptions: {
      types: ["node"],
    },
  },
  sourcemap: true,
  clean: true,
  treeshake: true,
  splitting: false,
  outDir: "dist",
});
