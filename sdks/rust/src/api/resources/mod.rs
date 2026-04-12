//! Service clients and API endpoints
//!
//! This module contains client implementations for:
//!
//! - **Responses**

use crate::{ApiError, ClientConfig};

pub mod responses;
pub struct APIClient {
    pub config: ClientConfig,
    pub responses: ResponsesClient,
}

impl APIClient {
    pub fn new(config: ClientConfig) -> Result<Self, ApiError> {
        Ok(Self {
            config: config.clone(),
            responses: ResponsesClient::new(config.clone())?,
        })
    }
}

pub use responses::ResponsesClient;
