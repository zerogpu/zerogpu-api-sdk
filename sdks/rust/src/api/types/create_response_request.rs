pub use crate::prelude::*;

#[derive(Debug, Clone, Serialize, Deserialize, Default, PartialEq, Eq, Hash)]
pub struct CreateResponseRequest {
    /// Model identifier from the ZeroGPU dashboard (e.g. summarization or IAB classify).
    #[serde(default)]
    pub model: String,
    #[serde(default)]
    pub input: Vec<InputMessage>,
    #[serde(skip_serializing_if = "Option::is_none")]
    pub text: Option<TextResponseConfig>,
}

impl CreateResponseRequest {
    pub fn builder() -> CreateResponseRequestBuilder {
        <CreateResponseRequestBuilder as Default>::default()
    }
}

#[derive(Clone, PartialEq, Default, Debug)]
#[non_exhaustive]
pub struct CreateResponseRequestBuilder {
    model: Option<String>,
    input: Option<Vec<InputMessage>>,
    text: Option<TextResponseConfig>,
}

impl CreateResponseRequestBuilder {
    pub fn model(mut self, value: impl Into<String>) -> Self {
        self.model = Some(value.into());
        self
    }

    pub fn input(mut self, value: Vec<InputMessage>) -> Self {
        self.input = Some(value);
        self
    }

    pub fn text(mut self, value: TextResponseConfig) -> Self {
        self.text = Some(value);
        self
    }

    /// Consumes the builder and constructs a [`CreateResponseRequest`].
    /// This method will fail if any of the following fields are not set:
    /// - [`model`](CreateResponseRequestBuilder::model)
    /// - [`input`](CreateResponseRequestBuilder::input)
    pub fn build(self) -> Result<CreateResponseRequest, BuildError> {
        Ok(CreateResponseRequest {
            model: self
                .model
                .ok_or_else(|| BuildError::missing_field("model"))?,
            input: self
                .input
                .ok_or_else(|| BuildError::missing_field("input"))?,
            text: self.text,
        })
    }
}
