<?php


// Comprovació si el formulari s'ha enviat
$valid = false;
if (isset($_POST)) {
    //print("Hay datos");
    //$valid = true;

    // Validació de camps buits i registre d'usuari
    //print_r($_POST);
    if ($_POST['usuari'] !== null && $_POST['contrasenya'] !== null) {
        $nomUser = $_POST['usuari'];
        $passUser = $_POST['contrasenya'];
        $valid = true;
        print($nomUser);
        print($passUser);
        //file_put_contents('./fitxers/usuaris.txt', $nomUser + ";" + $passUser + "\n", FILE_APPEND); //Me falla
    }
};
// Missatge d'èxit o error
/*
Esto me da demasiados errores
$missatge = "";
if ($valid == true) {
    $missatge = "L'usuari " + $nomUser + " s'ha registrat correctament";
} else {
    $missatge = "L'usuari no s'ha registrat, hi ha hagut un error";
}
     */
?>

<!DOCTYPE html>
<html lang="ca">

<head>
    <meta charset="UTF-8">
    <title>Registre de Nou Usuari</title>
    <style>
        body {
            font-family: Arial, sans-serif;
        }

        .contingut {
            width: 300px;
            margin: 50px auto;
            padding: 20px;
            border: 1px solid #ccc;
        }
    </style>
</head>

<body>
    <div class="contingut">
        <h1>Registre d'Usuaris</h1>

        <?php print($missatge); ?>

        <form method="POST" action="<?php echo htmlspecialchars($_SERVER['PHP_SELF']); ?>">
            <label for="usuari">Nom d'Usuari:</label><br>
            <input type="text" id="usuari" name="usuari" required><br><br>

            <label for="contrasenya">Contrasenya:</label><br>
            <input type="password" id="contrasenya" name="contrasenya" required><br><br>

            <button type="submit">Registrar</button>
        </form>

        <p>Ja tens un compte? <a href="inici.php">Inicia sessió</a></p>
    </div>
</body>

</html>