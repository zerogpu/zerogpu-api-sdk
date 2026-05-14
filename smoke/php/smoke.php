<?php

declare(strict_types=1);

/**
 * Live smoke: one POST /v1/responses via Fern-generated PHP SDK.
 */
require __DIR__ . '/vendor/autoload.php';

use Zerogpu\Types\InputMessage;
use Zerogpu\Types\InputMessageRole;
use Zerogpu\Responses\Requests\CreateResponseRequest;
use Zerogpu\Types\TextResponseConfig;
use Zerogpu\Types\TextResponseConfigFormat;
use Zerogpu\ZerogpuClient;

function load_dotenv(string $path): void
{
    if (!is_readable($path)) {
        return;
    }
    foreach (file($path, FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES) ?: [] as $line) {
        $line = trim($line);
        if ($line === '' || str_starts_with($line, '#')) {
            continue;
        }
        if (!str_contains($line, '=')) {
            continue;
        }
        [$k, $v] = explode('=', $line, 2);
        $k = trim($k);
        $v = trim($v, " \t\"'");
        if (($k !== '') && getenv($k) === false) {
            putenv("$k=$v");
            $_ENV[$k] = $v;
        }
    }
}

$here = __DIR__;
$fern = dirname($here, 2);
load_dotenv("$here/.env");
load_dotenv(dirname($fern) . '/Benchmark/.env');

$apiKey = trim((string) getenv('ZEROGPU_API_KEY'));
$projectId = trim((string) getenv('ZEROGPU_PROJECT_ID'));
$model = trim((string) getenv('ZEROGPU_MODEL'));
if ($apiKey === '' || $projectId === '') {
    fwrite(STDERR, "Set ZEROGPU_API_KEY and ZEROGPU_PROJECT_ID\n");
    exit(1);
}
if ($model === '') {
    fwrite(STDERR, "Set ZEROGPU_MODEL\n");
    exit(1);
}

$prompt = trim((string) getenv('ZEROGPU_INPUT_TEXT'));
if ($prompt === '') {
    $prompt = 'In one short sentence, what is a habit tracker?';
}

$client = new ZerogpuClient($apiKey, $projectId);

$req = new CreateResponseRequest([
    'model' => $model,
    'input' => [
        new InputMessage([
            'role' => InputMessageRole::User,
            'content' => $prompt,
        ]),
    ],
    'text' => new TextResponseConfig([
        'format' => new TextResponseConfigFormat([
            'type' => 'text',
        ]),
    ]),
]);

$res = $client->responses->createResponse($req);
if ($res === null) {
    fwrite(STDERR, "Unexpected null response\n");
    exit(1);
}

echo 'id: ' . $res->id . PHP_EOL;
echo 'model: ' . $res->model . PHP_EOL;
echo 'usage: ' . json_encode($res->usage) . PHP_EOL;
