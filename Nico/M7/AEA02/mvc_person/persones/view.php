<?php

class view
{

	private $diccionari = array(
		'subtitle' => array(
			'inici' => 'Buscar persona', // titles for each view
			'view1' => 'Mostrar dades nom i edat',
			'view2' => 'Mostrar dades nom i alcada',
			'form-select' => 'Formulari de selecció de persona',
			'view-select' => 'Dades de la persona',
			'form-insert' => 'Formulari d\'inserció de persona',
			'view-insert' => 'Dades de totes les persones',
			'form-update' => 'Formulari d\'actualització de persona',
			'view-update' => 'Dades actualitzades de la persona',
			'form-delete' => 'Formulari d\'esborrat de persona',
			'view-delete' => 'Dades restants de les persones'
		),
		'capçalera' => array(
			'view1' => array('nom', 'edat'), // table headers for each view
			'view2' => array('nom', 'alcada'),
			'view-select' => array('nom', 'edat', 'alcada'),
			'view-insert' => array('nom', 'edat', 'alcada'),
			'view-update' => array('nom', 'edat', 'alcada'),
			'view-delete' => array('nom', 'edat', 'alcada')
		),
		'form' => array(
			'form-select' => array('nom'),
			'form-insert' => array('nom', 'edat', 'alcada'),
			'form-update' => array('nom', 'edat', 'alcada'),
			'form-delete' => array('nom')
		)
	);


	public function retornar_vista($vista, $dades = array(), $message = "Dades de l'usuari")
	{
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
		if ($vista == 'view1' || $vista == 'view2' || $vista == 'view-select' || $vista == 'view-insert' || $vista == 'view-update' || $vista == 'view-delete') {

			// the view template is read and its contents is included in the main template
			$view = file_get_contents(__DIR__ . '/../site_media/html/view_template.html');
			$html = str_replace('{main}', $view, $html);

			// the table header is built and writen on the template
			$capçalera = $this->buildHeader($vista);
			$html = str_replace('{capçalera}', $capçalera, $html);

			// the table contents is built and writen on the template
			$contingut = $this->buildContents($dades);
			$html = str_replace('{contingut}', $contingut, $html);
		}

		if ($vista == 'form-select' || $vista == 'form-insert' || $vista == 'form-update' || $vista == 'form-delete') {
			// the form template is read and its contents is included in the main template
			$form = file_get_contents(__DIR__ . '/../site_media/html/form_template.html');
			$html = str_replace('{main}', $form, $html);

			$html = str_replace('{url}', "view-" . explode('-', $vista)[1], $html);

			// the form fields are built and writen on the template
			$fields = $this->buildForm($vista);
			$html = str_replace('{contingut}', $fields, $html);
		}

		if ($vista == 'inici' || ($vista == 'view-select' && count($dades) == 0) || $vista == 'view-insert')
			$vista = 'form-select';

		print $html;
	}


	private function buildHeader($vista)
	{
		$str = "";
		foreach ($this->diccionari['capçalera'][$vista] as $value)
			$str .= "<th>" . $value . "</th>";
		return $str;
	}


	private function buildContents($dades)
	{
		$str = "";
		for ($i = 0; $i < count($dades); $i++) {
			$str .= "<tr>";
			foreach ($dades[$i] as $value)
				$str .= "<td>$value</td>";
			$str .= "</tr>";
		}
		return $str;
	}


	private function buildForm($vista)
	{
		$str = "";
		foreach ($this->diccionari['form'][$vista] as $value) {

			$str .= "<div> $value </div>";
			$str .= "<div><input type='text' name='$value' id='$value'></div>";
		}
		return $str;
	}
}
