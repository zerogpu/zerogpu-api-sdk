<?php

namespace Zerogpu\Types;

use Zerogpu\Core\Json\JsonSerializableType;
use Zerogpu\Core\Json\JsonProperty;

class OutputContentBlock extends JsonSerializableType
{
    /**
     * @var ?string $type
     */
    #[JsonProperty('type')]
    public ?string $type;

    /**
     * @var ?string $text Generated model output
     */
    #[JsonProperty('text')]
    public ?string $text;

    /**
     * @param array{
     *   type?: ?string,
     *   text?: ?string,
     * } $values
     */
    public function __construct(
        array $values = [],
    ) {
        $this->type = $values['type'] ?? null;
        $this->text = $values['text'] ?? null;
    }

    /**
     * @return string
     */
    public function __toString(): string
    {
        return $this->toJson();
    }
}
