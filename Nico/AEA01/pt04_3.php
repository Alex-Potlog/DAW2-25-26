<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Processament del formulari</title>
</head>

<body>
    <h1>Resultat del formulari</h1>
    <?php
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        // Validar i sanejar les dades
        $dades = [];
        foreach ($_POST as $clau => $valor) {
            if (is_array($valor)) {
                $dades[$clau] = array_map(function ($item) {
                    $item = trim($item);
                    $item = htmlspecialchars($item);
                    return filter_var($item, FILTER_SANITIZE_FULL_SPECIAL_CHARS);
                }, $valor);
            } else {
                $valor = trim($valor);
                $valor = htmlspecialchars($valor);
                $dades[$clau] = filter_var($valor, FILTER_SANITIZE_FULL_SPECIAL_CHARS);
            }
        }

        // Comprovar que tots els camps són obligatòris
        foreach ($dades as $clau => $valor) {
            if (empty($valor)) {
                die("<p>Error: El camp '$clau' és obligatori.</p>");
            }
        }

        // Mostrar les dades recollides
        echo "<h2>Dades recollides:</h2>";
        echo "<ul>";
        foreach ($dades as $clau => $valor) {
            if (is_array($valor)) {
                echo "<li><strong>$clau:</strong> " . implode(", ", $valor) . "</li>";
            } else {
                echo "<li><strong>$clau:</strong> $valor</li>";
            }
        }
        echo "</ul>";
    } else {
        echo "<p>Error: No s'ha enviat cap formulari.</p>";
    }
    ?>
</body>

</html>