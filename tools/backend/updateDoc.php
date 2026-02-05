<?php
$secretFile = '/home/backend/docsecret.txt';
$targetDir = '/var/www/html/documentation';
$uploadField = 'build';

if (!file_exists($secretFile)) {
    echo('Secret file not found: ' . $secretFile . PHP_EOL);
    http_response_code(500);
    echo 'Secret file not found.' . PHP_EOL;
    exit;
}

$expected = trim((string)file_get_contents($secretFile));
$providedB64 = (string)($_POST['secret_b64'] ?? '');
$provided = '';
if ($providedB64 !== '') {
    $decoded = base64_decode($providedB64, true);
    if ($decoded !== false) {
        $provided = $decoded;
    }
}

if ($provided === '') {
    echo('Secret provided is empty or missing.' . PHP_EOL);
}

if ($expected === '' || !hash_equals($expected, $provided)) {
    echo('Invalid secret provided.' . PHP_EOL);
    http_response_code(403);
    echo 'Invalid secret.' . PHP_EOL;
    exit;
}

if (!isset($_FILES[$uploadField]) || $_FILES[$uploadField]['error'] !== UPLOAD_ERR_OK) {
    http_response_code(400);
    echo 'Missing or invalid upload.' . PHP_EOL;
    exit;
}

$tmpPath = $_FILES[$uploadField]['tmp_name'];
$zip = new ZipArchive();

if ($zip->open($tmpPath) !== true) {
    echo('Zip open failed. Temp path: ' . $tmpPath . PHP_EOL);
    http_response_code(400);
    echo 'Invalid zip file.' . PHP_EOL;
    exit;
}

if (!is_dir($targetDir) && !mkdir($targetDir, 0755, true)) {
    echo('Unable to create target directory: ' . $targetDir . PHP_EOL);
    http_response_code(500);
    echo 'Unable to create target directory.' . PHP_EOL;
    $zip->close();
    exit;
}

$testFile = rtrim($targetDir, '/\\') . '/.write_test';
if (@file_put_contents($testFile, 'ok') === false) {
    echo('Write permission test failed in: ' . $targetDir . PHP_EOL);
    http_response_code(500);
    echo 'Write permission test failed.' . PHP_EOL;
    $zip->close();
    exit;
}
@unlink($testFile);
echo('Write permission test ok.' . PHP_EOL);

$iterator = new RecursiveIteratorIterator(
    new RecursiveDirectoryIterator($targetDir, FilesystemIterator::SKIP_DOTS),
    RecursiveIteratorIterator::CHILD_FIRST
);

foreach ($iterator as $item) {
    if ($item->isDir()) {
        @rmdir($item->getPathname());
    } else {
        @unlink($item->getPathname());
    }
}

if (!$zip->extractTo($targetDir)) {
    echo('Failed to extract zip to: ' . $targetDir . PHP_EOL);
    http_response_code(500);
    echo 'Failed to extract zip.' . PHP_EOL;
    $zip->close();
    exit;
}

$zip->close();

echo 'OK' . PHP_EOL;
