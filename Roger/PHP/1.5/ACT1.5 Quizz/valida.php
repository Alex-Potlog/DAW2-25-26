<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>

    <?php
    $llista_preguntes = json_decode($_POST["pregunta"], true);

    $resposta = $_POST["resposta"] - 1; # Es -1, ja que es un array i comença en el 0

    $correcte = $llista_preguntes["answers"];

    if ($llista_preguntes["correctIndex"] == $resposta) {
        echo "resposta correcta";
    } else {
        echo "La resposta {$correcte[$resposta]} es incorrecta ";
    }

    echo "</br> la resposta correcta es " . $correcte[$llista_preguntes["correctIndex"]];


    ?>
</body>

</html>