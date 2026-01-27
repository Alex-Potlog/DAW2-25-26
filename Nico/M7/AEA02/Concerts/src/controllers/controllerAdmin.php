<?php
class ControllerAdmin
{


    function handler()
    {
        $uri = parse_url($_SERVER['REQUEST_URI'], PHP_URL_PATH);
        $uri = trim($uri, '/');
        $segments = explode('/', $uri);

        //var_dump($segments);
        if ($segments[1] == 'crear') {
            $this->crearAdmin();
        }

        //echo "Admin Controller";
    }


    function crearAdmin()
    {

        require_once MODELS_PATH . "Concerts.php";
        $concertsModel = new Concerts();
        //echo "Crear Admin";
    }
}
