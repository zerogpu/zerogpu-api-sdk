/**
 * Smoke test: one real call through the Fern-generated TypeScript SDK.
 *
 * Credentials (same as Benchmark):
 *   ZEROGPU_API_KEY
 *   ZEROGPU_PROJECT_ID
 *   ZEROGPU_MODEL   (required — use the model id from your dashboard, same as `npm run benchmark -- --model <id>`)
 *
 * Optional:
 *   ZEROGPU_MESSAGE_INPUT=1 — send `input` as chat messages. Default is a plain string `input` (common for production models).
 *   ZEROGPU_INPUT_TEXT — override the default prompt / user text
 *
 * Loads .env from this folder, then ../../../Benchmark/.env if present.
 *
 * Note: keep `"type": "module"` out of package.json here — with it set, `tsx smoke.ts` can fail to resolve the SDK’s exports on some setups.
 */
import { config } from "dotenv";
import { dirname, resolve } from "path";
import { fileURLToPath } from "url";

import { ZerogpuApiClient } from "../../sdks/typescript/index.ts";
import type { CreateResponseRequest } from "../../sdks/typescript/api/resources/responses/client/requests/CreateResponseRequest.ts";
import type { Response } from "../../sdks/typescript/api/types/Response.ts";

const __dirname = dirname(fileURLToPath(import.meta.url));

for (const p of [
  resolve(__dirname, ".env"),
  resolve(__dirname, "../../../Benchmark/.env"),
]) {
  config({ path: p });
}

function firstAssistantText(res: Response): string {
  for (const msg of res.output ?? []) {
    for (const block of msg.content ?? []) {
      if (block.type === "output_text" && block.text) return String(block.text).trim();
      if (typeof block.text === "string") return block.text.trim();
    }
  }
  return "";
}

async function main() {
  const apiKey = process.env.ZEROGPU_API_KEY?.trim();
  const projectId = process.env.ZEROGPU_PROJECT_ID?.trim();
  const model = process.env.ZEROGPU_MODEL?.trim();

  if (!apiKey || !projectId) {
    console.error(
      "Set ZEROGPU_API_KEY and ZEROGPU_PROJECT_ID (e.g. use Benchmark/.env or export in shell)."
    );
    process.exit(1);
  }

  if (!model) {
    console.error(
      "Set ZEROGPU_MODEL to a model id from the ZeroGPU dashboard (example: zlm-v1-followup-questions-edge)."
    );
    process.exit(1);
  }

  const client = new ZerogpuApiClient({
    apiKey,
    projectId,
  });

  const useMessageInput = process.env.ZEROGPU_MESSAGE_INPUT === "1";

  const body: CreateResponseRequest = useMessageInput
    ? {
        model,
        input: [
          {
            role: "user",
            content:
              process.env.ZEROGPU_INPUT_TEXT?.trim() ||
              "In one short sentence, what is a habit tracker?",
          },
        ],
        text: { format: { type: "text" } },
      }
    : {
        model,
        input:
          process.env.ZEROGPU_INPUT_TEXT?.trim() ||
          "In one short sentence, what is a habit tracker?",
        text: { format: { type: "text" } },
      };

  const res = await client.responses.createResponse(body);

  console.log("id:", res.id);
  console.log("model:", res.model);
  console.log("usage:", res.usage);
  console.log("text:", firstAssistantText(res) || "(no output_text block)");
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
