<?php
$pregunta = json_decode($_POST['pregunta'], true);


$respostesPos = $pregunta['answers'];

if ($pregunta['correctIndex'] == $_POST['resposta'] - 1) {
    echo "CORRECT!!! ";
} else {
    echo "The answer " . $respostesPos[$_POST['resposta'] - 1] . " was incorrect :( . ";
}

echo "The answer was " . $respostesPos[$pregunta['correctIndex']];

echo "</br></br>";

echo "<a href='quizz.php'>Do another question</a>";
