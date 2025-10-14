<!DOCTYPE html>
<html>

<?php
# ex1: Calcula tres nombres aleatoris i, utilitzant
# l'operador condicional "? :", mostri per pantalla quins és el nombre major i quin és el nombre menor.

$num = rand(1, 1000);
$num2 = rand(1, 1000);

$numeroMajor = $num > $num2 ? "El numero major és: $num" : "El numero major és: $num2";

echo ($numeroMajor . "\n");


#Ex2 Inicialitza un array associatiu que tingui com a clau el nom del país i com a valor 
#el nombre d'habitants. Mostra en el navegador les dades de manera llegible

$pais = array("Espanya" => 50, "França" => 30, "Italia" => 40);

echo "El nombre d'habitants a Espanya es de" . $pais["Espanya"] . "<br>";
echo "El nombre d'habitants a França es de" . $pais["França"] . "<br>";
echo "El nombre d'habitants a Italia es de" . $pais["Italia"] . "<br>";


#Ex3
#Inicialitza un array associatiu amb quatre registres de participants en una carrera. 
#Genera els dorsals dels corredors i emmagatzema'ls en l'última casella de l'array. 
#El format del dorsal és: H, D o X en funció del gènere + les tres primeres lletres del nom (la 1a en majúscula) + 
#les tres primeres lletres del primer cognom (la 1a en majúscula). Mostra pel navegador l'array sencer de manera legible.

$deportistes  = [
    ["genere" => "D", "nom" => "Roger", "cognom1" => "Munatne", "cognom2" => "Cuadra"],
    ["genere" => "D", "nom" => "Alex", "cognom1" => "Lopez", "cognom2" => "Perez"],
    ["genere" => "X", "nom" => "Xavier", "cognom1" => "Gómez", "cognom2" => "Sanchez"],
    ["genere" => "H", "nom" => "Pau", "cognom1" => "Barquero", "cognom2" => "Rovira"]
];

foreach ($deportistes as $index => $deportista) {
    $dorsal = $deportista['genere']
        . strtoupper(substr($deportista['nom'], 0, 1)) . strtolower(substr($deportista['nom'], 1, 2))
        . strtoupper(substr($deportista['cognom1'], 0, 1)) . strtolower(substr($deportista['cognom1'], 1, 2));
    $deportistes[$index]['dorsal'] = $dorsal; // Afegir dorsal a l'array
}


foreach ($deportistes as $deportista) {
    echo  $deportista['nom'] . " " . $deportista['cognom1'] . " amb dorsal " . $deportista['dorsal'] . "<br>";
}

#Ex4
#Implementa un script que mostri per pantalla una graella semblant a la següent:


echo "<table border='1' style='text-align: center;'>";

for ($i = 1; $i <= 10; $i++) { //
    echo "<tr>";
    for ($j = 1; $j <= 10; $j++) {
        $num = $i * $j;
        echo "<td>$num</td>"; //
    }
    echo "</tr>";
};
echo "</table>";
echo "<br>";



/*5-. Inicialitza un array amb 10 ciutats, crida a les diferents funcions d'ordenació que ofereix PHP (sort(), rsort(), asort(), 
arsort(), ksort(), krsort() i shuffle()) explicant com ordena i mostra el resultat pel navegador.*/
echo "EXERCICI 5" . "<br>";


$ciutats = array("Barcelona", "Madrid", "València", "Sevilla", "Zaragoza", "Màlaga", "Murcia", "Santiago", "Bilbao", "Alicante");
echo "ARRAY INICIAL:" . "<br>";
print_r($ciutats);
echo "<br> <br>";

// sort() - Ascendent 
sort($ciutats);
echo "sort() (ascendent):" . "<br>";
print_r($ciutats);
echo "<br> <br>";

// rsort() - Descendent
rsort($ciutats);
echo "rsort() (descendent):" . "<br>";
print_r($ciutats);
echo "<br> <br>";

//asort() - Ascendent per valor, mantenint la clau
asort($ciutats);
echo "asort() (ascendent per valor, mantenint la clau):" . "<br>";
print_r($ciutats);
echo "<br> <br>";

// arsort() - Descendent per valor, mantenint la clau
arsort($ciutats);
echo "arsort() (descendent per valor, mantenint la clau):" . "<br>";
print_r($ciutats);
echo "<br> <br>";

// ksort() - Ascendent per clau
ksort($ciutats);
echo "ksort() (ascendent per clau):" . "<br>";
print_r($ciutats);
echo "<br> <br>";

// krsort() - Descendent per clau
krsort($ciutats);
echo "krsort() (descendent per clau):" . "<br>";
print_r($ciutats);
echo "<br> <br>";

// shuffle() - Ordenació aleatòria
shuffle($ciutats);
echo "shuffle() (ordenació aleatòria):" . "<br>";
print_r($ciutats);
echo "<br> <br>";
?>





</html>