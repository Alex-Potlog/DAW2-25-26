<?php
/*Crea la següent estructura de fitxers:
    ACT15_up
        uploads/
        Act15_up.html
        Act15_up.php

Comprova que en el fitxer de configuració php.ini està permesa la pujada de fitxers (file_uploads = On)

En FILE_UPLOAD  trobaràs el codi del fitxer act15_up.html (formulari per pujar el fitxer) i el codi del fitxer act15.php (pujar i comprovar)

Puja un fitxer al servidor.

Revisa el programa act15_up.php, entenent què fa i perquè, afegint comentaris aclaridors.

Afegeix al codi la visualització del contingut de les superglobals $_FILES i $_POST. Entens les dades que contenen?

Assegura't que entens la utilitat de les funcions basename(), pathinfo(), isset(), file_exists() i htmlspecialchars().Et pot ajudar escriure-ho amb les teves paraules en un comentari del codi o utilitzant la funció echo().*/
$target_dir = "uploads/";
$target_file = $target_dir . basename($_FILES["fileToUpload"]["name"]);
$uploadOk = 1;
$imageFileType = strtolower(pathinfo($target_file, PATHINFO_EXTENSION));

// Check if image file is a actual image or fake image
if (isset($_POST["submit"])) { //Comprova que s'ha fet submit al formulari
    $check = getimagesize($_FILES["fileToUpload"]["tmp_name"]); //Comprova que el fitxer és una imatge
    if ($check !== false) {
        echo "File is an image - " . $check["mime"] . "."; //Mostra el tipus de fitxer
        $uploadOk = 1;
    } else {
        echo "File is not an image."; //tengo que comentar esto?
        $uploadOk = 0;
    }
}

// Check if file already exists
if (file_exists($target_file)) {
    echo "Sorry, file already exists."; //SE INGLES
    $uploadOk = 0;
}

// Check file size
if ($_FILES["fileToUpload"]["size"] > 500000) { //Limita el tamany del fitxer a 500KB
    echo "Sorry, your file is too large.";
    $uploadOk = 0;
}

// Allow certain file formats
if (
    $imageFileType != "jpg" && $imageFileType != "png" && $imageFileType != "jpeg"
    && $imageFileType != "gif" //Limita els formats permesos a JPG, JPEG, PNG i GIF
) {
    echo "Sorry, only JPG, JPEG, PNG & GIF files are allowed.";
    $uploadOk = 0;
}

// Check if $uploadOk is set to 0 by an error
if ($uploadOk == 0) {
    echo "Sorry, your file was not uploaded.";
    // if everything is ok, try to upload file
} else {
    if (move_uploaded_file($_FILES["fileToUpload"]["tmp_name"], $target_file)) { //Mou el fitxer pujat a la carpeta de destinació
        echo "The file " . htmlspecialchars(basename($_FILES["fileToUpload"]["name"])) . " has been uploaded."; //Mostra un missatge de confirmació
    } else {
        echo "Todo funciona menos tu"; //Mostra un missatge d'error si no s'ha pogut pujar el fitxer
    }
}

//6. Afegeix al codi la visualització del contingut de les superglobals $_FILES i $_POST. Entens les dades que contenen?
echo "<h2>Contingut de \$_FILES:</h2>";
echo "<pre>";
print_r($_FILES); //Mostra el contingut de la superglobal $_FILES
echo "</pre>";

echo "<h2>Contingut de \$_POST:</h2>";
echo "<pre>";
print_r($_POST); //Mostra el contingut de la superglobal $_POST
echo "</pre>";

//$_FILES conté informació sobre el fitxer pujat com el nom, tipus, tamany, etc.
//$_POST conté informació enviada des del formulari com el botó de submit.

//basename() es una funció que retorna el nom del fitxer a partir de la ruta completa.
//com funciona: basename('/etc/sudoers.d') retorna 'sudoers.d'

//pathinfo() es una funció que retorna informació sobre la ruta d'un fitxer com el nom, extensió, etc.
//com funciona: pathinfo('/www/htdocs/inc/lib.inc.php') retorna un array amb
//dirname: '/www/htdocs/inc'
//basename: 'lib.inc.php'
//extension: 'php'
//filename: 'lib.inc'


//isset() es una funció que comprova si una variable està definida i no és null.
//com funciona: isset($var) retorna true si $var està definida i no és null, sinó retorna false.

//file_exists() es una funció que comprova si un fitxer o directori existeix.
//com funciona: file_exists('/path/to/file') retorna true si el fitxer existeix, sinó retorna false.


//htmlspecialchars() es una funció que converteix caràcters especials en entitats HTML per evitar vulnerabilitats XSS.
//com funciona: htmlspecialchars('<a href="test">Test</a>') retorna '&lt;a href=&quot;test&quot;&gt;Test&lt;/a&gt;'
