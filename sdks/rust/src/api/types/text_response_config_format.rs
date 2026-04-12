pub use crate::prelude::*;

#[derive(Debug, Clone, Serialize, Deserialize, Default, PartialEq, Eq, Hash)]
pub struct TextResponseConfigFormat {
    /// Response format type (e.g. `text`)
    #[serde(skip_serializing_if = "Option::is_none")]
    pub r#type: Option<String>,
}

impl TextResponseConfigFormat {
    pub fn builder() -> TextResponseConfigFormatBuilder {
        <TextResponseConfigFormatBuilder as Default>::default()
    }
}

#[derive(Clone, PartialEq, Default, Debug)]
#[non_exhaustive]
pub struct TextResponseConfigFormatBuilder {
    r#type: Option<String>,
}

impl TextResponseConfigFormatBuilder {
    pub fn r#type(mut self, value: impl Into<String>) -> Self {
        self.r#type = Some(value.into());
        self
    }

    /// Consumes the builder and constructs a [`TextResponseConfigFormat`].
    pub fn build(self) -> Result<TextResponseConfigFormat, BuildError> {
        Ok(TextResponseConfigFormat {
            r#type: self.r#type,
        })
    }
}
