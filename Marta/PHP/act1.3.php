<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Activitat 1.3</title>
</head>
<body>
    <?php

    /*1. Implementa amb funcions, un script que simuli una calculadora
        a) El cos principal calcularà un enter aleatori entre 1 i 5.
        b) Segons el número es cridarà a la funció corresponent per realitzar les operacions (1->suma, 2->resta, 3->producte, 4->divisió i 5->arrel quadrada)
        c) Dins de cada funció es calcularan aleatòriament els operands de l'operació.
        d) La funció farà el càlcul corresponent i tornarà el resultat al cos principal. En el cas de la divisió també el residu.
        e) El cos principal mostrarà al navegador tota la informació de l'operació realitzada*/
    echo "<b>La Calculadora</b><br>";
    
    $enter=rand(1, 5);

    echo "Número enter aleatòri: ".$enter."<br>";

    function suma() {
        $num1=rand(0, 99);
        $num2=rand(0, 99);

        $suma= $num1+$num2;
        echo "El resultat de sumar $num1 i el $num2 és: $suma <br>";
    }

    function resta() {
        $num1=rand(0, 99);
        $num2=rand(0, 99);

        $resta= $num1-$num2;
        echo "El resultat de restar $num1 i el $num2 és: $resta <br>";
    }

    function producte() {
        $num1=rand(0, 99);
        $num2=rand(0, 99);

        $producte= $num1*$num2;
        echo "El resultat de multiplicar $num1 i el $num2 és: $producte <br>";
    }

    function divisio () {
        $num1=rand(0, 99);
        $num2=rand(0, 99);

        $divisio= $num1/$num2;
        $residu=$num1%$num2;
        echo "El resultat de dividir $num1 i el $num2 és: $divisio i el residu és: $residu <br>";
    }

    function arrel() {
        $num1=rand(0, 99);

        $arrelQ= sqrt($num1);
        echo "L'arrel quadrada de $num1 és: $arrelQ <br>";
    }

    if ($enter===1){
        suma();
    } elseif ($enter===2){
        resta();
    } elseif ($enter===3){
        producte();
    } elseif ($enter===4){
        divisio();
    } else {
        arrel();
    }
    
    echo "-----------------------------------------------------------------------------------------------------<br>";
    /*Modifica el programa del punt 1 de manera que els operands de les operacions es calculin en el cos principal i es passin per paràmetre a les funcions corresponents.*/
    echo "<b>La Calculadora 2 </b><br>";
    
    $enter2=rand(1, 5);

    echo "Número enter aleatòri: ".$enter2."<br>";

    $numer1=rand(0, 99);
    $numer2=rand(0, 99);

    function suma2($a, $b) {
        $suma= $a+$b;
        echo "El resultat de sumar $a i el $b és: $suma <br>";
    }

    function resta2($a, $b) {
        $resta= $a-$b;
        echo "El resultat de restar $a i el $b és: $resta <br>";
    }

    function producte2($a, $b) {
        $producte= $a*$b;
        echo "El resultat de multiplicar $a i el $b és: $producte <br>";
    }

    function divisio2 ($a, $b) {
        $divisio= $a/$b;
        $residu=$a%$b;
        echo "El resultat de dividir $a i el $b és: $divisio i el residu és: $residu <br>";
    }

    function arrel2($a) {
        $arrelQ= sqrt($a);
        echo "L'arrel quadrada de $a és: $arrelQ <br>";
    }

    if ($enter2===1){
        echo suma2($numer1, $numer2);
    } elseif ($enter2===2){
        echo resta2($numer1, $numer2);
    } elseif ($enter2===3){
        echo producte2($numer1, $numer2);
    } elseif ($enter2===4){
        echo divisio2($numer1, $numer2);
    } else {
        echo arrel2($numer1);
    }

    ?>
</body>
</html>