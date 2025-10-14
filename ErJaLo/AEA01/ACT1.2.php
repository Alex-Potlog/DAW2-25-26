<!DOCTYPE html>

<head>
    <html lang="es">

    <style>
        body {
            height: 5000px;
        }
    </style>
</head>
<html>

<body>

    <?php
    //1. Calcula tres nombres aleatoris i, utilitzant l'operador condicional "? :", mostri per pantalla quins és el nombre major i quin és el nombre menor.
    $numeros = array(
        'N1' => rand(0, 10),
        'N2' => rand(0, 10),
        'N3' => rand(0, 10)
    );
    foreach ($numeros as $key => $value) {
        echo 'Posició: ' . $key . ' Valor:' . $value . '<br>';
    }
    echo '<br><span>' . 'Valor Maxim:' . '</span>';
    echo ($numeros['N1'] > $numeros['N2']) ? ($numeros['N1'] > $numeros['N3'] ? $numeros['N1'] : $numeros['N3']) : ($numeros['N2'] > $numeros['N3'] ? $numeros['N2'] : $numeros['N3']);
    echo '<br><span>' . 'Valor Maxim:' . '</span>';
    echo '' . ($numeros['N1'] < $numeros['N2']) ? ($numeros['N1'] < $numeros['N3'] ? $numeros['N1'] : $numeros['N3']) : ($numeros['N2'] < $numeros['N3'] ? $numeros['N2'] : $numeros['N3']);
    echo '<br>';
    ?>

    <?php
    //2. Inicialitza un array associatiu que tingui com a clau el nom del país i com a valor el nombre d'habitants. Mostra en el navegador les dades de manera llegible
    $paises = array(
        'España' => 48810000,
        'Francia' => 68529000,
        'Andorra' => 81938
    );
    echo '<br>';
    foreach ($paises as $key => $value) {
        echo 'Pais: ' . $key . ' Habitantes:' . $value . '<br>';
    }
    echo '<br>';
    ?>

    <?php
    //3. Inicialitza un array associatiu amb quatre registres de participants en una carrera. Genera els dorsals dels corredors i emmagatzema'ls en l'última casella de l'array. El format del dorsal és: H, D o X en funció del gènere + les tres primeres lletres del nom (la 1a en majúscula) + les tres primeres lletres del primer cognom (la 1a en majúscula). Mostra pel navegador l'array sencer de manera legible.
    $noms = array(
        ['Genere' => 'H', 'Nom' => 'Jan', 'Cognom' => 'Lopez'],
        ['Genere' => 'H', 'Nom' => 'John', 'Cognom' => 'Esparrell'],
        ['Genere' => 'H', 'Nom' => 'Ibai', 'Cognom' => 'Palomino'],
        ['Genere' => 'D', 'Nom' => 'Edith', 'Cognom' => 'Esposa'],
    );
    $participants = array();
    foreach ($noms as $value) {
        $participants[$value['Genere'] . ucfirst(substr($value['Nom'], 0, 3)) . ucfirst(substr($value['Cognom'], 0, 3))] = rand(540, 900);
    }

    foreach ($participants as $key => $value) {
        echo 'Participant: ' . $key . ' Temps (segons): ' . $value . ' Minuts: ' . (int) ($value / 60) . 'm ' . $value % 60 . 's';
        echo '<br>';
    }

    ?>
    <style>
        .row {
            display: flex;
            flex-wrap: wrap;
        }

        .w-100 {
            width: 100%;
        }

        .w-50 {
            width: 50%;
        }

        .m0a {
            margin: 0px auto;
        }

        .celda {
            width: 5em;
            height: 5em;
            text-align: center;
            border: 1px solid black;
            align-content: center;
        }
    </style>
    <div class="container w-50 m0a">
        <div class="row">
            <?php
            for ($i = 1; $i <= 10; $i++) {
                echo '<div class="w-100 row">';
                for ($j = 1; $j <= 10; $j++) {
                    echo '<div class="celda">';
                    echo $i * $j;
                    echo '</div>';
                }
                echo '</div>';
            }
            echo '</div>';
            echo '</div>';

            ?>

            <?php
            echo '<br>';
            echo '<br>';
            echo '<br>';
            echo '<br>';

            $ciudades = array(
                "Madrid",
                "Barcelona",
                "Valencia",
                "Sevilla",
                "Zaragoza",
                "Bilbao",
                "Granada",
                "Málaga",
                "Toledo",
                "Santander"
            );

            $sort = $ciudades;
            sort($sort);
            echo '<div class="container w-50 m0a">';
            echo '<p>Sort</p>';
            echo '<div class="row">';
            foreach ($sort as $value) {
                echo '<div class="celda">';
                echo "" . $value . " ";
                echo '</div>';

            }
            echo '</div>';
            echo '</div>';


            $rsort = $ciudades;
            rsort($rsort);
            echo '<div class="container w-50 m0a">';
            echo '<p>Sort</p>';
            echo '<div class="row">';
            foreach ($rsort as $value) {
                echo '<div class="celda">';
                echo "" . $value . " ";
                echo '</div>';

            }
            echo '</div>';
            echo '</div>';


            $asort = $ciudades;
            asort($asort);
            echo '<div class="container w-50 m0a">';
            echo '<p>Sort</p>';
            echo '<div class="row">';
            foreach ($asort as $value) {
                echo '<div class="celda">';
                echo "" . $value . " ";
                echo '</div>';

            }
            echo '</div>';
            echo '</div>';


            $arsort = $ciudades;
            arsort($arsort);
            echo '<div class="container w-50 m0a">';
            echo '<p>Sort</p>';
            echo '<div class="row">';
            foreach ($arsort as $value) {
                echo '<div class="celda">';
                echo "" . $value . " ";
                echo '</div>';

            }
            echo '</div>';
            echo '</div>';


            $ksort = $ciudades;
            ksort($ksort);
            echo '<div class="container w-50 m0a">';
            echo '<p>Sort</p>';
            echo '<div class="row">';
            foreach ($ksort as $value) {
                echo '<div class="celda">';
                echo "" . $value . " ";
                echo '</div>';

            }
            echo '</div>';
            echo '</div>';


            $krsort = $ciudades;
            krsort($ksort);
            echo '<div class="container w-50 m0a">';
            echo '<p>Sort</p>';
            echo '<div class="row">';
            foreach ($krsort as $value) {
                echo '<div class="celda">';
                echo "" . $value . " ";
                echo '</div>';

            }
            echo '</div>';
            echo '</div>';


            $shuffle = $ciudades;
            shuffle($shuffle);
            echo '<div class="container w-50 m0a">';
            echo '<p>Sort</p>';
            echo '<div class="row">';
            foreach ($shuffle as $value) {
                echo '<div class="celda">';
                echo "" . $value . " ";
                echo '</div>';

            }
            echo '</div>';
            echo '</div>';

            ?>
        </div>
    </div>


</body>