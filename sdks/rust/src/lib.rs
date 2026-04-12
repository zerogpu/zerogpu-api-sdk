//! # ZeroGPU API SDK
//!
//! The official Rust SDK for the ZeroGPU API.
//!
//! ## Getting Started
//!
//! ```rust
//! use zerogpu_api::prelude::*;
//!
//! #[tokio::main]
//! async fn main() {
//!     let config = ClientConfig {
//!         api_key: Some("<value>".to_string()),
//!         ..Default::default()
//!     };
//!     let client = ApiClient::new(config).expect("Failed to build client");
//!     client
//!         .responses
//!         .create_response(
//!             &CreateResponseRequest {
//!                 model: "model".to_string(),
//!                 input: vec![InputMessage {
//!                     role: InputMessageRole::User,
//!                     content: "content".to_string(),
//!                 }],
//!                 text: None,
//!             },
//!             None,
//!         )
//!         .await;
//! }
//! ```
//!
//! ## Modules
//!
//! - [`api`] - Core API types and models
//! - [`client`] - Client implementations
//! - [`config`] - Configuration options
//! - [`core`] - Core utilities and infrastructure
//! - [`error`] - Error types and handling
//! - [`prelude`] - Common imports for convenience

pub mod api;
pub mod client;
pub mod config;
pub mod core;
pub mod environment;
pub mod error;
pub mod prelude;

pub use api::*;
pub use client::*;
pub use config::*;
pub use core::*;
pub use environment::*;
pub use error::{ApiError, BuildError};
