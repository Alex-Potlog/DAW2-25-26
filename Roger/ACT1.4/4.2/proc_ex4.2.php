<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>

    <?php

    function netjDades($dada)
    {
        $dada = trim($dada);
        $dada = strip_tags($dada);
        $dada = htmlspecialchars($dada, ENT_QUOTES, 'UTF_8');
        return $dada;
    }

    $dades = [];

    foreach ($_POST as $clau => $valor) {
        if (is_array($valor)) {
            $dades[$clau] = array_map('netjDades', $valor);
        } else {
            $dades[$clau] = netjDades($valor);
        }
    }

    $dadaBuida = false;

    foreach ($dades as $clau => $valor) {
        if (empty($dades[$clau])) {
            $dadaBuida = true;
        }
    }

    if ($dadaBuida) {
        echo "<span>Tots els camps han de ser omplerts</span>";
        echo "<span><a href='formExer2.php'>Torna al formulari</a></span>";
        exit;
    }

    echo "<table>";
    echo "<tr><th>Camp</th><th>Valor</th></tr>";

    foreach ($dades as $clau => $valor) {
        if ($clau != "enviar") {

            echo "<tr>";
            echo "<td>" . htmlspecialchars($clau) . "</td><td>";
            if (is_array($valor)) {
                echo "<span>" . implode(", ", $valor) . "</span>";
            } else {
                echo "<span>" . filter_var($valor, FILTER_SANITIZE_FULL_SPECIAL_CHARS) . "</span>";
            }
            echo "</td></tr>";
        }
    }

    echo "</table>";
    echo '<p><a href="formExer2.php">Torna al formulari</a></p>';


    ?>

</body>

</html>