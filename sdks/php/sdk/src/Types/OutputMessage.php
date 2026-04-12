<?php

namespace Zerogpu\Types;

use Zerogpu\Core\Json\JsonSerializableType;
use Zerogpu\Core\Json\JsonProperty;
use Zerogpu\Core\Types\ArrayType;

class OutputMessage extends JsonSerializableType
{
    /**
     * @var ?string $type
     */
    #[JsonProperty('type')]
    public ?string $type;

    /**
     * @var ?string $role
     */
    #[JsonProperty('role')]
    public ?string $role;

    /**
     * @var ?array<OutputContentBlock> $content
     */
    #[JsonProperty('content'), ArrayType([OutputContentBlock::class])]
    public ?array $content;

    /**
     * @param array{
     *   type?: ?string,
     *   role?: ?string,
     *   content?: ?array<OutputContentBlock>,
     * } $values
     */
    public function __construct(
        array $values = [],
    ) {
        $this->type = $values['type'] ?? null;
        $this->role = $values['role'] ?? null;
        $this->content = $values['content'] ?? null;
    }

    /**
     * @return string
     */
    public function __toString(): string
    {
        return $this->toJson();
    }
}
