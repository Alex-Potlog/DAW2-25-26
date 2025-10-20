<!DOCTYPE html>
<html>

<?php
#Escriu un script que demani al sistema la data i hora i que mostri pel navegador
# l'estació de l'any, el mes de l'any, el dia de la setmana i que doni  "bon dia", "bona tarda" o "bona nit" segons l'hora.

$mes = date("m");
$hora = date("H");
$dia = date("d");
$diesSetmana = ["dilluns", "dimarts", "dimecres"];

if ($hora > 12 && $hora < 20) {
    print "bona tarda";
} elseif ($hora < 12) {
    print "bon dia";
} else {
    print "bona nit";
}


if ($mes <= 4 && $mes > 0) {
    print("Estem a l'hivern");
} elseif ($mes <= 6) {
    print("estem a la primavera");
} elseif ($mes <= 9) {
    print("estem a l'estiu");
} else {
    print("estem a la tardor");
}

print("el dia de la setmana es" . $diesSetmana[$dia]);



#tercer ex:
#Mostra una contrasenya aleatòria de 8 caràcters de longitud. Els caràcters vàlids són "abcdefghijklmnopqrstuvwxyz0123456789 # $% & @". 

$caractersValids = "abcdefghijklmnopqrstuvwxyz0123456789#$%&@";
$longitud = 8;
$contrasenya = "";
for ($i = 0; $i < $longitud; $i++) {
    $index = rand(0, strlen($caractersValids) - 1); #random entre 0 i la ultima posició del string
    $contrasenya .= $caractersValids[$index]; #.= es append
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