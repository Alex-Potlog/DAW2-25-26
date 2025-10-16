<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Imatges dinamiques</title>
</head>

<body>

    <?php
    /*El lloc web http://www.portalmochis.net/humor/ilusiones/ trobaràs un repositori d'imatges.

Fer un script que mostri totes les imatges en una taula de dues columnes.

Utilitza la funció file_get_contents() per obtenir el contingut del lloc.

Utilitza la funció preg_match_all() per seleccionar els noms de les imatges.

Utilitza funcions de cadenes per recuperar el nom exacte de la imatge

Utilitza echo "<img src='https://www.portalmochis.net/humor/ilusiones/angelesdemonios.jpg'>"; per mostrar cada imatge dins de la cel·la.*/
    $paginaImatges = "http://www.portalmochis.net/humor/ilusiones/";
    $contingut = file_get_contents($paginaImatges);
    preg_match_all('/<img src="(.*?)"/', $contingut, $matches);
    $imatges = $matches[1];
    echo "<table border='1'>";
    $columna = 0;
    foreach ($imatges as $imatge) {
        if ($columna % 2 == 0) {
            echo "<tr>";
        }
        echo "<td><img src='" . $paginaImatges . $imatge . "'></td>";
        if ($columna % 2 == 1) {
            echo "</tr>";
        }
        $columna++;
    }
    if ($columna % 2 != 0) {
        echo "<td></td></tr>";
    }
    echo "</table>";





    ?>

</body>

</html>