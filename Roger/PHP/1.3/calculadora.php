<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
    <?php
    /*

    Implementa amb funcions, un script que simuli una calculadora
        El cos principal calcularà un enter aleatori entre 1 i 5.
        Segons el número es cridarà a la funció corresponent per realitzar les operacions (1->suma, 2->resta, 3->producte, 4->divisió i 5->arrel quadrada)
        Dins de cada funció es calcularan aleatòriament els operands de l'operació.
        La funció farà el càlcul corresponent i tornarà el resultat al cos principal. En el cas de la divisió també el residu.
        El cos principal mostrarà al navegador tota la informació de l'operació realitzada.
    Modifica el programa del punt 1 de manera que els operands de les operacions es calculin en el cos principal i es passin per paràmetre a les funcions corresponents. 

    */

    $numero = rand(1, 5);
    echo "El numero es: $numero <br>";

    function sum()
    {
        $numero1 = rand(0, 100);
        $numero2 = rand(0, 100);
        $resultat = $numero1 + $numero2;
        echo $resultat;
        return $resultat;
    }

    function resta()
    {
        $numero1 = rand(0, 100);
        $numero2 = rand(0, 100);
        $resultat = $numero1 - $numero2;
        return $resultat;
    }

    function multiplicacio()
    {
        $numero1 = rand(0, 100);
        $numero2 = rand(0, 100);
        $resultat = $numero1 * $numero2;
        echo $resultat;
        return $resultat;
    }

    function divisio()
    {
        $numero1 = rand(0, 100);
        $numero2 = rand(0, 100);
        $resultat = $numero1 / $numero2;
        $residu = $numero1 % $numero2;
        echo $resultat . "I el residu" . $residu;
        return $resultat;
    }

    function arrel()
    {
        $numero1 = rand(0, 100);
        $resultat = sqrt($numero1);
        echo $resultat;
        return $resultat;
    }

    switch ($numero) {
        case 1:
            sum();
            break;
        case 2:
            resta();
            break;
        case 3:
            multiplicacio();
            break;
        case 4:
            divisio();
            break;
        case 5:
            arrel();
            break;
    }


    ?>


</body>

</html>