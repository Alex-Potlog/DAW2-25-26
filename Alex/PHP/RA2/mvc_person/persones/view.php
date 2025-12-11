<?php

class view {
  
  private $diccionari = array (
    'subtitle' => array ('inici' => 'Buscar persona', // titles for each view
                         'view1' => 'Mostrar dades nom i edat',
                         'view2' => 'Mostrar dades nom i alcada'),
    'capçalera' => array ('view1' => array('nom','edat'), // table headers for each view
                         'view2' => array('nom','alcada')));
  

public function retornar_vista ($vista, $dades=array(), $message="Dades de l'usuari") {
	
	// the main template is read (menu, message and the main body (a form or select result)
        // read entire file into a string
	$html = file_get_contents(__DIR__ . '/../site_media/html/persones_template.html');
        //print_r ($html);
	
	// subtitle of the page is writen 
	$html = str_replace('{subtitle}', $this->diccionari['subtitle'][$vista], $html);
        //print_r($html);
	
	// message passed by controller is writen 
	$html = str_replace('{message}', $message, $html);
        //print_r($html);
	
	// the HTML table with the select result is built 
	if ($vista=='view1' || $vista=='view2' ) {
		
		// the view template is read and its contents is included in the main template
		$view = file_get_contents(__DIR__ . '/../site_media/html/view_template.html');
		$html = str_replace ('{main}', $view, $html);
		
		// the table header is built and writen on the template
		$capçalera = $this->buildHeader ($vista);
		$html = str_replace('{capçalera}', $capçalera,$html);
		
		// the table contents is built and writen on the template
		$contingut = $this->buildContents ($dades);
		$html = str_replace('{contingut}', $contingut, $html);
	}
	
	 
	if ($vista=='inici' || ($vista=='view_select' && count($dades)==0) || $vista=='view_insert')
		$vista='form_select';



	print $html;
} 


private function buildHeader ($vista) {
	$str = "";
	foreach ($this->diccionari['capçalera'][$vista] as $value) 
		$str .= "<th>" . $value . "</th>";
	return $str;
} 


private function buildContents ($dades) {
	$str = "";
	for ($i=0; $i<count($dades); $i++) {
		$str .= "<tr>";
		foreach ($dades[$i] as $value) 
			$str .= "<td>$value</td>";
		$str .= "</tr>";
	}
	return $str;
}


private function buildForm ($vista) {
	$str = "";
	foreach ($this->diccionari['form'][$vista] as $value) {
	
		$str .= "<div> $value </div>";
		$str .= "<div><input type='text' name='$value' id='$value'></div>";	
	}	
	return $str;
	}

}
?>