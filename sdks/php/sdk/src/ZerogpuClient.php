<?php

namespace Zerogpu;

use Zerogpu\Responses\ResponsesClient;
use Psr\Http\Client\ClientInterface;
use Zerogpu\Core\Client\RawClient;

class ZerogpuClient
{
    /**
     * @var ResponsesClient $responses
     */
    public ResponsesClient $responses;

    /**
     * @var array{
     *   baseUrl?: string,
     *   client?: ClientInterface,
     *   maxRetries?: int,
     *   timeout?: float,
     *   headers?: array<string, string>,
     * } $options @phpstan-ignore-next-line Property is used in endpoint methods via HttpEndpointGenerator
     */
    private array $options;

    /**
     * @var RawClient $client
     */
    private RawClient $client;

    /**
     * @param string $apiKey The apiKey to use for authentication.
     * @param string $projectId
     * @param ?array{
     *   baseUrl?: string,
     *   client?: ClientInterface,
     *   maxRetries?: int,
     *   timeout?: float,
     *   headers?: array<string, string>,
     * } $options
     */
    public function __construct(
        string $apiKey,
        string $projectId,
        ?array $options = null,
    ) {
        $defaultHeaders = [
            'x-api-key' => $apiKey,
            'x-project-id' => $projectId,
            'X-Fern-Language' => 'PHP',
            'X-Fern-SDK-Name' => 'Zerogpu',
        ];

        $this->options = $options ?? [];

        $this->options['headers'] = array_merge(
            $defaultHeaders,
            $this->options['headers'] ?? [],
        );

        $this->client = new RawClient(
            options: $this->options,
        );

        $this->responses = new ResponsesClient($this->client, $this->options);
    }
}
