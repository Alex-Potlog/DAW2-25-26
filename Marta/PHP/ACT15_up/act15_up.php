<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    
    <?php
        // phpinfo(); -> per obtenir la informació del php que tinc instal·lat
        
        $target_dir = "uploads/"; //Variable per accedir a la carpeta "uploads"
        $target_file = $target_dir . basename($_FILES["fileToUpload"]["name"]); //basename -> D'una ruta et retorna el nom final.
        $uploadOk = 1;
        $imageFileType = strtolower(pathinfo($target_file,PATHINFO_EXTENSION)); //pathinfo -> del string que li passem em retora la informació que volguem.
                                                                                // en aquest cas, de la variable que li passem em retornarà l'extensió
        
        // Check if image file is a actual image or fake image
        //Al if pare, isset-> em determina si la variable esta declarada i es diferent de null.
        if(isset($_POST["submit"])) {
            $check = getimagesize($_FILES["fileToUpload"]["tmp_name"]); //getimagesize -> em retorna una array amb informació bàsica de les dimensions de la imatge i ho guarda a $check
                                                                        //print_r($check); -> mostra informació d'arrays.
            if($check !== false) {
                echo "File is an image - " . $check["mime"] . "."; //["mime"] -> és una codificaió per saber el tipus de fitxer
                $uploadOk = 1;
            } else {
                echo "File is not an image.";
                $uploadOk = 0;
            }
        }
    ?>

</body>
</html>