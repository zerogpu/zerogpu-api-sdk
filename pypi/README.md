# zerogpu-api (Python)

Official ZeroGPU API client for Python.

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

## API Reference

- [ZeroGPU docs](https://docs.zerogpu.ai)
- [Responses endpoint](https://docs.zerogpu.ai/api-reference/endpoint/responses)
