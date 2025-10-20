<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mostra imatges Externes</title>
</head>
<body>
    <?php
        //Guardem la url d'on volem treure les imatges a una variable.
        $url="https://www.portalmochis.net/humor/ilusiones/";

        //Obtenir el contingut del lloc en format string
        $content=file_get_contents($url);
        
        // Es guarda a la variable "$patro" tot un conjunt de caracters que generen un patró per identificar els noms dels fitxers que volem.
        // En aquest cas busca les etiquetes <a> on els enllaços href contingui extensions d'imatge

                // Patró per capturar els noms dels fitxers d'imatge
                // Busca etiquetes <a> amb href que continguin extensions d'imatge
        $patro = '/<a href="([^"]+\.(jpg|gif|png|jpeg))"/i';

        // Amb la funció preg_match_all el que fem és: amb el patró que hem guardat a la variable "$patro", busquem a la variable "$content" totes les
        // etiquetes que tinguin el mateix format del "$patro" a la nostra url i ho guardem a l'array "$coincidencies"
        preg_match_all($patro, $content, $coincidencies);

        // $coincidencies[0] conté totes les coincidències completes
        // $coincidencies[1] conté els noms dels fitxers (primer grup de captura)
        // $coincidencies[2] conté les extensions (segon grup de captura)

        
        // Mostrem tots els noms de fitxer. En aquest cas, creem la variable "$imatges" com una array, en aquest cas amb la funcio "explode()" separem cada part
        //de la variable $fitxer a partir del caracter '/' i ho guardem a l'array "$parts" i després amb la funcio "implode()" agafarem el tros que ens interessa
        //del array "$parts" a partir del caracter '/' i ho guardarem finalment a l'array "$imatges" que hem creat al principi.
        $imatges = array();
        foreach ($coincidencies[1] as $fitxer) {
            $parts=explode('/', $fitxer);
            $nomFitxer=implode('/', array_slice($parts,3));
            $imatges[]=$nomFitxer;
        }

        echo "<b>Mostra Imatges externes</b>"."<br>";
        echo "<table border='1'>";
            for ($i=0; $i<count($imatges); $i+=2){ //array per les files. En aquest cas es fa "$i+=2" perque la imatge de la casella de la que seria la 2na columna no es repeteixi a la següent fila
                echo "<tr>";
                    for($j=0; $j<2; $j++){ //array per les columnes
                        $index=$i+$j;
                        if ($index<count($imatges)){
                            echo "<td><b>".$imatges[$index]."</b><br>";
                            echo "<img src='".$url.$imatges[$index]."' width='auto'></td>";
                        }
                    }
                echo "</tr>";
            }
        echo "</table>";

    ?>
</body>
</html>