<?php
define('BASE_PATH', __DIR__ . '/../');
define('SRC_PATH', __DIR__ . '/../src/');
define('PUBLIC_PATH', __DIR__ . '/');
define('CONTROLLERS_PATH', SRC_PATH . 'controllers/');
define('MODELS_PATH', SRC_PATH . 'models/');

error_reporting(-1);
ini_set('display_errors', 'On');

// Determinar quin controlador usar basant-se en el paràmetre 'controller'
$route = isset($_GET['controller']) ? $_GET['controller'] : 'user';

switch ($route) {
    case 'admin':
        require_once CONTROLLERS_PATH . "controllerAdmin.php";
        $controller = new ControllerAdmin();
        break;
    case 'user':
    default:
        require_once CONTROLLERS_PATH . "controllerUser.php";
        $controller = new ControllerUser();
        break;
}

$controller->handler();
