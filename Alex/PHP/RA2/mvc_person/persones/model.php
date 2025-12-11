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
  
  function __destruct() {

  }
  
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
   
  }
  
  
  public function insert($user_data = array()) {
    
     }
  
  public function update ($userData = array()) {
   
  }
 
  public function delete ($nom="") {
  
  }
 
    
}

?>
