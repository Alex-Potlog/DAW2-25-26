<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cookie 1</title>
</head>
<body>

<?php
echo "Definir diverses cookies i mostrar-les per pantalla.<br><br>";
setcookie("cookies[cookie1]", "Sóc la cookie 1", time() + 3600); // Caduca en 1 hora
setcookie("cookies[cookie2]", "Sóc la cookie 2", time() + 3600); // Caduca en 2 hores       
setcookie("cookies[cookie3]", "Sóc la cookie 2", time() + 3600); // Caduca en 2 hores    

if(isset($_COOKIE["cookies"])) {
    foreach($_COOKIE["cookies"] as $name => $value) {
        echo "Cookie: " . $name . " - Valor: " . $value . "<br>";
    }
} else {
    echo "No hi ha cookies definides encara.<br>";
}

print_r($_COOKIE);;
echo "<br>";
?>

</body>
</html>

