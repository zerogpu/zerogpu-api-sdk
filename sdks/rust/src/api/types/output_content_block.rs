pub use crate::prelude::*;

#[derive(Debug, Clone, Serialize, Deserialize, Default, PartialEq, Eq, Hash)]
pub struct OutputContentBlock {
    #[serde(skip_serializing_if = "Option::is_none")]
    pub r#type: Option<String>,
    /// Generated model output
    #[serde(skip_serializing_if = "Option::is_none")]
    pub text: Option<String>,
}

impl OutputContentBlock {
    pub fn builder() -> OutputContentBlockBuilder {
        <OutputContentBlockBuilder as Default>::default()
    }
}

#[derive(Clone, PartialEq, Default, Debug)]
#[non_exhaustive]
pub struct OutputContentBlockBuilder {
    r#type: Option<String>,
    text: Option<String>,
}

impl OutputContentBlockBuilder {
    pub fn r#type(mut self, value: impl Into<String>) -> Self {
        self.r#type = Some(value.into());
        self
    }

    pub fn text(mut self, value: impl Into<String>) -> Self {
        self.text = Some(value.into());
        self
    }

    /// Consumes the builder and constructs a [`OutputContentBlock`].
    pub fn build(self) -> Result<OutputContentBlock, BuildError> {
        Ok(OutputContentBlock {
            r#type: self.r#type,
            text: self.text,
        })
    }
}
