<?php

class view {

private $diccionari = array (
    //afegir aquí el que necessitem per la 'consulta'
	'subtitle' => array (
		'inici' => 'Buscar persona', // titles for each view
        'view1' => 'Mostrar dades nom i edat',
        'view2' => 'Mostrar dades nom i alcada',//TODO añadir todos los casos para que se muestre la informacion
		'form_select' => 'Formulari de selecció de persona',
		'view_select' => 'Dades de la persona',
		'form_insert' => 'Formulari d\'inserció de persona',
		'view_insert' => 'Dades de totes les persones'
	), 
    'capçalera' => array (
		'view1' => array('nom','edat'), // table headers for each view
        'view2' => array('nom','alcada'),
		'view_select' => array('nom','edat','alcada'),
		'view_insert' => array('nom','edat','alcada')
	),
	'form' => array(
		'form_select' => array('nom'), //TODO añadir mas formularios (los que haga falta para el ejercicio)
		'form_insert' => array('nom', 'edat', 'alcada'),
	)
);
//Aqui hauriem d'afegir la part del form

//POssibles modificacions per a que és vegin les dades que ha recollit per la consulta.
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
	
	if ($vista=='inici' || ($vista=='view_select' && count($dades)==0)){
		$vista='form_select';
	}
	
	if($vista=='form_select') {
		// the form template is read and its contents is included in the main template
		$form = file_get_contents(__DIR__ . '/../site_media/html/form_template.html');
		$html = str_replace ('{main}', $form, $html);
		
		$html = str_replace('{url}', "view_select",$html);

		// the form fields are built and writen on the template
		$fields = $this->buildForm ($vista);
		$html = str_replace('{contingut}', $fields,$html);
	}

	if ($vista=='view_select' && count($dades)>0 || $vista == 'view_insert' && count($dades)>0) {
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

	if($vista == 'form_insert'){
		$form = file_get_contents(__DIR__ . '/../site_media/html/formInsert_template.html');
		$html = str_replace ('{main}', $form, $html);

		$html = str_replace('{url}', "view_insert",$html);

		$fields = $this->buildForm ($vista);
		$html = str_replace('{contingut}', $fields,$html);
	}

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