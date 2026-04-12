pub use crate::prelude::*;

#[derive(Debug, Clone, Serialize, Deserialize, Default, PartialEq, Eq, Hash)]
pub struct TextResponseConfig {
    #[serde(skip_serializing_if = "Option::is_none")]
    pub format: Option<TextResponseConfigFormat>,
}

impl TextResponseConfig {
    pub fn builder() -> TextResponseConfigBuilder {
        <TextResponseConfigBuilder as Default>::default()
    }
}

#[derive(Clone, PartialEq, Default, Debug)]
#[non_exhaustive]
pub struct TextResponseConfigBuilder {
    format: Option<TextResponseConfigFormat>,
}

impl TextResponseConfigBuilder {
    pub fn format(mut self, value: TextResponseConfigFormat) -> Self {
        self.format = Some(value);
        self
    }

    /// Consumes the builder and constructs a [`TextResponseConfig`].
    pub fn build(self) -> Result<TextResponseConfig, BuildError> {
        Ok(TextResponseConfig {
            format: self.format,
        })
    }
}
