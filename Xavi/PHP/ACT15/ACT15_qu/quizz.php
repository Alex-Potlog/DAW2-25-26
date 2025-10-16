<!DOCTYPE html>
<html lang="ca">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ACT 1.5 XRB</title>
</head>

<body>
    <?php
    $dades = json_decode(file_get_contents('Quiz.json'), true)["questions"];
    $pregunta = $dades[rand(0, count($dades) - 1)];
    echo $pregunta['question'];
    echo "</br>";
    $i = 1;
    foreach ($pregunta['answers'] as $answer) {

        echo $i . ". " . $answer;
        echo "</br>";
        $i++;
    }

    ?>
    <form action="valida.php" method="POST">
        <input type="hidden" name="pregunta" value='<?php echo json_encode($pregunta, JSON_HEX_APOS | JSON_HEX_QUOT); ?>'>
        <label for="resposta">Answer: </label><input type="number" name="resposta" min="1" max="4" required>
        <input type="submit" value="Send">
    </form>
</body>

</html>