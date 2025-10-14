<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Exercici 1.X</title>
</head>

<body>
    <?php


    /* Defineix una variable amb el preu d'un article i una constant almb el valor de l'IVA vigent. Calcular i mostrar el preu final
    de l'article en aplicar l'IVA. Arrodonir als cèntims d'euro. */
    echo "EXERCICI 1" . "<br>";
    $preu = 19.95; //Variable
    define("IVA", 0.21); //Constant
    $preuTotal = round($preu + ($preu * IVA), 2);
    echo $preuTotal;

    echo "<br>";





    /* Escriu un script que demani al sistema la data i hora i que mostri pel navegador l'estació de l'any, el mes de l'any, el dia de la setmana
i que doni  "bon dia", "bona tarda" o "bona nit" segons l'hora. */
    echo "EXERCICI 2" . "<br>";
    date_default_timezone_set("Europe/Madrid"); //Establece zona horaria por si acaso
    $dia = date("d");
    $mes = date("m");
    $any = date("Y");

    $estacio = ""; //localitzar variable
    if ($mes == 12 || $mes == 1 || $mes == 2) {
        $estacio = "Hivern";
    } elseif ($mes >= 3 && $mes <= 5) {
        $estacio = "Primavera";
    } elseif ($mes >= 6 && $mes <= 8) {
        $estacio = "Estiu";
    } else {
        $estacio = "Tardor";
    }

    // Càlcul mes
    switch ($mes) {
        case 1:
            $nom_mes = "Gener";
            break;
        case 2:
            $nom_mes = "Febrer";
            break;
        case 3:
            $nom_mes = "Març";
            break;
        case 4:
            $nom_mes = "Abril";
            break;
        case 5:
            $nom_mes = "Maig";
            break;
        case 6:
            $nom_mes = "Juny";
            break;
        case 7:
            $nom_mes = "Juliol";
            break;
        case 8:
            $nom_mes = "Agost";
            break;
        case 9:
            $nom_mes = "Setembre";
            break;
        case 10:
            $nom_mes = "Octubre";
            break;
        case 11:
            $nom_mes = "Novembre";
            break;
        case 12:
            $nom_mes = "Desembre";
            break;
        default:
            $nom_mes = "Si te sale esto, es que vives en otro universo";
    }
    //Càlcul nom de la setmana
    switch ($dia_set) {
        case 1:
            $nom_dia = "Dilluns";
            break;
        case 2:
            $nom_dia = "Dimarts";
            break;
        case 3:
            $nom_dia = "Dimecres";
            break;
        case 4:
            $nom_dia = "Dijous";
            break;
        case 5:
            $nom_dia = "Divendres";
            break;
        case 6:
            $nom_dia = "Dissabte";
            break;
        case 7:
            $nom_dia = "Diumenge";
            break;
        default:
            $nom_dia = "Si te sale esto, es que vives en otro planeta";
    }
    //Càlcul moment del dia
    if ($hora >= 6 && $hora < 14) {
        $moment_dia = "Bon dia";
    } elseif ($hora >= 14 && $hora < 22) {
        $moment_dia = "Bona tarda";
    } else {
        $moment_dia = "Bona nit";
    }
    echo strtoupper($moment_dia) . " !!!!!! " . "Per si ningú t'ho ha dit: " . "<br>"; //String TO UPPER
    echo "L'estació de l'any és: " . $estacio . "<br>";
    echo "El mes de l'any és: " . $nom_mes . "<br>";
    echo "I el dia de la setmana és: " . $nom_dia . "<br>";
    echo "<br>";




    /* Mostra una contrasenya aleatòria de 8 caràcters de longitud. Els caràcters vàlids són "abcdefghijklmnopqrstuvwxyz0123456789 # $% & @".  */
    echo "EXERCICI 3" . "<br>";
    $cars_valids = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789#$%&@";

    $contrasenya = ""; //Inicia variable
    for ($i = 0; $i < 8/*Longitud*/; $i++) {
        $index = rand(0, strlen($cars_valids) - 1); //Elije un numero del 0 al longitud de los caracteres validos
        $contrasenya .= $cars_valids[$index]; //el operador .= es Append
    }
    echo "La contrasenya aleatòria generada és: " . $contrasenya . "<br>";
    echo "<br>";

    /* Escriu un script que generi un enter de 8 dígits, calculi la lletra que li correspon de DNI i mostri pel navegador el resultat de manera llegible. */
    echo "EXERCICI 4" . "<br>";
    $numero_dni = rand(10000000, 99999999);
    $lletres_dni = "TRWAGMYFPDXBNJZSQVHLCKE";
    $lletra_dni = substr($lletres_dni, $numero_dni % 23, 1);
    echo "El número de DNI generat és: " . $numero_dni . $lletra_dni . "<br>";
    echo "<br>";
    /* Implementa un script per a generar els dorsals dels corredors d'una cursa. El format del dorsal és: H, D o X en funció del gènere + les tres
primeres lletres del nom (la 1a en majúscula) + les tres primeres lletres del primer cognom (la 1a en majúscula). Inicialitza variables amb els valors
que vulguis i mostra pel navegador de el dorsal resultant. */
    echo "EXERCICI 5" . "<br>";
    $genere = "H"; // H, D o X
    $nom = "Nicolas";
    $cognom1 = "Miszczak";
    $cognom2 = ""; // No s'utilitza en el dorsal
    $dorsal = $genere . strtoupper(substr($nom, 0, 1)) . strtolower(substr($nom, 1, 2))
        . strtoupper(substr($cognom1, 0, 1)) . strtolower(substr($cognom1, 1, 2));
    echo "El dorsal generat és: " . $dorsal . "<br>";
    echo "<br>";
    ?>
</body>

</html>