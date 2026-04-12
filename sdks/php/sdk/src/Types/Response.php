<?php

namespace Zerogpu\Types;

use Zerogpu\Core\Json\JsonSerializableType;
use Zerogpu\Core\Json\JsonProperty;
use Zerogpu\Core\Types\ArrayType;

class Response extends JsonSerializableType
{
    /**
     * @var string $id
     */
    #[JsonProperty('id')]
    public string $id;

    /**
     * @var string $object
     */
    #[JsonProperty('object')]
    public string $object;

    /**
     * @var int $created Unix timestamp when the response was created
     */
    #[JsonProperty('created')]
    public int $created;

    /**
     * @var string $model
     */
    #[JsonProperty('model')]
    public string $model;

    /**
     * @var array<OutputMessage> $output
     */
    #[JsonProperty('output'), ArrayType([OutputMessage::class])]
    public array $output;

    /**
     * @var ?TokenUsage $usage
     */
    #[JsonProperty('usage')]
    public ?TokenUsage $usage;

    /**
     * @param array{
     *   id: string,
     *   object: string,
     *   created: int,
     *   model: string,
     *   output: array<OutputMessage>,
     *   usage?: ?TokenUsage,
     * } $values
     */
    public function __construct(
        array $values,
    ) {
        $this->id = $values['id'];
        $this->object = $values['object'];
        $this->created = $values['created'];
        $this->model = $values['model'];
        $this->output = $values['output'];
        $this->usage = $values['usage'] ?? null;
    }

    /**
     * @return string
     */
    public function __toString(): string
    {
        return $this->toJson();
    }
}
