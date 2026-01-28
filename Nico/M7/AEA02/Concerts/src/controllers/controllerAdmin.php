<?php
require_once MODELS_PATH . 'Concerts.php';
require_once SRC_PATH . 'views/view.php';

class ControllerAdmin
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
            case 'afegir':
                $this->afegirConcert();
                break;
            case 'modificar':
                $this->modificarSala();
                break;
            case 'index':
            default:
                $this->mostrarTots();
                break;
        }
    }

    // Mostrar tots els concerts
    private function mostrarTots($message = '')
    {
        $concerts = $this->model->selectAll();
        $data = [
            'title' => 'Tots els Concerts',
            'concerts' => $concerts,
            'message' => $message
        ];
        echo $this->view->render('concerts', $data);
    }

    // Afegir un nou concert
    public function afegirConcert()
    {
        if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
            $this->mostrarTots();
            return;
        }

        $dades = [
            'grup' => isset($_POST['grup']) ? trim($_POST['grup']) : '',
            'ciutat' => isset($_POST['ciutat']) ? trim($_POST['ciutat']) : '',
            'sala' => isset($_POST['sala']) ? trim($_POST['sala']) : '',
            'data' => isset($_POST['data']) ? $_POST['data'] : '',
            'hora' => isset($_POST['hora']) ? $_POST['hora'] : ''
        ];

        // Validar que tots els camps estiguin plens
        if (empty($dades['grup']) || empty($dades['ciutat']) || empty($dades['sala']) ||
            empty($dades['data']) || empty($dades['hora'])) {
            $message = '<div class="message error">Tots els camps són obligatoris</div>';
            $this->mostrarTots($message);
            return;
        }

        $result = $this->model->insert($dades);

        if ($result) {
            $message = '<div class="message success">Concert afegit correctament</div>';
        } else {
            $message = '<div class="message error">Error en afegir el concert</div>';
        }

        $this->mostrarTots($message);
    }

    // Modificar la sala d'un concert
    public function modificarSala()
    {
        if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
            $this->mostrarTots();
            return;
        }

        $id = isset($_POST['id']) ? intval($_POST['id']) : 0;
        $sala = isset($_POST['sala']) ? trim($_POST['sala']) : '';

        if ($id <= 0 || empty($sala)) {
            $message = '<div class="message error">ID i nova sala són obligatoris</div>';
            $this->mostrarTots($message);
            return;
        }

        // Verificar que el concert existeix
        $concert = $this->model->select($id);
        if (!$concert) {
            $message = '<div class="message error">El concert amb ID ' . $id . ' no existeix</div>';
            $this->mostrarTots($message);
            return;
        }

        $result = $this->model->update($id, $sala);

        if ($result) {
            $message = '<div class="message success">Sala modificada correctament</div>';
        } else {
            $message = '<div class="message error">Error en modificar la sala</div>';
        }

        $this->mostrarTots($message);
    }
}
