pub use crate::prelude::*;

#[derive(Debug, Clone, Serialize, Deserialize, Default, PartialEq, Eq, Hash)]
pub struct OutputMessage {
    #[serde(skip_serializing_if = "Option::is_none")]
    pub r#type: Option<String>,
    #[serde(skip_serializing_if = "Option::is_none")]
    pub role: Option<String>,
    #[serde(skip_serializing_if = "Option::is_none")]
    pub content: Option<Vec<OutputContentBlock>>,
}

impl OutputMessage {
    pub fn builder() -> OutputMessageBuilder {
        <OutputMessageBuilder as Default>::default()
    }
}

#[derive(Clone, PartialEq, Default, Debug)]
#[non_exhaustive]
pub struct OutputMessageBuilder {
    r#type: Option<String>,
    role: Option<String>,
    content: Option<Vec<OutputContentBlock>>,
}

impl OutputMessageBuilder {
    pub fn r#type(mut self, value: impl Into<String>) -> Self {
        self.r#type = Some(value.into());
        self
    }

    pub fn role(mut self, value: impl Into<String>) -> Self {
        self.role = Some(value.into());
        self
    }

    pub fn content(mut self, value: Vec<OutputContentBlock>) -> Self {
        self.content = Some(value);
        self
    }

    /// Consumes the builder and constructs a [`OutputMessage`].
    pub fn build(self) -> Result<OutputMessage, BuildError> {
        Ok(OutputMessage {
            r#type: self.r#type,
            role: self.role,
            content: self.content,
        })
    }
}
