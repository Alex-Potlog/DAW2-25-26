<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <?php
// 1. Mostra per pantalla una matriu d'asteriscs "*". La quantitat de files i de columnes es calcula aleatòriament.

$numCol=rand(1,10);
$numFil=rand(1,10);


echo "<b>Exercici 1</b>"."<br>";
    echo "<table style='text-align: center;'>";

    for ($i=1; $i<=$numFil; $i++){
        echo "<tr>";
        for ($j=1; $j<=$numCol; $j++){
            $num = ($i - 1) * 10 + $j;
            echo "<td>*</td>";
        }
        echo "</tr>";
    }
    echo "</table>";
echo "/-----------------------------------------------------------------------------------/<br>";

// 2. Mostra per pantalla la taula de multiplicar del nombre 5.
echo "<b>Exercici 2</b>"."<br>";
$num5=5;

for ($i=1; $i<=10; $i++){
    $mult=$num5*$i;
    echo $num5 ." x ".$i." = ".$mult."<br>";
}
echo "/-----------------------------------------------------------------------------------/<br>";

// 3. Programa que calculi un nombre aleatori entre 0 i 50. Quan el nombre sigui inferior a 25, que mostri el missatge "El nombre $x és inferior a 25".Quan el nombre sigui superior a 25, que mostri el missatge "El nombre $x és superior a 25". Quan el nombre sigui igual a 25, acaba el programa.
echo "<b>Exercici 3</b>"."<br>";
$numAleatori=rand(0, 50);

if ($numAleatori<25){
    echo "El nombre ".$numAleatori." és inferior a 25";
} elseif ($numAleatori>25){
    echo "El nombre ".$numAleatori." és superior a 25";
}else{
    echo "FI";
}
echo "<br>/-----------------------------------------------------------------------------------/<br>";

// 4. Programa que mostri per pantalla les lletres d'una paraula emmagatzemada en una variable al dret i al revés.
echo "<b>Exercici 4</b>"."<br>";
$paraula="Cascabell";

$long=strlen($paraula);

$parReves="";
for ($i=$long-1; $i>=0; $i--){
    $parReves.=$paraula[$i];
}

echo $paraula."<br>";
echo $parReves;
    ?>
</body>
</html>
