<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
    <form action="<?php echo $_SERVER["PHP_SELF"]; ?>" method="GET">
        Name: <input type="text" name="nom"><br>
        Data Naixement: <input type="date" name="data" min="1990-01-01" max="2020-01-01"><br>
        <input type="submit">
    </form>

    Ets el <?php echo $_GET["nom"]; ?> i tens <?php echo $edad; ?> anys

    <?php
    /*
    Implementa en un únic fitxer (exercici1) un formulari que demani a l'usuari el seu nom i la seva data de naixement. Utilitza action="<?php echo $_SERVER["PHP_SELF"];?>"
Per introduir la data de naixement, utilitza un menú de selecció generant els nombres de dia, mes i any (des de 1990 fins 2020) mitjançant php.
Fes-lo amb el mètode GET.
Processar el formulari serà calcular l'edat del usuari i mostrar-li d'aquesta manera: " Ets la Laia i tens 25 anys"
    */

    // $name = "";
    // $data = "";
    // $data_actual = date("Y/m/d");
    // $any_act = substr(string: $data_actual, offset: 0, length: 4);
    // $mes_act = substr(string: $data_actual, offset: 0, length: 4);
    // $dia_act = substr(string: $data_actual, offset: 0, length: 4);



    // if ($_SERVER["REQUEST_METHOD"] == "GET") {
    //     $name = test_input($_GET["nom"]);
    //     $data = test_input($_GET["data"]);
    // }

    // function edat($data)
    // {
    //     $any = (int) substr(string: $data, offset: 0, length: 4);
    //     $mes = (int) substr(string: $data, offset: 6, length: 8);
    //     $dia = (int) substr(string: $data, offset: 9, length: 11);
    // }

    $resultat = $any_act - $any;

    $date = new DateTime($_GET["data"]);
    $dateact = new DateTime();
    $diferencia = $date->diff($dateact);
    $edad = $diferencia->y;

    echo "Ets" . $_GET["nom"] . "Tens" . $edad;

    ?>
</body>

</html>