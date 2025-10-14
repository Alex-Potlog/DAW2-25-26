<!DOCTYPE html>
<html>

<?php
#Defineix una variable amb el preu d'un article i una constant 
#amb el valor de l'IVA vigent. Calcular i mostrar el preu final de l'article en aplicar l'IVA. Arrodonir als cèntims d'euro.

$preu = readline("Introdueix el preu del producte: ");
const IVA = 0.21;
$preu_final = $preu + ($preu * IVA);
echo "El preu final amb IVA és: " . number_format($preu_final, 2) . " euros.\n";

#Escriu un script que demani al sistema la data i hora i que mostri pel navegador
# l'estació de l'any, el mes de l'any, el dia de la setmana i que doni  "bon dia", "bona tarda" o "bona nit" segons l'hora.

$mes = date("m");
$hora = date("H");
$dia = date("d");

if ($hora > 12 && $hora < 20) {
    print "bona tarda";
} elseif ($hora < 12) {
    print "bon dia";
} else {
    print "bona nit";
}

#calcul estacio
if ($mes <= 4 && $mes > 0) {
    print("Estem a l'hivern");
} elseif ($mes <= 6) {
    print("estem a la primavera");
} elseif ($mes <= 9) {
    print("estem a l'estiu");
} else {
    print("estem a la tardor");
}

// Calcul mes
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
        $nom_mes = "No sé pas en quin mes visc";
}
//Calcul dia setmana
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
        $nom_dia = "No sé pas quin dia visc";
}


#tercer ex:
#Mostra una contrasenya aleatòria de 8 caràcters de longitud. Els caràcters vàlids són "abcdefghijklmnopqrstuvwxyz0123456789 # $% & @". 

$caractersValids = "abcdefghijklmnopqrstuvwxyz0123456789#$%&@";
$longitud = 8;
$contrasenya = "";
for ($i = 0; $i < $longitud; $i++) {
    $index = rand(0, strlen($caractersValids) - 1); #random entre 0 i la ultima posició del string
    $contrasenya .= $caractersValids[$index]; #.= es append(+=)
};
echo "La contrasenya aleatòria generada és: " . $contrasenya . "<br>";
echo "<br>";


/*
4-. Escriu un script que generi un enter de 8 dígits, calculi la lletra que li correspon de DNI 
i mostri pel navegador el resultat de manera llegible.
*/

$numDni = rand(10000000, 99999999);
$lletres_dni = "TRWAGMYFPDXBNJZSQVHLCKE";

$lletres_dni =  substr($lletres_dni, $numDni % 23, 1);

echo ("El teu dni es:" . $numDni . $lletres_dni . "<br>");



/*
Implementa un script per a generar els dorsals dels corredors d'una cursa. 
El format del dorsal és: H, D o X en funció del gènere + les tres primeres lletres del nom (la 1a en majúscula) 
+ les tres primeres lletres del primer cognom (la 1a en majúscula). 
Inicialitza variables amb els valors que vulguis i mostra pel navegador de el dorsal resultant.
*/

$genere = "h";
$nom = "Roger";
$cognom = "Muntane";

$dorsal = substr((strtoupper($genere)), 0, 1) . substr((strtoupper($nom)), 0, 3) . substr((strtoupper($cognom)), 0, 3);
echo ("El teu dorsal es:" . $dorsal . "<br>");


?>




</html>