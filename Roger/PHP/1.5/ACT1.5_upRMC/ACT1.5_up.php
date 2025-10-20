<?php
$target_dir = "uploads/"; // carpeta destí
$target_file = $target_dir . basename($_FILES["fileToUpload"]["name"]); // direcció completa
$uploadOk = 1; // flag per comprovar que no hi hagi errors
$imageFileType = strtolower(pathinfo($target_file, PATHINFO_EXTENSION)); // extensió del arxiu

// Revisa si l'arxiu és una imatge
if (isset($_POST["submit"])) {
    $check = getimagesize($_FILES["fileToUpload"]["tmp_name"]);
    if ($check !== false) {
        echo "File is an image - " . $check["mime"] . ".";
        $uploadOk = 1;
    } else {
        echo "File is not an image.";
        $uploadOk = 0;
    }
}

//  Revisa si l'arxiu ja existeix a la carpeta
if (file_exists($target_file)) {
    echo "Sorry, file already exists.";
    $uploadOk = 0;
}

// Revisa el tamany de l'arxiu
if ($_FILES["fileToUpload"]["size"] > 500000) {
    echo "Sorry, your file is too large.";
    $uploadOk = 0;
}

// Revisa que el la imatge sigui de un certs formats
if (
    $imageFileType != "jpg" && $imageFileType != "png" && $imageFileType != "jpeg"
    && $imageFileType != "gif"
) {
    echo "Sorry, only JPG, JPEG, PNG & GIF files are allowed.";
    $uploadOk = 0;
}

// Revisa si el Flag es 0 (si hi ha hagut un error)
if ($uploadOk == 0) {
    echo "Sorry, your file was not uploaded.";
    // si no hi ha errors, intenta pujar l'arxiu
} else {
    if (move_uploaded_file($_FILES["fileToUpload"]["tmp_name"], $target_file)) {
        echo "The file " . htmlspecialchars(basename($_FILES["fileToUpload"]["name"])) . " has been uploaded.";
    } else {
        echo "Sorry, there was an error uploading your file.";
    }
}
echo "<pre>";
echo "</br></br>";
print_r($_FILES);
echo "</br></br>";
print_r($_POST);
echo "</pre>";

echo "</br></br>";
echo "=== DOCUMENTACIÓ DE FUNCIONS ===";
echo "</br></br>";
echo "basename() - Retorna el nom del destí final de la ruta";
echo "</br>";
echo "pathinfo() - Retorna informació sobre una ruta en forma de array";
echo "</br>";
echo "isset() - Retorna true si la variable passada existeix i no es null";
echo "</br>";
echo "file_exists() - Retorna true si la ruta existeix i false si no";
echo "</br>";
echo "htmlspecialchars() - Converteix caràcters especials en entitats HTML, per exemple & en &amp";
echo "</br>";
