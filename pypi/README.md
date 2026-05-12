# zerogpu-api (Python SDK)

Official Python SDK for the ZeroGPU API: **`POST /v1/responses`** and **`POST /v1/chat/completions`**, with `x-api-key` and `x-project-id` on every request.

## Install

```bash
pip install zerogpu-api
```

## Quick start — Responses

`input` may be a **string** or a **list** of message dicts / `InputMessage`, depending on the model.

```python
import os
from zerogpu import ZerogpuApi

client = ZerogpuApi(
    api_key=os.environ["ZEROGPU_API_KEY"],
    project_id=os.environ["ZEROGPU_PROJECT_ID"],
)

response = client.responses.create_response(
    model="zlm-v1-followup-questions-edge",
    input="In one short sentence, what is a habit tracker?",
    text={"format": {"type": "text"}},
)
print(response)
```

### Optional `metadata` (Responses)

```python
client.responses.create_response(
    model="gliner-multi-pii-v1",
    input="Your text…",
    metadata={"mask": "label", "usecase": "redact"},
)
```

## Chat completions

```python
from zerogpu import ChatMessage

client.chat.create_chat_completion(
    model="gliner-multi-pii-v1",
    messages=[ChatMessage(role="user", content="Your text…")],
    metadata={"mask": "label", "usecase": "redact"},
)
```

## API reference

- [ZeroGPU docs](https://docs.zerogpu.ai)
- [Responses](https://docs.zerogpu.ai/api-reference/endpoint/responses)
- [Chat completions](https://docs.zerogpu.ai/api-reference/endpoint/chat-completions)

## Repository

Source and release workflow: [github.com/zerogpu/SDK](https://github.com/zerogpu/SDK) (Python package lives under `pypi/`).
