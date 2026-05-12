# Reference
## Responses
<details><summary><code>client.responses.<a href="src/zerogpu/responses/client.py">create_response</a>(...) -> Response</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zerogpu import ZerogpuApi
from zerogpu.environment import ZerogpuApiEnvironment

client = ZerogpuApi(
    api_key="<value>",
    project_id="<x-project-id>",
    environment=ZerogpuApiEnvironment.PRODUCTION,
)

client.responses.create_response(
    model="model",
    input="input",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**model:** `str` — Model identifier from the ZeroGPU dashboard (e.g. summarization or IAB classify).
    
</dd>
</dl>

<dl>
<dd>

**input:** `CreateResponseRequestInput` 

Model-dependent input. Many production models accept a **plain string**.
Others accept a **chat-style message list** (`role` + `content`). Use the shape
required by your model; see [docs](https://docs.zerogpu.ai/api-reference/endpoint/responses).
    
</dd>
</dl>

<dl>
<dd>

**text:** `typing.Optional[TextResponseConfig]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

