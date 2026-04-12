# Reference
## Responses
<details><summary><code>client.Responses.CreateResponse(request) -> *sdk.Response</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```go
request := &sdk.CreateResponseRequest{
        Model: "model",
        Input: []*sdk.InputMessage{
            &sdk.InputMessage{
                Role: sdk.InputMessageRoleUser,
                Content: "content",
            },
        },
    }
client.Responses.CreateResponse(
        context.TODO(),
        request,
    )
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

**model:** `string` — Model identifier from the ZeroGPU dashboard (e.g. summarization or IAB classify).
    
</dd>
</dl>

<dl>
<dd>

**input:** `[]*sdk.InputMessage` 
    
</dd>
</dl>

<dl>
<dd>

**text:** `*sdk.TextResponseConfig` 
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

