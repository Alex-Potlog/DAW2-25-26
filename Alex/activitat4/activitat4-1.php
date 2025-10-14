<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Exercici 4</title>
</head>

<body>

    <form action="<?php echo $_SERVER["PHP_SELF"]; ?>" method="get">
        <input type="text" name="texto" placeholder="Entra el teu nom...">
        <input type="date" name="data" max="2020-12-31" min="1990-01-01">
        <input type="submit" value="Entra">
    </form>

    <?php
    if (!empty($_GET["data"]) && !empty($_GET["texto"])) {
        $data = $_GET["data"];
        $data = naixement($data);
        echo "Ets en/na " . $_GET["texto"] . " i tens " . $data;
    }
    function naixement($data): int
    {
        $any = (int) substr($data, 0, 4);
        $mes = (int) substr($data, 5, 2);
        $dia = (int) substr($data, 8, 2);
        $anyAra = (int) date("Y");
        $mesAra = (int) date("m");
        $diaAra = (int) date("d");
        $anyDiff = 0;

        if ($mes > $mesAra) {
            $anyDiff = $anyAra - $any;
        } elseif ($mes == $mesAra) {
            $anyDiff = ($dia > $diaAra) ? $anyAra - $any - 1 : $anyAra - $any;
        } else {
            $anyDiff = $anyAra - $any;
        }
        return $anyDiff;
    }
    ?>

</body>

</html>