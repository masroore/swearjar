<?php
$c = include 'badwords.php';
echo json_encode($c, JSON_UNESCAPED_UNICODE|JSON_PRETTY_PRINT);