<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Formularis</title>
</head>

<body>
    <form action="<?php echo $_SERVER["PHP_SELF"]; ?>" method="get">
        <label for="name">Nom:</label>
        <input type="text" name="nombre" id="name" required>

        <label for="day">Dia:</label>
        <select name="dia" id="day">
            <?php
            for ($i = 1; $i <= 31; $i++) {
                echo "<option value='$i'>$i</option>";
            }
            ?>
        </select>

        <label for="month">Mes:</label>
        <select name="mes" id="month">
            <?php
            $mesos = [
                1 => "Gener",
                2 => "Febrer",
                3 => "Març",
                4 => "Abril",
                5 => "Maig",
                6 => "Juny",
                7 => "Juliol",
                8 => "Agost",
                9 => "Setembre",
                10 => "Octubre",
                11 => "Novembre",
                12 => "Desembre"
            ];
            foreach ($mesos as $num => $nom) {
                echo "<option value='$num'>$nom</option>";
            }
            ?>
        </select>

        <label for="year">Any:</label>
        <select name="any" id="year">
            <?php
            for ($i = 1990; $i <= 2020; $i++) {
                echo "<option value='$i'>$i</option>";
            }
            ?>
        </select>

        <input type="submit" value="Dale para que aparezca la magia">
    </form>

    <?php
    if ($_SERVER["REQUEST_METHOD"] == "GET" && isset($_GET["nombre"]) && isset($_GET["dia"]) && isset($_GET["mes"]) && isset($_GET["any"])) {
        $nombre = htmlspecialchars($_GET["nombre"]);
        $dia = (int)$_GET["dia"];
        $mes = (int)$_GET["mes"];
        $any = (int)$_GET["any"];

        // Calcular l'edat
        $dataNaixement = new DateTime("$any-$mes-$dia");
        $dataActual = new DateTime();
        $edat = $dataActual->diff($dataNaixement)->y;

        echo "<p>Ets $nombre i tens $edat anys.</p>";
    }
    ?>
</body>

</html>