<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <form method="POST" action="quizz.php">
        <?php
            $content_json=file_get_contents('Quiz.json'); //Em llegeix el contingut del fitxer que l'hi he passat per parametre.

            $decoded_json=json_decode($content_json, true); //Decodifica el contingut del fitxer JSON.
            
            if ($_SERVER["REQUEST_METHOD"] == "POST") {
                $index=$_POST['preguntaActual'];
                
                //Mostra si la resposta es correcte o no
                $q= $decoded_json['questions'][$index];

                $preg=$q['question'];
                $correctIndex= $q['correctIndex'];
                $resp=$q['answers'][$correctIndex];
                $respSelect=$_POST['preg_'];

                echo "La pregunta és <b>".$preg."</b><br>";
                echo "La resposta correcte és <b>".$resp."</b><br>";
                echo "La teva resposta ha sigut <b>".$q['answers'][$respSelect]."</b><br>";

                if ($correctIndex == $respSelect){
                    echo "Resposta <b>CORRECTE</b>";
                } else {
                    echo "Resposta <b>INCORRECTE</b>";
                }
                
                $index++;
                echo "<input type='hidden' value=".$index." name='preguntaActual'/>";
                echo "<br><button type='submit' name='submit'>Següent pregunta</button>";
            
            } else{
                echo "<p>Error: No s'ha enviat cap formulari.</p>";
            }   
        ?>
    </form>
</body>
</html>