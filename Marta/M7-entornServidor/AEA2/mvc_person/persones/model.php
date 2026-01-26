<?php

// magic constant
require_once (__DIR__ . "/../core/DBAbstractModel.php");

class persones extends DBAbstractModel {
  
  private $id;
  private $nom;
  private $edat;
  private $alcada;

  public $message;
  
  function __construct() {
    $this->db_name = "patromvc";
  }
  
  function __toString() {
    echo "entro string <br>";
    return "(" . $this->id . ", " . $this->name . ", " . $this->edat . ", " .  
      $this->alcada . ")";
  }
  
  function __destruct() {}
  
  //select dels camps passats de tots els registres
  //stored in $rows property
  public function selectAll($fields=array()) {
    
    $this->query="SELECT ";
    $firstField = true;
    for ($i=0; $i<count($fields); $i++) {
      if ($firstField) {
        $this->query .= $fields[$i];
        $firstField=false;
      }
      else $this->query .= ", " . $fields[$i];
    }
    $this->query .= " FROM persones";
    $this->get_results_from_query();
    return $this->rows;
    
  }
  
  public function select($nom="") {
      //Crear la query aqui per a consultar el nom que em entrat pel formulari 
      // i passar-les despré a la vista per a mostrar les dades

      //EL cridem al controller 
      $this->query="SELECT nom, edat, alcada FROM persones WHERE nom= '$nom'";
      $this->get_results_from_query();
      return $this->rows;
  }
  
  
  public function insert($user_data = array()) {
    //TODO queries

    $this->query="INSERT INTO persones (nom, edat, alcada) VALUES
        ('" . $user_data['nom'] . "',
        '" . $user_data['edat'] . "',
        '" . $user_data['alcada'] . "')";
    $this->execute_single_query();
  }
  
  public function update ($userData = array()) {
      $this->query="UPDATE persones SET
        nom= '".$userData['nom']."',
        edat= '".$userData['edat']."',
        alcada='".$userData['alcada']."'
        WHERE nom='".$userData['nom']."'";
      $this->execute_single_query();
  }

  public function delete ($nom="") {
  
  }
    
}

?>
