<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>



    <?php
    /*
    1. Calcula tres nombres aleatoris i, utilitzant l'operador condicional "? :", mostri per pantalla quins és el nombre
    major i quin és el nombre menor.
    2. Inicialitza un array associatiu que tingui com a clau el nom del país i com a valor el nombre d'habitants. Mostra
    en el navegador les dades de manera llegible
    3. Inicialitza un array associatiu amb quatre registres de participants en una carrera. Genera els dorsals dels
    corredors i emmagatzema'ls en l'última casella de l'array. El format del dorsal és: H, D o X en funció del gènere +
    les tres primeres lletres del nom (la 1a en majúscula) + les tres primeres lletres del primer cognom (la 1a en
    majúscula). Mostra pel navegador l'array sencer de manera legible.
    */

    # Exercici 1
    echo "Exercici 1<br><br>";

    $nums = [];
    $nums[0] = rand(0, 99);
    $nums[1] = rand(0, 99);
    $nums[2] = rand(0, 99);

    $max = $nums[0] > $nums[1] ? ($nums[0] > $nums[2] ? $nums[0] : $nums[2]) : ($nums[1] > $nums[2] ? $nums[1] : $nums[2]);
    $min = $nums[0] < $nums[1] ? ($nums[0] < $nums[2] ? $nums[0] : $nums[2]) : ($nums[1] < $nums[2] ? $nums[1] : $nums[2]);

    echo "El més petit és " . $min . ". El més gran és " . $max . "<br>";

    # Exercici 2
    echo "<br>Exercici 2<br><br>";

    $array = array(
        "Espanya" => 47420000,
        "Regne Unit" => 68200000,
        "França" => 67390000,
        "Alemanya" => 83240000,
        "Itàlia" => 59110000,
        "Portugal" => 10310000,
        "Països Baixos" => 17480000,
        "Bèlgica" => 11590000,
        "Suïssa" => 8800000,
        "Suècia" => 10510000,
        "Noruega" => 5400000,
        "Dinamarca" => 5900000
    );

    foreach ($array as $key => $value) {
        echo $key . ": " . $value . "<br>";
    }

    # Exercici 3
    echo "<br>Exercici 3<br><br>                                          ";

    $array = [
        ["Dorsal" => "H", "Nom" => "Pep", "Cognom" => "Gal"],
        ["Dorsal" => "D", "Nom" => "Pep", "Cognom" => "Gal"],
        ["Dorsal" => "X", "Nom" => "Pep", "Cognom" => "Gal"]
    ];

    for ($i = 0; $i < count($array); $i++) {
        foreach ($array[$i] as $key => $value)
            echo $key . ": " . $value . "<br>";
        echo '-------------------------------------<br> ';
    }

    # Exercici 4
    echo "EXERCICI 4" . "<br>";
    echo "<table border='1' style='text-align: center;'>";

    for ($i = 1; $i <= 10; $i++) {
        echo "<tr>";
        for ($j = 1; $j <= 10; $j++) {
            $num = $i * $j;
            echo "<td>$num</td>";
        }
        echo "</tr>";
    }
    echo "</table>";
    echo "<br>";
    ?>
</body>