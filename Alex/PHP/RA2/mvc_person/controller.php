<?php

require_once 'model.php';
require_once 'view.php';

class controller {
  
  //rutes o esdeveniments possibles
  //view1: nom i edat
  //view2: nom i alçada
  private $peticions = array('view1', 'view2');
  
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
        
        case 'inici':
            $view->retornar_vista($event, array());
        case 'consulta':
          $view->selectForm();
          
          $dades = $per->select();
          
        }
      
  }

}





?>