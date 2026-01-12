<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Recepció de dades amb cookies</title>
</head>
<body>
    <?php

        if ($_SERVER["REQUEST_METHOD"] == "POST" && isset($_POST['Enviar'])) {
            $nom=trim($_POST['nomusu']);
            if (!empty($nom)){
                setcookie('nomusu', $nom, time() + 3600); // Caduca en 1 hora
                //redirigir
                header('Location: ' . $_SERVER['PHP_SELF']);
                exit();
            }
        }

        if ($_SERVER["REQUEST_METHOD"] == "POST" && isset($_POST['Elimina cookie'])) {
            setcookie('nomusu','', time()-3600, '/');
            unset($_COOKIE['nomusu']);

            //redirigir
            header('Location: ' . $_SERVER['PHP_SELF']);
            exit();
        }

        $nomGuardat=isset($_COOKIE['nomusu']) ? htmlspecialchars($_COOKIE['nomusu']) : null;
    ?>

</body>
</html>