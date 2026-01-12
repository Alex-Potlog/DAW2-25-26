<?php

// Comprovació de sessió 
if (isset($_POST)) {
    print_r($_POST);
}

// Comprovació del formulari de login


// Verificar el login


// Login correcte. 
// Ha de terminar redirigint a inici.php per assegurar que la cookie es llegeix immediatament
// header('Location: inici.php'); exit;


// Login incorrecte. Mostrar missatge d'error

?>

<!DOCTYPE html>
<html lang="ca">

<head>
    <meta charset="UTF-8">
    <title>Inici de Sessió / Àrea Privada</title>
    <style>
        body {
            font-family: Arial, sans-serif;
        }

        .contingut {
            width: 400px;
            margin: 50px auto;
            padding: 20px;
            border: 1px solid #ccc;
        }
    </style>
</head>

<body>
    <div class="contingut">
        <?php // if(): ? /*Comprovació sessió iniciada*/ 
        ?>
        <h1> Benvingut/da, <?/* mostrar nom d'usuari*/ ?>!</h1>
        <p>Has iniciat la sessió correctament. Aquesta és la teva àrea privada.</p>

        <p><a href="tanca_sessio.php">Tancar Sessió</a> </p>
        <hr>
        <p><a href="registre.php">Anar al Registre</a></p>
        <?php // else: ? > /* Pintar formulari */
        ?>
        <h1>Inici de Sessió</h1>

        <?php // /* Mostrar missatge*/
        ?>

        <form method="POST" action="<?php /*Redirigeix sobre si mateix*/ ?>">
            <label for="usuari">Nom d'Usuari:</label><br>
            <input type="text" id="usuari" name="usuari" required><br><br>

            <label for="contrasenya">Contrasenya:</label><br>
            <input type="password" id="contrasenya" name="contrasenya" required><br><br>

            <button type="submit">Iniciar Sessió</button>
        </form>

        <p>Encara no tens un compte? <a href="registre.php">Registra't</a></p>
        <?php //Esto no se me da bien /* Fi condició*/ 
        ?>
    </div>
</body>

</html>