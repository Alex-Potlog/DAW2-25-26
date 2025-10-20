<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>

    <?php

    /*
    Funcio on ens assegurem que no hi hagi espaix en vuit o altres caracters que puguin causar un error mes endavant
    */
    function netjarDades($info)
    {
        $info = strip_tags($info);
        $info = trim($info); #Per eliminar caractes invisibles al principi i final
        $info = htmlspecialchars($info, ENT_QUOTES, 'UTF_8');
        return $info;
    }

    $dades = [];

    /*
    Es s'obteneix la informació de totes les varibles en el metode post del formulari a traves de un foreach i es guerda
    */
    foreach ($_POST as $clau => $resultat) {
        if (is_array($resultat)) {
            $dades[$clau] = array_map('netjarDades', $resultat);
        } else {
            $dades[$clau] = netjarDades($resultat);
        }
    }

    $infoBuida = false;

    /*
    Bucle per validar si esta buit la informació per controlar-ho mes endavant
    */
    foreach ($dades as $clau => $resultat) {
        if (empty($dades[$clau])) {
            $infoBuida = true;
        }
    }

    /*
    Condició per retornar al formulari si no hi ha informacio
    */
    if ($infoBuida) {
        echo "<span>No pot haver ningun camp vuit</span>";
        echo "<span><a href='ex4.2.php'>Torna al formulari</a></span>";
        exit;
    }

    echo "<table>";
    echo "<tr><th>Camp</th><th>resultat</th></tr>";

    /**
     * Processa un array de dades i les mostra en una taula HTML, ignorant l'element "enviar"
     */
    foreach ($dades as $clau => $resultat) {
        if ($clau != "enviar") {

            echo "<tr>";
            echo "<td>" . htmlspecialchars($clau) . "</td><td>"; #el htmlspecialchars es per seguretat de la informació
            if (is_array($resultat)) {
                echo "<span>" . implode(", ", $resultat) . "</span>"; #implode per convertir-ho en string si es un array
            } else {
                echo "<span>" . filter_var($resultat, FILTER_SANITIZE_FULL_SPECIAL_CHARS) . "</span>"; #filtervar per per sanititzar caràcters especials
            }
            echo "</td></tr>";
        }
    }

    echo "</table>";
    echo '<p><a href="ex4.2.php">Torna al formulari</a></p>';


    ?>

</body>

</html>