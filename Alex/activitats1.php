<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
    <?php
    # Primer exercici
    echo "Primer exercici <br><br>";
    $preu = 10;
    define("IVA", 21);
    $total = $preu + ($preu * IVA) / 100;
    echo $total . "<br>";

    # Segon exercici
    echo "<br>Segon exercici <br><br>";

    $mes = date("m");
    $hora = date("H");
    $dia = date("l");
    $diaAny = date("d");

    echo "Mes actual: " . $mes . "<br>";
    echo "Dia actual: " . $dia . "<br>";

    if (($mes <= 3 && $diaAny <= 20) || ($mes == 12 && $diaAny > 20)) {
        echo "Hivern <br>";
    } elseif ($mes == 4 || $mes == 5 || ($mes == 3 && $diaAny > 20) || ($mes == 6 && $diaAny <= 20)) {
        echo "Primavera <br>";
    } elseif ($mes == 7 || $mes == 8 || ($mes == 6 && $diaAny > 20) || ($mes == 9 && $diaAny <= 20)) {
        echo "Estiu <br>";
    } else {
        echo "Tardor <br>";
    }

    if ($hora < 16 && $hora > 6) {
        echo "Bon dia <br>";
    } elseif ($hora >= 16 && $hora < 21) {
        echo "Bona tarda <br>";
    } else {
        echo "Bona nit <br>";
    }

    # Tercer exercici
    echo "<br>Tercer exercici<br><br>";
    $carsValids = "abcdefghijklmnopqrstuvwxyz0123456789#$%&@QWERTYUIOPASDFGHJKLÑZXCVBNM";
    $contra = "";
    for ($i = 0; $i < 8; $i++) {
        $contra .= $carsValids[(rand(0, strlen($carsValids) - 1))];
    }
    echo $contra . "<br>";

    # Quart exercici
    echo "<br>Quart exercici<br><br>";
    define("DNI", "TRWAGMYFPDXBNJZSQVHLCKE");
    $dni = "";
    $numDni = rand(1000000, 9999999);
    $lletraDni = substr(DNI, $numDni % 23, 1);
    $dni = "$numDni$lletraDni";
    echo "$dni<br>";

    # Cinquè exercici
    echo "<br>Cinquè exercici<br><br>";

    ?>

</body>

</html>