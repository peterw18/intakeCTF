<?php

$uploadDir = __DIR__ . '/uploads/';
if (!is_dir($uploadDir)) {
    mkdir($uploadDir, 0700, true);
}

// Get filename from query string (?name=...)
$filename = isset($_GET['name']) ? basename($_GET['name']) : ('file_' . uniqid());

// Save file to uploads/
$filepath = $uploadDir . $filename;

// Read raw POST data
$data = file_get_contents('php://input');

// Write file
file_put_contents($filepath, $data);

?>