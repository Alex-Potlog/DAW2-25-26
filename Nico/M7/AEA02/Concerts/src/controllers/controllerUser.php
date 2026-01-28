<?php
require_once MODELS_PATH . 'Concerts.php';
require_once SRC_PATH . 'views/view.php';

class ControllerUser
{
    private $model;
    private $view;

    public function __construct()
    {
        $this->model = new Concerts();
        $this->view = new View();
    }

    public function handler()
    {
        $action = isset($_GET['action']) ? $_GET['action'] : 'index';

        switch ($action) {
            case 'cercargrup':
                $this->cercarPerGrup();
                break;
            case 'cercardates':
                $this->cercarPerDates();
                break;
            case 'index':
            default:
                $this->mostrarTots();
                break;
        }
    }

    // Mostrar tots els concerts
    public function mostrarTots()
    {
        $concerts = $this->model->selectAll();
        $data = [
            'title' => 'Tots els Concerts',
            'concerts' => $concerts,
            'message' => ''
        ];
        echo $this->view->render('concerts', $data);
    }

    // Cercar concerts per grup musical
    public function cercarPerGrup()
    {
        $grup = isset($_GET['grup']) ? trim($_GET['grup']) : '';

        if (empty($grup)) {
            $this->mostrarTots();
            return;
        }

        $concerts = $this->model->selectByGrup($grup);
        $data = [
            'title' => 'Resultats de cerca per grup: ' . htmlspecialchars($grup),
            'concerts' => $concerts,
            'message' => ''
        ];
        echo $this->view->render('concerts', $data);
    }

    // Cercar concerts entre dues dates
    public function cercarPerDates()
    {
        $dataInici = isset($_GET['dataInici']) ? $_GET['dataInici'] : '';
        $dataFi = isset($_GET['dataFi']) ? $_GET['dataFi'] : '';

        if (empty($dataInici) || empty($dataFi)) {
            $this->mostrarTots();
            return;
        }

        $concerts = $this->model->selectByDates($dataInici, $dataFi);
        $data = [
            'title' => 'Concerts entre ' . htmlspecialchars($dataInici) . ' i ' . htmlspecialchars($dataFi),
            'concerts' => $concerts,
            'message' => ''
        ];
        echo $this->view->render('concerts', $data);
    }
}
