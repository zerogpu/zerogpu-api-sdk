# zerogpu-sdk (Python SDK)

Official Python client for the ZeroGPU API: responses, chat completions, moderations, embeddings, and audio (transcriptions and speech), authenticated with your API key (`x-api-key` header). Published from [**ZeroGPU API SDKs**](https://github.com/zerogpu/SDK) (`pypi/` in that repository).

## Install

```bash
pip install zerogpu-sdk
```

## Quick start — Responses

`input` may be a **string** or a **list** of message dicts / `InputMessage`, depending on the model.

```python
import os
from zerogpu import ZerogpuApi

client = ZerogpuApi(
    api_key=os.environ["ZEROGPU_API_KEY"],
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

## Moderations

Classify text against OpenAI's 13 safety categories. `model` defaults to `zlm-v1-moderation-edge`.

```python
moderation = client.moderations.create_moderation(input="I want to hurt them.")
print(moderation.results[0].flagged, moderation.results[0].categories)
```

## Embeddings

384-dimensional vectors from `all-minilm-l6-v2` or `bge-small-en-v1.5`. Pass a list to embed a batch.

```python
embeddings = client.embeddings.create_embedding(
    model="all-minilm-l6-v2",
    input=["first document", "second document"],
)
print(embeddings.data[0].embedding)
```

## Audio

Transcribe with `whisper-tiny`. `json` (default) and `verbose_json` return a `TranscriptionResponse`; `text`, `srt`, and `vtt` return a string.

```python
with open("speech.mp3", "rb") as f:
    transcript = client.audio.create_transcription(file=f)
print(transcript.text)
```

Generate speech with `chatterbox-nano`; the result is the audio bytes. Pass `voice_sample` to clone a voice from a reference clip.

```python
audio = client.audio.create_speech(input="Hey, how are you today?", response_format="mp3")
with open("speech.mp3", "wb") as f:
    f.write(audio)
```

Every client has an async twin: `AsyncZerogpuApi` exposes the same methods with `await`.

## API reference

- [ZeroGPU docs](https://docs.zerogpu.ai)
- [Responses](https://docs.zerogpu.ai/api-reference/endpoint/responses)
- [Chat completions](https://docs.zerogpu.ai/api-reference/endpoint/chat-completions)
- [Moderations](https://docs.zerogpu.ai/api-reference/moderations)
- [Embeddings](https://docs.zerogpu.ai/api-reference/embeddings)
- [Transcriptions](https://docs.zerogpu.ai/api-reference/audio-transcriptions)
- [Speech](https://docs.zerogpu.ai/api-reference/audio-speech)

## Repository

Source and release workflow: [github.com/zerogpu/SDK](https://github.com/zerogpu/SDK) (Python package lives under `pypi/`).
