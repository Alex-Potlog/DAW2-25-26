<?php
if (isset($_GET['erase'])) {
    setcookie("nomus", "", time() - 3600);
} elseif (isset($_POST["nomusuari"])) {
    setcookie("nomus", $_POST["nomusuari"], 3600 + time());
}
?>
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>cookiePOST</title>
</head>

<body>
    <?php
    if (isset($_COOKIE["nomus"])) {
        echo "<h1>Benvingut/da " . $_COOKIE["nomus"] . "</h1>";
    } else {
        echo "<h1>Benvingut/da usuari desconegut</h1>";
    }
    echo "<br>Cookie: <br>" . $_COOKIE["nomus"];
    echo "<br>Post: <br>" . $_POST["nomusuari"];
    ?>
    <a href="pt06_1.php">Tornar</a>
</body>

</html>