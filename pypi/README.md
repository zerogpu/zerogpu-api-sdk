# zerogpu-api (Python SDK)

Official Python SDK for the ZeroGPU Responses API. Build production integrations with typed models, clear errors, and simple authentication.

## Install

```bash
pip install zerogpu-api
```

## Quick Start

```python
from zerogpu import ZerogpuApi

client = ZerogpuApi(
    api_key="…",
    project_id="…",
)
client.responses.create_response(
    model="zlm-v1-followup-questions-edge",
    input="In one short sentence, what is a habit tracker?",
    text={"format": {"type": "text"}},
)
```

Response text is returned in the standard Responses API payload shape (`output` blocks).

## API Reference

- [ZeroGPU docs](https://docs.zerogpu.ai)
- [Responses endpoint](https://docs.zerogpu.ai/api-reference/endpoint/responses)
