<?php

namespace Zerogpu\Types;

use Zerogpu\Core\Json\JsonSerializableType;
use Zerogpu\Core\Json\JsonProperty;

class TextResponseConfig extends JsonSerializableType
{
    /**
     * @var ?TextResponseConfigFormat $format
     */
    #[JsonProperty('format')]
    public ?TextResponseConfigFormat $format;

    /**
     * @param array{
     *   format?: ?TextResponseConfigFormat,
     * } $values
     */
    public function __construct(
        array $values = [],
    ) {
        $this->format = $values['format'] ?? null;
    }

    /**
     * @return string
     */
    public function __toString(): string
    {
        return $this->toJson();
    }
}
