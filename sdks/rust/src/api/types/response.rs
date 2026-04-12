pub use crate::prelude::*;

#[derive(Debug, Clone, Serialize, Deserialize, Default, PartialEq, Eq, Hash)]
pub struct Response {
    #[serde(default)]
    pub id: String,
    #[serde(default)]
    pub object: String,
    /// Unix timestamp when the response was created
    #[serde(default)]
    pub created: i64,
    #[serde(default)]
    pub model: String,
    #[serde(default)]
    pub output: Vec<OutputMessage>,
    #[serde(skip_serializing_if = "Option::is_none")]
    pub usage: Option<TokenUsage>,
}

impl Response {
    pub fn builder() -> ResponseBuilder {
        <ResponseBuilder as Default>::default()
    }
}

#[derive(Clone, PartialEq, Default, Debug)]
#[non_exhaustive]
pub struct ResponseBuilder {
    id: Option<String>,
    object: Option<String>,
    created: Option<i64>,
    model: Option<String>,
    output: Option<Vec<OutputMessage>>,
    usage: Option<TokenUsage>,
}

impl ResponseBuilder {
    pub fn id(mut self, value: impl Into<String>) -> Self {
        self.id = Some(value.into());
        self
    }

    pub fn object(mut self, value: impl Into<String>) -> Self {
        self.object = Some(value.into());
        self
    }

    pub fn created(mut self, value: i64) -> Self {
        self.created = Some(value);
        self
    }

    pub fn model(mut self, value: impl Into<String>) -> Self {
        self.model = Some(value.into());
        self
    }

    pub fn output(mut self, value: Vec<OutputMessage>) -> Self {
        self.output = Some(value);
        self
    }

    pub fn usage(mut self, value: TokenUsage) -> Self {
        self.usage = Some(value);
        self
    }

    /// Consumes the builder and constructs a [`Response`].
    /// This method will fail if any of the following fields are not set:
    /// - [`id`](ResponseBuilder::id)
    /// - [`object`](ResponseBuilder::object)
    /// - [`created`](ResponseBuilder::created)
    /// - [`model`](ResponseBuilder::model)
    /// - [`output`](ResponseBuilder::output)
    pub fn build(self) -> Result<Response, BuildError> {
        Ok(Response {
            id: self.id.ok_or_else(|| BuildError::missing_field("id"))?,
            object: self
                .object
                .ok_or_else(|| BuildError::missing_field("object"))?,
            created: self
                .created
                .ok_or_else(|| BuildError::missing_field("created"))?,
            model: self
                .model
                .ok_or_else(|| BuildError::missing_field("model"))?,
            output: self
                .output
                .ok_or_else(|| BuildError::missing_field("output"))?,
            usage: self.usage,
        })
    }
}
