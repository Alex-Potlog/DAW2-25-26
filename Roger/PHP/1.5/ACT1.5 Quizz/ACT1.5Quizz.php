<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>

    <?php
    $info_codificada = file_get_contents("Quiz.json");
    $llista_preguntes = json_decode($info_codificada, true)["questions"]; //El true es per a convertir-ho en un array i nomes agafar l'apartat en les preguntes

    $numero = rand(0, count($llista_preguntes) - 1);

    $pregunta = $llista_preguntes[$numero];

    echo $pregunta["question"]; //El json son elements clau valor i escribeixo la clau

    $i = 1;
    foreach ($pregunta["answers"] as $eleccions) {
        echo "</br>" . $i . ". " . $eleccions;
        $i++;
    }

    ?>

    <form action="valida.php" method="POST">
        <input type="hidden" name="pregunta" value='<?php echo json_encode($pregunta, JSON_HEX_APOS | JSON_HEX_QUOT); ?>'> <!-- json encor per guardar la info i enviarla sino no es pot -->
        <label for="resposta">Answer: </label><input type="number" name="resposta" min="1" max="4" required>
        <input type="submit" value="Send">
    </form>

</body>

</html>