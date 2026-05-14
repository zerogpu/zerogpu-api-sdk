//! Live smoke: one POST /v1/responses via Fern-generated Rust SDK.

use std::path::PathBuf;

use zerogpu_api::client::ApiClientBuilder;
use zerogpu_api::prelude::*;

fn load_dotenv(path: PathBuf) {
    if let Ok(s) = std::fs::read_to_string(&path) {
        for line in s.lines() {
            let line = line.trim();
            if line.is_empty() || line.starts_with('#') {
                continue;
            }
            if let Some((k, v)) = line.split_once('=') {
                let k = k.trim();
                let v = v.trim().trim_matches('"').trim_matches('\'');
                if std::env::var_os(k).is_none() || std::env::var(k).map(|x| x.is_empty()).unwrap_or(true) {
                    std::env::set_var(k, v);
                }
            }
        }
    }
}

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let smoke_dir = PathBuf::from(env!("CARGO_MANIFEST_DIR"));
    let fern_root = smoke_dir.parent().and_then(|p| p.parent()).expect("smoke/rust under Fern SDK");
    load_dotenv(smoke_dir.join(".env"));
    load_dotenv(fern_root.join("../Benchmark/.env"));

    let api_key = std::env::var("ZEROGPU_API_KEY").unwrap_or_default();
    let project_id = std::env::var("ZEROGPU_PROJECT_ID").unwrap_or_default();
    let model = std::env::var("ZEROGPU_MODEL").unwrap_or_default();
    if api_key.trim().is_empty() || project_id.trim().is_empty() {
        eprintln!("Set ZEROGPU_API_KEY and ZEROGPU_PROJECT_ID");
        std::process::exit(1);
    }
    if model.trim().is_empty() {
        eprintln!("Set ZEROGPU_MODEL");
        std::process::exit(1);
    }

    let prompt = std::env::var("ZEROGPU_INPUT_TEXT").unwrap_or_default();
    let prompt = if prompt.trim().is_empty() {
        "In one short sentence, what is a habit tracker?".to_string()
    } else {
        prompt
    };

    let client = ApiClientBuilder::default()
        .api_key(api_key)
        .custom_header("x-project-id".to_string(), project_id)
        .build()?;

    let req = CreateResponseRequest {
        model,
        input: vec![InputMessage {
            role: InputMessageRole::User,
            content: prompt,
        }],
        text: Some(TextResponseConfig {
            format: Some(TextResponseConfigFormat {
                r#type: Some("text".into()),
            }),
        }),
    };

    let res = client.create_response(&req, None).await?;
    println!("id: {}", res.id);
    println!("model: {}", res.model);
    println!("usage: {:?}", res.usage);
    Ok(())
}
