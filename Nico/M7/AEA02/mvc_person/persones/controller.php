<?php

require_once 'model.php';
require_once 'view.php';

class controller
{

  //rutes o esdeveniments possibles
  //view1: nom i edat
  //view2: nom i alçada
  private $peticions = array('view1', 'view2', 'form-select', 'view-select', 'form-insert', 'view-insert', 'form-update', 'view-update', 'form-delete', 'view-delete');

  public function handler()
  {

    // Què em demanen?
    $event = 'inici';

    // On som?
    $uri = $_SERVER['REQUEST_URI'];
    echo $uri;

    foreach ($this->peticions as $peticio) //Find the position of the first occurrence of a substring in a string
      if (strpos($uri, $peticio) == true)
        $event = $peticio;

    $per = new persones();

    $view = new view();

    switch ($event) {
      case 'view1':
        $dades = $per->selectAll(array("nom", "edat"));
        $view->retornar_vista($event, $dades);
        break;

      case 'view2':
        $dades = $per->selectAll(array("nom", "alcada"));
        $view->retornar_vista($event, $dades);
        break;

      case 'form-select': //Esto es el action realmente
        $view->retornar_vista($event);
        break;
      case 'view-select':
        $dades = $per->select($_POST['nom']);
        $view->retornar_vista($event, $dades);
        break;
      case 'form-insert':
        $view->retornar_vista($event);
        break;
      case 'view-insert':
        $per->insert(array(
          'nom' => $_POST['nom'],
          'edat' => $_POST['edat'],
          'alcada' => $_POST['alcada']
        ));
        $dades = $per->selectAll(array("nom", "edat", "alcada"));
        $view->retornar_vista($event, $dades);
        break;
      case 'form-update':
        $view->retornar_vista($event);
        break;
      case 'view-update':
        $per->update(array(
          'nom' => $_POST['nom'],
          'edat' => $_POST['edat'],
          'alcada' => $_POST['alcada']
        ));
        $dades = $per->selectAll(array("nom", "edat", "alcada"));
        $view->retornar_vista($event, $dades);
        break;
      case 'form-delete':
        $view->retornar_vista($event);
        break;
      case 'view-delete':
        $per->delete($_POST['nom']);
        $dades = $per->selectAll(array("nom", "edat", "alcada"));
        $view->retornar_vista($event, $dades);
        break;

      case 'inici':
        $view->retornar_vista($event, array());
    }
  }
}
