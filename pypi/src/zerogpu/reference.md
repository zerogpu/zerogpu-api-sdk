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

**instructions:** `typing.Optional[str]` — Optional system-style instructions applied on top of `input`, for models that support them.
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, typing.Any]]` — Optional model-specific parameters (e.g. PII `mask`, `usecase`). Omit when not required.
    
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

## Chat
<details><summary><code>client.chat.<a href="src/zerogpu/chat/client.py">create_chat_completion</a>(...) -> ChatCompletionResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zerogpu import ZerogpuApi, ChatMessage
from zerogpu.environment import ZerogpuApiEnvironment

client = ZerogpuApi(
    api_key="<value>",
    environment=ZerogpuApiEnvironment.PRODUCTION,
)

client.chat.create_chat_completion(
    model="model",
    messages=[
        ChatMessage(
            role="system",
            content="content",
        )
    ],
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

**model:** `str` — Model identifier from the ZeroGPU dashboard.
    
</dd>
</dl>

<dl>
<dd>

**messages:** `typing.List[ChatMessage]` 
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, typing.Any]]` — Optional model-specific parameters (e.g. PII options).
    
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

## Moderations
<details><summary><code>client.moderations.<a href="src/zerogpu/moderations/client.py">create_moderation</a>(...) -> ModerationResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zerogpu import ZerogpuApi

client = ZerogpuApi(
    api_key="<value>",
)

client.moderations.create_moderation(
    input="I want to hurt them.",
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

**input:** `CreateModerationRequestInput` — A string, a list of strings (one result per element), or a list of `{"type": "text", "text": ...}` parts.
    
</dd>
</dl>

<dl>
<dd>

**model:** `typing.Optional[str]` — Defaults to `zlm-v1-moderation-edge`; OpenAI moderation ids are accepted and mapped.
    
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

## Embeddings
<details><summary><code>client.embeddings.<a href="src/zerogpu/embeddings/client.py">create_embedding</a>(...) -> EmbeddingResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zerogpu import ZerogpuApi

client = ZerogpuApi(
    api_key="<value>",
)

client.embeddings.create_embedding(
    model="all-minilm-l6-v2",
    input="ZeroGPU runs inference at the edge.",
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

**model:** `str` — `all-minilm-l6-v2` or `bge-small-en-v1.5`.
    
</dd>
</dl>

<dl>
<dd>

**input:** `CreateEmbeddingRequestInput` — A string, or a list of strings (one vector per element).
    
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

## Audio
<details><summary><code>client.audio.<a href="src/zerogpu/audio/client.py">create_transcription</a>(...) -> CreateTranscriptionResult</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zerogpu import ZerogpuApi

client = ZerogpuApi(
    api_key="<value>",
)

with open("speech.mp3", "rb") as f:
    client.audio.create_transcription(
        file=f,
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

**file:** `core.File` — The audio file: bytes, an open binary file, or a `(filename, content)` tuple. Up to 25 MB and 10 minutes.
    
</dd>
</dl>

<dl>
<dd>

**model:** `typing.Optional[str]` — Defaults to `whisper-tiny`.
    
</dd>
</dl>

<dl>
<dd>

**language:** `typing.Optional[str]` — ISO-639-1 code, such as `en`. Detected automatically when omitted.
    
</dd>
</dl>

<dl>
<dd>

**prompt:** `typing.Optional[str]` — Text to guide spelling and style, such as names or jargon.
    
</dd>
</dl>

<dl>
<dd>

**response_format:** `typing.Optional[TranscriptionResponseFormat]` — `json` (default) and `verbose_json` return a `TranscriptionResponse`; `text`, `srt`, and `vtt` return a string.
    
</dd>
</dl>

<dl>
<dd>

**temperature:** `typing.Optional[float]` — Sampling temperature, 0 to 1.
    
</dd>
</dl>

<dl>
<dd>

**timestamp_granularities:** `typing.Optional[typing.Sequence[str]]` — `segment` (default), `word`, or both. Requires `verbose_json`.
    
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

<details><summary><code>client.audio.<a href="src/zerogpu/audio/client.py">create_speech</a>(...) -> bytes</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zerogpu import ZerogpuApi

client = ZerogpuApi(
    api_key="<value>",
)

audio = client.audio.create_speech(
    input="Hey, how are you today?",
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

**input:** `str` — The text to speak, up to 2000 characters.
    
</dd>
</dl>

<dl>
<dd>

**model:** `typing.Optional[str]` — Defaults to `chatterbox-nano`.
    
</dd>
</dl>

<dl>
<dd>

**voice:** `typing.Optional[str]` — OpenAI voice names are accepted and all map to the built-in voice.
    
</dd>
</dl>

<dl>
<dd>

**response_format:** `typing.Optional[SpeechResponseFormat]` — `mp3` (default), `opus`, `aac`, `flac`, `wav`, or `pcm`.
    
</dd>
</dl>

<dl>
<dd>

**seed:** `typing.Optional[int]` — Pins sampling for repeatable output (best-effort).
    
</dd>
</dl>

<dl>
<dd>

**temperature:** `typing.Optional[float]` — Sampling temperature, 0 to 2.
    
</dd>
</dl>

<dl>
<dd>

**top_p:** `typing.Optional[float]` — Nucleus sampling, 0 to 1.
    
</dd>
</dl>

<dl>
<dd>

**top_k:** `typing.Optional[int]` — Top-k sampling.
    
</dd>
</dl>

<dl>
<dd>

**repetition_penalty:** `typing.Optional[float]` — Penalty on repeated speech tokens, 1 to 4.
    
</dd>
</dl>

<dl>
<dd>

**voice_sample:** `typing.Optional[core.File]` — Reference clip to clone a voice from (up to 10 MB and 30 seconds). Overrides `voice`.
    
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
