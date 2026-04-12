# zerogpu-api (Python)

Install from PyPI (after you publish):

```bash
pip install zerogpu-api
```

```python
from zerogpu import ZerogpuApi, InputMessage

client = ZerogpuApi(
    api_key="…",
    project_id="…",
)
client.responses.create_response(
    model="your-model-id",
    input=[InputMessage(role="user", content="Hello")],
)
```

See [docs.zerogpu.ai](https://docs.zerogpu.ai) for authentication and models.
