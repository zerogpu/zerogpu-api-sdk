# Reference
## Responses
<details><summary><code>client.responses.<a href="/lib/zerogpu/responses/client.rb">create_response</a>(request) -> Zerogpu::Types::Response</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```ruby
client.responses.create_response(
  model: "model",
  input: [{
    role: "user",
    content: "content"
  }]
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

**model:** `String` — Model identifier from the ZeroGPU dashboard (e.g. summarization or IAB classify).
    
</dd>
</dl>

<dl>
<dd>

**input:** `Internal::Types::Array[Zerogpu::Types::InputMessage]` 
    
</dd>
</dl>

<dl>
<dd>

**text:** `Zerogpu::Types::TextResponseConfig` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `Zerogpu::Responses::RequestOptions` 
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

