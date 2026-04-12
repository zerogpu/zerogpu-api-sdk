<?php

namespace Zerogpu\Types;

use Zerogpu\Core\Json\JsonSerializableType;
use Zerogpu\Core\Json\JsonProperty;

class TokenUsage extends JsonSerializableType
{
    /**
     * @var ?int $inputTokens
     */
    #[JsonProperty('input_tokens')]
    public ?int $inputTokens;

    /**
     * @var ?int $outputTokens
     */
    #[JsonProperty('output_tokens')]
    public ?int $outputTokens;

    /**
     * @var ?int $totalTokens
     */
    #[JsonProperty('total_tokens')]
    public ?int $totalTokens;

    /**
     * @param array{
     *   inputTokens?: ?int,
     *   outputTokens?: ?int,
     *   totalTokens?: ?int,
     * } $values
     */
    public function __construct(
        array $values = [],
    ) {
        $this->inputTokens = $values['inputTokens'] ?? null;
        $this->outputTokens = $values['outputTokens'] ?? null;
        $this->totalTokens = $values['totalTokens'] ?? null;
    }

    /**
     * @return string
     */
    public function __toString(): string
    {
        return $this->toJson();
    }
}
