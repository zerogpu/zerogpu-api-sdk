<?php

namespace Zerogpu\Types;

use Zerogpu\Core\Json\JsonSerializableType;
use Zerogpu\Core\Json\JsonProperty;

class TextResponseConfigFormat extends JsonSerializableType
{
    /**
     * @var ?string $type Response format type (e.g. `text`)
     */
    #[JsonProperty('type')]
    public ?string $type;

    /**
     * @param array{
     *   type?: ?string,
     * } $values
     */
    public function __construct(
        array $values = [],
    ) {
        $this->type = $values['type'] ?? null;
    }

    /**
     * @return string
     */
    public function __toString(): string
    {
        return $this->toJson();
    }
}
