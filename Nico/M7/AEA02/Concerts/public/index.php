<?php
define('BASE_PATH', __DIR__ . '/../');
define('SRC_PATH', __DIR__ . '/../src/');
define('PUBLIC_PATH', __DIR__ . '/');
define('CONTROLLERS_PATH', SRC_PATH . 'controllers/');
define('MODELS_PATH', SRC_PATH . 'models/');

// echo "Base Path: " . BASE_PATH . "\n";
// echo "<br>";
// echo "Controllers Path: " . CONTROLLERS_PATH . "\n";
// echo "<br>";
// echo "SRC Path: " . SRC_PATH . "\n";

error_reporting(-1);
ini_set('display_errors', 'On');
// exit;
$uri = parse_url($_SERVER['REQUEST_URI'], PHP_URL_PATH);
$uri = trim($uri, '/');
$segments = explode('/', $uri);
$route = isset($segments[0]) && $segments[0] != '' ? $segments[0] : 'concerts';
if ($route == 'admin') {
    require_once CONTROLLERS_PATH . "AdminController.php";
    $controller = new AdminController();
} elseif ($route == 'users') {
    require_once CONTROLLERS_PATH . "UserController.php";
    $controller = new UserController();
} else {
    // header("HTTP/1.0 404 Not Found");
    echo "404 Not Found";
    exit;;
}

// require_once CONTROLLERS_PATH . "UsersController.php";
// $controller = new UsersController();
// require_once CONTROLLERS_PATH . "ConcertsController.php";
// $controller = new ConcertsController();

$controller->handler();
