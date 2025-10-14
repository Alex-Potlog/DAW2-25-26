<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Exercici 2 - Arrays</title>
</head>

<body>
    <?php
    /*Calcula tres nombres aleatoris i, utilitzant l'operador condicional "? :", mostri per pantalla quins és el nombre major i quin és el nombre menor.
*/
    $x = rand(1, 100);
    $y = rand(1, 100);
    $z = rand(1, 100);

    $max = ($x > $y) ? ($x > $z ? $x : $z) : ($y > $z ? $y : $z);
    $min = ($x < $y) ? ($x < $z ? $x : $z) : ($y < $z ? $y : $z);

    echo "Nombres generats: $x, $y, $z<br>";
    echo "El nombre major és: $max<br>";
    echo "El nombre menor és: $min<br><br>";
    /*
Inicialitza un array associatiu que tingui com a clau el nom del país i com a valor el nombre d'habitants. Mostra en el navegador les dades de manera llegible*/
    $ass = array(
        "España" => 47351567,
        "Polonia" => 37950802,
        "Zimbabwe" => 14862924,
        "Herzegovina" => 3280819,
        "Andorra" => 77265,
        "Saotome i Príncipe" => 219159,
        "Antigua i Barbuda" => 97929,
        "Tuvalu" => 11792,
        "Vaticà" => 825
    );
    foreach ($ass as $pais => $habitants) {
        echo "$pais té $habitants habitants.<br>";
    }
    echo "<br>";

    /*
Inicialitza un array associatiu amb quatre registres de participants en una carrera. Genera els dorsals dels corredors i emmagatzema'ls en l'última casella de l'array. El format del dorsal és: H, D o X en funció del gènere + les tres primeres lletres del nom (la 1a en majúscula) + les tres primeres lletres del primer cognom (la 1a en majúscula). Mostra pel navegador l'array sencer de manera legible.
*/
    $participants = array(
        array("nom" => "Ana", "cognom" => "García", "genere" => "D"),
        array("nom" => "Luis", "cognom" => "Martínez", "genere" => "H"),
        array("nom" => "Marta", "cognom" => "López", "genere" => "D"),
        array("nom" => "Carlos", "cognom" => "Sánchez", "genere" => "H")
    );
    foreach ($participants as $index => $participant) {
        $dorsal = $participant['genere']
            . strtoupper(substr($participant['nom'], 0, 1)) . strtolower(substr($participant['nom'], 1, 2))
            . strtoupper(substr($participant['cognom'], 0, 1)) . strtolower(substr($participant['cognom'], 1, 2));
        $participants[$index]['dorsal'] = $dorsal;
    }

    var_dump($participants);
    echo "<br>";
    echo "<br>";
    echo "<br>";
    foreach ($participants as $participant) {
        echo $participant['nom'] . " " . $participant['cognom'] . ", Gènere: " . $participant['genere'] . " amb Dorsal: " . $participant['dorsal'] . "<br>";
    }
    echo "<br>";

    /*
Implementa un script que mostri per pantalla una graella semblant a la següent:*/

    echo "<table>";
    for ($i = 1; $i <= 10; $i++) {
        echo "<tr>";
        for ($j = 1; $j <= 10; $j++) {
            $producte = $i * $j;
            echo "<td>$producte</td>";
        }
        echo "</tr>";
    }

    echo "</table>";


    echo "<br>";

    echo "EXERCICI 4" . "<br>";
    echo "Sentencia for" . "<br>";

    echo "<table border='1' style='text-align: center;'>";

    for ($i = 1; $i <= 10; $i++) { //
        echo "<tr>";
        for ($j = 1; $j <= 10; $j++) {
            $num = ($i - 1) * 10 + $j;
            echo "<td>$num</td>"; //
        }
        echo "</tr>";
    }
    echo "</table>";
    echo "<br>";

    //Inicialitza un array amb 10 ciutats, crida a les diferents funcions d'ordenació que ofereix PHP (sort(), rsort(), asort(), arsort(), ksort(), krsort() i shuffle()) explicant com ordena i mostra el resultat pel navegador.

    $ciutats = array("Barcelona", "Madrid", "València", "Sevilla", "Zaragoza", "Màlaga", "Murcia", "Palma", "Bilbao", "Alicante");
    echo "Array original:<br>";
    var_dump($ciutats);
    echo "<br>";
    sort($ciutats);
    echo "Array ordenat amb sort(ascendent):<br>";
    var_dump($ciutats);
    echo "<br>";
    rsort($ciutats);
    echo "Array ordenat amb rsort(descendent):<br>";
    var_dump($ciutats);
    echo "<br>";
    asort($ciutats);
    echo "Array ordenat amb asort(ascendent per valor, mantenint la clau):<br>";
    var_dump($ciutats);
    echo "<br>";
    arsort($ciutats);
    echo "Array ordenat amb arsort(descendent per valor, mantenint la clau):<br>";
    var_dump($ciutats);
    echo "<br>";
    ksort($ciutats);
    echo "Array ordenat amb ksort(ascendent per clau):<br>";
    var_dump($ciutats);
    echo "<br>";
    krsort($ciutats);
    echo "Array ordenat amb krsort(descendent per clau):<br>";
    var_dump($ciutats);
    echo "<br>";
    shuffle($ciutats);
    echo "Array ordenat amb shuffle(random):<br>";
    var_dump($ciutats);
    echo "<br>";

    ?>
</body>

</html>