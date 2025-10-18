<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=, initial-scale=1.0">
    <title>Document</title>
</head>

<body>


    <?php
    // Obtenir el contingut del lloc web
    $contingut = file_get_contents("https://www.portalmochis.net/humor/ilusiones/");

    // Utilitzar preg_match_all() per seleccionar les URLs de les imatges
    preg_match_all('/<a[^>]+href=(["\'])(.*?\.(jpg|jpeg|png|gif))\1[^>]*>/i', $contingut, $matches); //Retorna un array bidimensional

    // Base URL per les imatges
    $base_url = "https://www.portalmochis.net/humor/ilusiones/";

    echo "<table border='1' style='width:100%; border-collapse: collapse;'>";
    echo "<tr><th colspan='2'>Il·lusions Òptiques - " . count($matches[2]) . " imatges</th></tr>";

    /**
     * Depent de la condició
     * $enlaces[0] → Array amb les etiquetes <a> COMPLETES
     * $enlaces[1] → Array amb les COMENTES utilitzades (" o ')
     *$enlaces[2] → Array amb les URLS dels enllaços (el que volem)
     *$enlaces[3] → Array amb les EXTENSIONS dels arxius
     */

    $columna = 0;
    foreach ($matches[2] as $src) {
        // Utilitzar funcions de cadenes per obtenir el nom exacte
        $nom_arxiu = basename($src);
        $url_completa = $base_url . $nom_arxiu;

        // Obrir nova fila cada 2 imatges
        if ($columna % 2 == 0) {
            echo "<tr>";
        }

        // Mostrar cada imatge en la cel·la
        echo "<td style='width:50%; text-align:center; padding:10px;'>";
        echo "<img src='" . $url_completa . "' style='max-width:300px; max-height:300px;'>";
        echo "<br><small>" . $nom_arxiu . "</small>";
        echo "</td>";

        // Tancar fila cada 2 imatges
        if ($columna % 2 == 1) {
            echo "</tr>";
        }

        $columna++;
    }

    // Tancar l'última fila si queda oberta
    if ($columna % 2 == 1) {
        echo "<td></td></tr>";
    }

    echo "</table>";
    ?>


</body>

</html>