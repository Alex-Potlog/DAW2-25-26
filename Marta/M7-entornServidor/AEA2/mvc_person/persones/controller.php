<?php

require_once 'model.php';
require_once 'view.php';

class controller {
  
  //rutes o esdeveniments possibles
  //view1: nom i edat
  //view2: nom i alçada
  //consulta: 
  private $peticions = array('view1', 'view2', 'form_select', 'view_select', 'form_insert', 'view_insert');
  
  public function handler () {
    
    // Què em demanen?
    $event = 'inici';
    
    // On som?
    $uri = $_SERVER['REQUEST_URI'];
    echo $uri;

    foreach ($this->peticions as $peticio) //Find the position of the first occurrence of a substring in a string
      if (strpos($uri,$peticio) == true)
        $event = $peticio;
          
    $per = new persones();
    
    $view = new view();
    
    switch ($event) {
        case 'view1':
          $dades = $per->selectAll(array("nom","edat"));
          $view->retornar_vista($event, $dades);
          break;
        
        case 'view2':
          $dades = $per->selectAll(array("nom","alcada"));
          $view->retornar_vista($event, $dades);
          break;
        
        //Cas en el que volem veure les dades d'una persona.
        case 'form_select': //Esto es el action realmente
        $view->retornar_vista($event);
        break;
        
        case 'view_select':
        $dades = $per->select($_POST['nom']);
        $view->retornar_vista($event, $dades);
        break;
        
        //Cas on volem inserir una nova persona i després veure les dades de totes les persones.
        case 'form_insert':
        $view->retornar_vista($event);
        break;
        
        case 'view_insert':
        //Consulta model per a inserir la nova persona
        $per->insert(array(
          'nom' => $_POST['nom'],
          'edat' => $_POST['edat'],
          'alcada' => $_POST['alcada']
        ));

        //Consulta model per a obtenir les dades de totes les persones
        $dades= $per->selectAll(array("nom","edat","alcada"));
        
        //Muestra vista amb les dades de totes les persones
        $view->retornar_vista($event, $dades);
        break;

        case 'update':
        //Muestra vista
        //Consulta model
        //TODO 3 cases (consulta, insert, update o delete)
        break;
        
        case 'delete':
        //Muestra vista
        //Consulta model
        //TODO 3 cases (consulta, insert, update o delete)
        break;

        case 'inici':
            $view->retornar_vista($event, array());
            
        }
      
  }
}





?>