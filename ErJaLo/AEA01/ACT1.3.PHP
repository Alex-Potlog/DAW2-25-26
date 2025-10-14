<!DOCTYPE html>
<html lang="es">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ACT1.3</title>
</head>

<body>
    Sense parametres
    <br>
    <?php
    $numero = rand(1, max: 5);
    switch ($numero) {
        case 1:
            echo 'Suma Numeros aleatoris: ' . suma();
            break;
        case 2:
            echo 'Resta Numeros aleatoris: ' . resta();
            break;
        case 3:
            echo 'Producte Numeros aleatoris: ' . producte();
            break;
        case 4:
            echo 'Divisio Numeros aleatoris: ' . divisio();
            break;
        case 5:
            echo 'Arrel Quadrada Numeros aleatoris: ' . arrelQuadrada();
            break;
        default:
            echo 'Error, el numero no esta asignat: ';
            break;
    }

    function suma()
    {
        return rand(1, 10) + rand(1, 10);
    }
    function resta()
    {
        return rand(1, 10) - rand(1, 10);
    }
    function producte()
    {
        return rand(1, 10) * rand(1, 10);
    }
    function divisio()
    {
        return rand(1, 10) / rand(1, 10);
    }
    function arrelQuadrada()
    {
        return sqrt(rand(25, 100));
    }

    ?>
    <br>
    Amb parametres:
    <br>
    <?php
    $numero = rand(1, max: 5);
    switch ($numero) {
        case 1:
            $x = rand(1, max: 5);
            $y = rand(1, max: 5);
            echo 'Suma Numeros aleatoris: ' . sumaAmbParametre($x, $y);
            break;
        case 2:
            $x = rand(1, max: 5);
            $y = rand(1, max: 5);
            echo 'Resta Numeros aleatoris: ' . restaAmbParametre($x, $y);
            break;
        case 3:
            $x = rand(1, max: 5);
            $y = rand(1, max: 5);
            echo 'Producte Numeros aleatoris: ' . producteAmbParametre($x, $y);
            break;
        case 4:
            $x = rand(1, max: 5);
            $y = rand(1, max: 5);
            echo 'Divisio Numeros aleatoris: ' . divisioAmbParametre($x, $y);
            break;
        case 5:
            $x = rand(25, max: 100);
            echo 'Arrel Quadrada Numeros aleatoris: ' . arrelQuadradaAmbParametre($x, $y);
            break;
        default:
            echo 'Error, el numero no esta asignat: ';
            break;
    }

    function sumaAmbParametre($x, $y)
    {
        return $x + $y;
    }
    function restaAmbParametre($x, $y)
    {
        return $x - $y;
    }
    function producteAmbParametre($x, $y)
    {
        return $x * $y;
    }
    function divisioAmbParametre($x, $y)
    {
        return $x / $y;
    }
    function arrelQuadradaAmbParametre($x)
    {
        return sqrt($x);
    }

    ?>

    <?php
    $numero = rand(1, max: 5);
    $x = rand(1, max: 20);
    $y = rand(1, max: 20);
    switch ($numero) {
        case 1:
            echo 'Suma Numeros aleatoris: ' . sumaSense();
            break;
        case 2:
            echo 'Resta Numeros aleatoris: ' . restaSense();
            break;
        case 3:
            echo 'Producte Numeros aleatoris: ' . producteSense();
            break;
        case 4:
            echo 'Divisio Numeros aleatoris: ' . divisioSense();
            break;
        case 5:
            echo 'Arrel Quadrada Numeros aleatoris: ' . arrelSense();
            break;
        default:
            echo 'Error, el numero no esta asignat: ';
            break;
    }

    function sumaSense()
    {
        return $x + $y;
    }
    function restaSense()
    {
        return $x - $y;
    }
    function producteSense()
    {
        return $x * $y;
    }
    function divisioSense()
    {
        return $x / $y;
    }
    function arrelSense()
    {
        return sqrt($x);
    }

    ?>


</body>

</html>