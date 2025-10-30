<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>Resultat del formulari</h1>
    <?php 

    //verificació de que la petició s'ha fet amb el mètode post
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        // Validar i sanejar les dades
        $dades = [];
        
        foreach ($_POST as $clau => $valor) { //foreach que recorre tots els camps del formulari 
            // Aquest if agafa les dades dels camps que són arrays (com els chechboxes o de sel·lecció múltiples) i així protegeix contra atacs XSS, netejant el contingut.
            if (is_array($valor)) {
                $dades[$clau] = array_map(function ($item) { //aplica sanejament a cada element del array utilitzant el array_map
                    $item = trim($item);
                    $item = htmlspecialchars($item);
                    return filter_var($item, FILTER_SANITIZE_FULL_SPECIAL_CHARS);
                }, $valor);
            } else { //Aquest else agafa les dades dels camps simples, com els de text, i així protegeix contra atacs XSS, netejant el contingut. Aplica directament el sanejament a cada valor.
                $valor = trim($valor);
                $valor = htmlspecialchars($valor);
                $dades[$clau] = filter_var($valor, FILTER_SANITIZE_FULL_SPECIAL_CHARS);
            }
        }

        // Comprovar que tots els camps són obligatòris i que per tant tenen algun valor
        foreach ($dades as $clau => $valor) {
            if (empty($valor)) {
                die("<p>Error: El camp '$clau' és obligatori.</p>");
            }
        }

        // Mostrar les dades recollides, permetent mostrar les dades en format llista html.
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


