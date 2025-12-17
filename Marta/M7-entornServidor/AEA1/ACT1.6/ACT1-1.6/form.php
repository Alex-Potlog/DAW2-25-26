<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Formulari amb Cookies</title>
</head>

<body>
    <form action='formCookie.php' method="post">
        <label for="nomusu"> Nom d'usuari</label>
        <input type="text" id="nomusu" name="nomusu" value="">
        <input type="submit" name="submit" value="Enviar"><br>
        <input type="submit" name="submit" value="Elimina cookie">
    </form>

    <?php if ($nomGuardat): ?>
        <div><p>Benvingut/a <?php echo $nomGuardat ?></p></div>
    <?php endif; ?>
</body>

</html>