<?php

namespace Zerogpu\Types;

use Zerogpu\Core\Json\JsonSerializableType;
use Zerogpu\Core\Json\JsonProperty;

class InputMessage extends JsonSerializableType
{
    /**
     * @var value-of<InputMessageRole> $role Message author role
     */
    #[JsonProperty('role')]
    public string $role;

    /**
     * @var string $content Message text
     */
    #[JsonProperty('content')]
    public string $content;

    /**
     * @param array{
     *   role: value-of<InputMessageRole>,
     *   content: string,
     * } $values
     */
    public function __construct(
        array $values,
    ) {
        $this->role = $values['role'];
        $this->content = $values['content'];
    }

    /**
     * @return string
     */
    public function __toString(): string
    {
        return $this->toJson();
    }
}
