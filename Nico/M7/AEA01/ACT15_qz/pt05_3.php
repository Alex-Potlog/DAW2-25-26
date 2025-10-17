<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Quizz</title>
</head>

<body>
    <?php
    /*

2-. El programa principal accedirà al fitxer, seleccionarà un pregunta, la mostrarà en pantalla junt amb un formulari per triar la resposta.

3-. El butó submit cridarà al programa valida.php, el qual comprovarà si la resposta és correcta o no, mostrant el missatge corresponent per pantalla.

4-. El programa valida.php oferirà tornar a jugar.

5-. Utilitza les funcions file_get_contents() i json_decode().*/
    //2
    $info = json_decode(file_get_contents("questions.json"))["questions"]; //Decodifica el fitxer JSON i accedeix a l'array "questions"
    $pregunta = $info[rand(0, count($info) - 1)]; //TODO arreglar todo
    ?>
    <form action="pt05_3_1.php">
        <h3><?php echo $pregunta->question; ?></h3>
        <?php
        foreach ($pregunta->answers as $index => $resposta) {
            echo "<input type='radio' name='resposta' value='" . ($index + 1) . "'>" . $resposta . "<br>"; //Mostra les respostes com a botons de radio
        }
        ?>
        <input type="hidden" name="correcta" value="<?php echo $pregunta->correct; ?>"> <!-- Guarda la resposta correcta en un camp ocult -->
        <input type="submit" value="Enviar">
    </form>

</body>

</html>