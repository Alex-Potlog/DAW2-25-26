<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cookie 1</title>
</head>
<body>

<?php

$value = "Bon dia";
setcookie("salutació", $value, time() + 3600); // Caduca en 1 hora
if(isset($_COOKIE["salutació"])) {
    echo "Cookie definida:    " . $_COOKIE["salutació"] . "<br>";
} else {
    echo "Cookie no definida encara.<br>";
}; 
echo "<br>";
print_r($_COOKIE);
echo "<br>";

//setcookie("salutació"); //Esborrar cookie
// print_r($_COOKIE);

?>

</body>
</html>


