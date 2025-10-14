<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
    <form action="<?php echo $_SERVER['PHP_SELF']; ?>" method="get">

        Nom: <input type="text" placeholder="nom" name="nom">

        <select name="dia">
            <option value="">Selecciona un dia</option>
            <?php
            for ($i = 1; $i <= 31; $i++) {
                echo "<option value='$i'>$i</option>";
            }
            ?>
        </select>

        <select name="mes">
            <option value="0">Selecciona un mes</option>
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

            foreach ($mesos as $num => $nomMes) {
                echo "<option value='$num'>$nomMes</option>";
            }
            ?>
        </select>

        <select name="any">
            <option value="">Selecciona un any</option>
            <?php
            for ($i = 1990; $i <= 2025; $i++) {
                echo "<option value='$i'>$i</option>";
            }
            ?>
        </select>

        <br><br>
        <input type="submit" value="Enviar">
    </form>
    <form action="ACT1.4.1_Jan_lopez.php" method="post">
        <div class="row">
            <div class="w-100">
                <label for="model">Model:</label>
                <input type="text" id="model" name="model" placeholder="Model" required>
            </div>
            <div class="w-100">
                <label for="marca">Marca:</label>
                <input type="text" id="marca" name="marca" placeholder="Marca" required>
            </div>
            <div class="w-50">
                <label for="motor">Motor:</label>
                <input type="text" id="motor" name="motor" placeholder="Motor" required>
            </div>
            <div class="w-50">
                <label for="cilindrada">Cilindrada:</label>
                <input type="text" id="cilindrada" name="cilindrada" placeholder="Cilindrada" required>
            </div>
            <div class="w-100">
                <label>Energia:</label>
                <input type="radio" id="gasolina" name="energia" value="gasolina" required>
                <label for="gasolina">Gasolina</label>
                <input type="radio" id="diesel" name="energia" value="diesel">
                <label for="diesel">Diesel</label>
                <input type="radio" id="hibrid" name="energia" value="hibrid">
                <label for="hibrid">Diesel</label>
                <input type="radio" id="electric" name="energia" value="electric">
                <label for="electric">Diesel</label>
            </div>
            <div class="w-100">
                <button type="submit">Enviar</button>
            </div>
        </div>
    </form>


    <?php
    $nom = $_GET['nom'];
    $dia = $_GET['dia'];
    $mes = $_GET['mes'];
    $any = $_GET['any'];
    $data_naixement = new DateTime("$any-$mes-$dia");
    $data_avui = new DateTime();
    $edat = $data_avui->diff($data_naixement)->y;

    $data_naixement = new DateTime("$any-$mes-$dia");
    $data_avui = new DateTime();
    $edat = $data_avui->diff($data_naixement)->y;

    echo "<p>Ets la $nom i tens $edat anys.</p>";
    ?>


</body>

</html>