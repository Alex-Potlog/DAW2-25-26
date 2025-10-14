<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Exercici 4-2</title>
</head>

<body>
    <?php

    $model = $_POST["model"] . filter_var($model, FILTER_SANITIZE_STRING)
        . filter_var($model, FILTER_SANITIZE_SPECIAL_CHARS)
        . filter_var($model, FILTER_SANITIZE_FULL_SPECIAL_CHARS)
        . trim($model);

    $marca = $_POST["marca"] . filter_var($marca, FILTER_SANITIZE_STRING)
        . filter_var($marca, FILTER_SANITIZE_SPECIAL_CHARS)
        . filter_var($marca, FILTER_SANITIZE_FULL_SPECIAL_CHARS)
        . trim($marca);

    $motor = $_POST["motor"] . filter_var($motor, FILTER_SANITIZE_STRING)
        . filter_var($motor, FILTER_SANITIZE_SPECIAL_CHARS)
        . filter_var($motor, FILTER_SANITIZE_FULL_SPECIAL_CHARS)
        . trim($motor);

    $cilindrada = $_POST["cilindrada"] . filter_var($cilindrada, FILTER_SANITIZE_STRING)
        . filter_var($cilindrada, FILTER_SANITIZE_SPECIAL_CHARS)
        . filter_var($cilindrada, FILTER_SANITIZE_FULL_SPECIAL_CHARS)
        . trim($cilindrada);

    $energia = $_POST["energia"];

    $opcions = $_POST["opcions"];

    echo "<h1>Dades del vehicle</h1>";
    echo "<p>Model: " . $model . "</p>";
    echo "<p>Marca: " . $marca . "</p>";
    echo "<p>Motor: " . $motor . "</p>";
    echo "<p>Cilindrada: " . $cilindrada . "</p>";
    echo "<p>Energia: " . $energia . "</p>";
    echo "<p>Opcions: ";
    foreach ($opcions as $opcio) {
        echo $opcio . " ";
    }
    echo "</p>";
    ?>
</body>

</html>