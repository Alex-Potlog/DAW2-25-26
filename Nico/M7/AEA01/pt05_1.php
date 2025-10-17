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
    preg_match_all('/<a href="([^"]+\.(jpg|jpeg|png|gif))"/i', $contingut, $imatges);
    echo "<table border='1'>";
    $paginaBase = "http://www.portalmochis.net";
    foreach ($imatges[1] as $index => $imatge) {
        if ($index % 2 == 0) { //Columnes de 2
            echo "<tr>";
        }
        echo "<td><img src='" . $paginaBase . $imatge . "'></td>";
        if ($index % 2 == 1) { //Tanca la fila després de 2 columnes
            echo "</tr>";
        }
    }

    echo "</table>";






    ?>

</body>

</html>