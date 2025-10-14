<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Calculadora</title>
</head>

<body>
    <?php
    /*Implementa amb funcions, un script que simuli una calculadora
El cos principal calcularà un enter aleatori entre 1 i 5.
Segons el número es cridarà a la funció corresponent per realitzar les operacions (1->suma, 2->resta, 3->producte, 4->divisió i 5->arrel quadrada)
Dins de cada funció es calcularan aleatòriament els operands de l'operació.
La funció farà el càlcul corresponent i tornarà el resultat al cos principal. En el cas de la divisió també el residu.
El cos principal mostrarà al navegador tota la informació de l'operació realitzada.*/
    $operator = rand(1, 5);
    $a = rand(1, 100);
    $b = rand(1, 100);

    function suma($a, $b)
    {
        return $a + $b;
    }
    function resta($a, $b)
    {
        return $a - $b;
    }
    function mult($a, $b)
    {
        return $a * $b;
    }
    function div($a, $b)
    {
        $quo = $a / $b;
        $rest = $a % $b;
        return array($quo, $rest);
    }
    function arrel($a)
    {
        return sqrt($a);
    }


    switch ($operator) {
        case 1:
            echo "Suma de $a y $b";
            echo "<br>";
            echo suma($a, $b);
            break;
        case 2:
            echo "Resta de $a y $b";
            echo "<br>";
            echo resta($a, $b);
            break;
        case 3:
            echo "Producte de $a y $b";
            echo "<br>";
            echo mult($a, $b);
            break;
        case 4:
            echo "Divisio de $a y $b";
            echo "<br>";
            echo "0 es el resultat, 1 es la resta";
            echo "<br>";
            print_r(div($a, $b));
            break;
        case 5:
            echo "Arrel quadrada de $a";
            echo "<br>";
            echo arrel($a);
            break;
        default:
            echo "No has seleccionat una opció valida";
            echo "<br>";
    }




    ?>

</body>

</html>