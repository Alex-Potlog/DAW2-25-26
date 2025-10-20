<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <form method="POST" action="valida.php">
        <?php

            $content_json=file_get_contents('Quiz.json'); //Em llegeix el contingut del fitxer que l'hi he passat per parametre.

            $decoded_json=json_decode($content_json, true); //Decodifica el contingut del fitxer JSON.
            
            if (isset($_POST['preguntaActual'])){ // Si "$_POST['preguntaActual']" existeix, m'ho guarades a la variable $index
                $index=$_POST['preguntaActual'];//Variable que em dira quina pregunta mostrar segons el que ens vingui de "valida.php"
            }else { //Si $_POST['preguntaActual'] no existeix, m'inicialitzes $index a 0
                $index=0;
            }
            
            echo "<input type='hidden' value=".$index." name='preguntaActual'/>";
            $i=1;

            $q= $decoded_json['questions'][$index];
                echo "<h3>".$q['question']."</h3>";
                foreach($q['answers'] as $index => $answer){
                ?>
                <div>
                    <input type="radio" id="<?php echo "p".$i."_r".$index;?>" name="preg_" value="<?php echo $index;?>" required>
                    <label for=<?php echo "p".$i."_r".$index;?>> <?php echo htmlspecialchars($answer);?></label> <!-- htmlspecialchars -> converteix els caracters especials a entitats html-->
                </div>
                <?php
                }
                // echo "<br>";

                //foreach per a mostrar totes les preguntes del document .json
            /* foreach ($decoded_json['questions'] as $q){
                echo "<h3>".$q['question']."</h3>";
                foreach($q['answers'] as $index => $answer){
                ?>
                <div>
                    <input type="radio" id="<?php echo "p".$i."_r".$index;?>" name="<?php echo "preg_".$i;?>" value="<?php echo $index;?>" required>
                    <label for=<?php echo "p".$i."_r".$index;?>> <?php echo htmlspecialchars($answer);?></label>
                </div>
                <?php
                }
                // echo "<br>";
                $i++;
            } */
        ?>
        <br><button type="submit" name="submit">Enviar resposta</button>
    </form>

</body>
</html>