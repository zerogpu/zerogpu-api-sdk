# Reference
## Responses
<details><summary><code>client.responses.<a href="/src/api/resources/responses/client.rs">create_response</a>(request: CreateResponseRequest) -> Result&lt;Response, ApiError&gt;</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```rust
use zerogpu_api::prelude::*;

#[tokio::main]
async fn main() {
    let config = ClientConfig {
        api_key: Some("<value>".to_string()),
        ..Default::default()
    };
    let client = ApiClient::new(config).expect("Failed to build client");
    client
        .responses
        .create_response(
            &CreateResponseRequest {
                model: "model".to_string(),
                input: vec![InputMessage {
                    role: InputMessageRole::User,
                    content: "content".to_string(),
                }],
                text: None,
            },
            None,
        )
        .await;
}
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

**input:** `Vec<InputMessage>` 
    
</dd>
</dl>

<dl>
<dd>

**text:** `Option<TextResponseConfig>` 
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

