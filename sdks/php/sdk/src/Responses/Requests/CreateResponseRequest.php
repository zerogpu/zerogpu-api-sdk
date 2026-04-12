<?php

namespace Zerogpu\Responses\Requests;

use Zerogpu\Core\Json\JsonSerializableType;
use Zerogpu\Core\Json\JsonProperty;
use Zerogpu\Types\InputMessage;
use Zerogpu\Core\Types\ArrayType;
use Zerogpu\Types\TextResponseConfig;

class CreateResponseRequest extends JsonSerializableType
{
    /**
     * @var string $model Model identifier from the ZeroGPU dashboard (e.g. summarization or IAB classify).
     */
    #[JsonProperty('model')]
    public string $model;

    /**
     * @var array<InputMessage> $input
     */
    #[JsonProperty('input'), ArrayType([InputMessage::class])]
    public array $input;

    /**
     * @var ?TextResponseConfig $text
     */
    #[JsonProperty('text')]
    public ?TextResponseConfig $text;

    /**
     * @param array{
     *   model: string,
     *   input: array<InputMessage>,
     *   text?: ?TextResponseConfig,
     * } $values
     */
    public function __construct(
        array $values,
    ) {
        $this->model = $values['model'];
        $this->input = $values['input'];
        $this->text = $values['text'] ?? null;
    }
}
