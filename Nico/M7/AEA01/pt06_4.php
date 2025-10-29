<?php
session_start();

// Si venen per l'enllaç d'esborrar (GET) eliminem la sessió i les dades
if (isset($_GET['erase'])) {
    // Neteja les dades de sessió
    $_SESSION = [];

    // Esborra la cookie de sessió si existeix
    if (ini_get("session.use_cookies")) {
        $params = session_get_cookie_params();
        setcookie(
            session_name(),
            '',
            time() - 42000,
            $params["path"],
            $params["domain"],
            $params["secure"],
            $params["httponly"]
        );
    }

    // Destrueix la sessió
    session_destroy();

    // Redirigeix per evitar reanviar la petició
    header("Location: pt06_4.php");
    exit();
}

// Gestiona visites i última visita dins la sessió
if (!isset($_SESSION['visites'])) {
    $_SESSION['visites'] = 1;
} else {
    $_SESSION['visites']++;
}

// Guarda la data actual com a última visita després d'obtenir la anterior
$ultima_visita = isset($_SESSION['ultima_visita']) ? $_SESSION['ultima_visita'] : null;
$_SESSION['ultima_visita'] = date("d/m/Y H:i:s");

?>
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <title>Visites (sessions)</title>
</head>

<body>
    <h1>Visites a la pàgina (sessions)</h1>

    <p>Data actual: <?php echo htmlspecialchars(date("d/m/Y H:i:s")); ?></p>
    <p>Últim accés: <?php echo $ultima_visita ? htmlspecialchars($ultima_visita) : "És la teva primera visita"; ?></p>
    <p>Nombre de visites: <?php echo (int)$_SESSION['visites']; ?></p>

    <a href="pt06_4.php">Actualitzar</a><br>
    <a href="pt06_4.php?erase=1">Eliminar dades de sessió</a>
</body>

</html>