pub use crate::prelude::*;

#[derive(Debug, Clone, Serialize, Deserialize, PartialEq, Eq, Hash)]
pub struct InputMessage {
    /// Message author role
    pub role: InputMessageRole,
    /// Message text
    #[serde(default)]
    pub content: String,
}

impl InputMessage {
    pub fn builder() -> InputMessageBuilder {
        <InputMessageBuilder as Default>::default()
    }
}

#[derive(Clone, PartialEq, Default, Debug)]
#[non_exhaustive]
pub struct InputMessageBuilder {
    role: Option<InputMessageRole>,
    content: Option<String>,
}

impl InputMessageBuilder {
    pub fn role(mut self, value: InputMessageRole) -> Self {
        self.role = Some(value);
        self
    }

    pub fn content(mut self, value: impl Into<String>) -> Self {
        self.content = Some(value.into());
        self
    }

    /// Consumes the builder and constructs a [`InputMessage`].
    /// This method will fail if any of the following fields are not set:
    /// - [`role`](InputMessageBuilder::role)
    /// - [`content`](InputMessageBuilder::content)
    pub fn build(self) -> Result<InputMessage, BuildError> {
        Ok(InputMessage {
            role: self.role.ok_or_else(|| BuildError::missing_field("role"))?,
            content: self
                .content
                .ok_or_else(|| BuildError::missing_field("content"))?,
        })
    }
}
