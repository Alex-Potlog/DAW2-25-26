<?php
if (isset($_GET['erase'])) {
    setcookie("visites", "", time() - 3600);
    setcookie("ultima-visita", "", time() - 3600);
    header("Location: pt06_3.php"); // Redirigeix després d'eliminar les cookies
    exit(); //sense aixo no funciona
}

$visites = 1;
if (isset($_COOKIE["visites"])) {
    $visites = $_COOKIE["visites"] + 1;
}
setcookie("visites", $visites, time() + 3600);
setcookie("ultima-visita", date("d/m/Y H:i:s"), time() + 3600);
?>
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Visites</title>
</head>

<body>
    <h1>Visites a la pàgina</h1>
    <p>Data actual: <?php echo date("d/m/Y H:i:s"); ?></p>
    <p>Últim accés: <?php echo isset($_COOKIE["ultima-visita"]) ? $_COOKIE["ultima-visita"] : "És la teva primera visita"; ?></p>
    <p>Nombre de visites: <?php echo $visites; ?></p>
    <a href="pt06_3.php">Actualitzar</a><br>
    <a href="pt06_3.php?erase=1">Eliminar cookie</a>

</body>

</html>