<!DOCTYPE html>

<head>
    <html lang="es">
</head>
<html>

<body>

    <?php
    //1. Defineix una variable amb el preu d'un article i una constant almb el valor de l'IVA vigent. Calcular i mostrar el preu final de l'article en aplicar l'IVA. Arrodonir als cèntims d'euro.
    

    define("IVA", 21);
    $preu = 10;
    echo 'Preu mes IVA: ' . ((IVA / 100) * $preu + $preu) . "<br>";
    ?>

    <?php
    //2. Escriu un script que demani al sistema la data i hora i que mostri pel navegador l'estació de l'any, el mes de l'any, el dia de la setmana i que doni  "bon dia", "bona tarda" o "bona nit" segons l'hora.
    $data = new DateTime();
    #echo 'Data actual: ' . $data->format('d-m-Y H:i:s');
    echo 'Estacio actual: ';
    $mes = $data->format('m');
    if ($mes >= 3 && $mes <= 5) {
        echo 'primavera';
    } elseif ($mes >= 6 && $mes <= 8) {
        echo 'verano';
    } elseif ($mes >= 9 && $mes <= 11) {
        echo 'otoño';
    } else {
        echo 'invierno';
    }
    '<br>Mes: ' . $data->format('F');
    '<br>Dia: ' . $data->format('l');
    if ($hora >= 6 && $hora < 12) {
        echo '<br>Bon dia';       // Mañana
    } elseif ($hora >= 12 && $hora < 20) {
        echo '<br>Bona tarda';    // Tarde
    } else {
        echo '<br>Bona nit';      // Noche
    }
    ?>

    <?php
    #3. Mostra una contrasenya aleatòria de 8 caràcters de longitud. Els caràcters vàlids són "abcdefghijklmnopqrstuvwxyz0123456789#$%&@". 
    $caracteres = "abcdefghijklmnopqrstuvwxyz0123456789#$%&@";
    $contrasenya = '';
    for ($i = 0; $i < 8; $i++) {
        $contrasenya .= $caracteres[rand(0, max: strlen($caracteres) - 1)];
    }

    echo '<br>Nova Contrasenya: ' . $contrasenya;
    ?>

    <?php
    #4. Escriu un script que generi un enter de 8 dígits, calculi la lletra que li correspon de DNI i mostri pel navegador el resultat de manera llegible.
    $dniNum = rand(10000000, 99999999);
    define("SECUENCIA", "TRWAGMYFPDXBNJZSQVHLCKE");
    $dni = $dniNum . SECUENCIA[$dniNum % 23];

    echo '<br>Nou DNI: ' . $dni;
    ?>

    <?php
    #5. Implementa un script per a generar els dorsals dels corredors d'una cursa. El format del dorsal és: H, D o X en funció del gènere + les tres primeres lletres del nom (la 1ra en majúscula) + les tres primeres lletres del primer cognom (la 1a en majúscula). Inicialitza variables amb els valors que vulguis i mostra pel navegador de el dorsal resultant.
    $genero = "H";
    $nom = "Jan";
    $apellido = "Lopez";

    $dorsal = '';
    $dorsal .= $genero;
    $dorsal .= ucfirst(substr($nom, 0, 3));
    $dorsal .= ucfirst(substr($apellido, 0, 3));
    echo '<br>Dorsal: ' . $dorsal;
    ?>
</body>

</html>