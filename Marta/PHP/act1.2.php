<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Activitat 1.2</title>
</head>
<body>
    <?php
    /*1. Calcula tres nombres aleatoris i, utilitzant l'operador condicional "? :", 
    mostri per pantalla quins és el nombre major i quin és el nombre menor.
    */
    echo "<b>Exercici 1</b>"."<br>";
    $num1= rand(0,100);
    $num2= rand(0,100);
    $num3= rand(0,100);

    echo "Els nombres generats són: $num1, $num2, $num3<br><br>";
    
    $mesGran = ($num1>$num2) ? (($num1>$num3) ? $num1 : $num3) : (($num2>$num3) ? $num2 : $num3);
    $menor = ($num1 < $num2) ? (($num1 < $num3) ? $num1 : $num3) : (($num2 < $num3) ? $num2 : $num3);

    echo "El número mes gran és: $mesGran<br>";
    echo "El número mes petit és: $menor";
    echo "<br><br>";
    /*2. Inicialitza un array associatiu que tingui com a clau el nom del país i 
    com a valor el nombre d'habitants. Mostra en el navegador les dades de manera llegible*/
    echo "<b>Exercici 2</b>"."<br>";

    $paisHabitants= array("Espanya" => 99852, "França"=> 105741, "Alemanya"=>102963, "Italia"=> 100159);
    #var_dump($paisHabitants);

    foreach ($paisHabitants as $x => $y){
        echo "$x : $y <br>";
    }

    echo "<br>";
    /*3.Inicialitza un array associatiu amb quatre registres de participants en una carrera. 
    Genera els dorsals dels corredors i emmagatzema'ls en l'última casella de l'array. 
    El format del dorsal és: H, D o X en funció del gènere + les tres primeres lletres del nom (la 1a en majúscula) 
    + les tres primeres lletres del primer cognom (la 1a en majúscula). Mostra pel navegador l'array sencer de manera legible.*/
    echo "<b>Exercici 3</b>"."<br>";
        $dorsals=array(
                ["genere" => "D",
                "nom" => "Marta",
                "cognom"=>"Llabres"],

                ["genere" => "H",
                'nom' => "Eric",
                "cognom"=>"Munoz"],

                ["genere" => "X",
                "nom" => "Noah",
                "cognom"=>"Cespedes"],

                ["genere" => 'D',
                "nom" => "Meritxell",
                "cognom"=>"Rodriguez"]
        );

        foreach ($dorsals as $index => $corredor){
            $dorsal=$corredor['genere']
            .strtoupper(substr($corredor['nom'], 0, 1)).strtolower(substr($corredor['nom'], 1, 2))
            .strtoupper(substr($corredor['cognom'], 0, 1)).strtolower(substr($corredor['cognom'], 1, 2));
            
            $dorsals[$index]['dorsal']=$dorsal;
        }
        
        echo "<pre>";
        var_dump($dorsals);   
        echo "</pre>";

        //Imprimir amb foreach
        foreach ($dorsals as $corredor) {
            echo  $corredor['nom'] . " " . $corredor['cognom1'] . " amb dorsal " . $corredor['dorsal'] . "<br>";
        }
    echo "<br>";

    /*4. Implementa un script que mostri per pantalla una graella semblant a la següent: (Aula Virtual)*/
    echo "<b>Exercici 4</b>"."<br>";
    echo "<table border='1' style='text-align: center;'>";

    for ($i=1; $i<=10; $i++){
        echo "<tr>";
        for ($j=1; $j<=10; $j++){
            $num = ($i - 1) * 10 + $j;
            echo "<td>$num</td>";
        }
        echo "</tr>";
    }
    echo "</table>";
    echo "<br>";
    /*5.  Inicialitza un array amb 10 ciutats, crida a les diferents funcions d'ordenació que ofereix PHP 
    (sort(), rsort(), asort(), arsort(), ksort(), krsort() i shuffle()) explicant com ordena i mostra el resultat pel navegador.*/
    echo "<b>Exercici 5</b>"."<br>";
        $ciutats= ['Barcelona', 'Girona', 'Màlaga', 'Mallorca', 'Santiago de Compostela', 'Berlin', 'Paris', 'Roma', 'Manchester', 'Londres'];

        #sort()
        sort($ciutats);

        foreach ($ciutats as $key => $val){
            echo "Ciutats [".$key."] = ".$val . "<br>";
        }
        echo "/-----------------------------------------------------------------------------------/<br>";

        #rsort()
        rsort($ciutats);

        $clength=count($ciutats);
        for($x=0;$x<$clength;$x++) {
            echo $ciutats[$x];
            echo "<br>";
        };
        echo "/-----------------------------------------------------------------------------------/<br>";

        #asort()
        asort($ciutats);

        foreach($ciutats as $x=>$x_value) {
                echo "Key=" . $x . ", Value=" . $x_value;
                echo "<br>";
        };
        echo "/-----------------------------------------------------------------------------------/<br>";
        #arsort()
        arsort($ciutats);

        foreach($ciutats as $x=>$x_value) {
            echo "Key=" . $x . ", Value=" . $x_value;
            echo "<br>";
        };
        echo "/-----------------------------------------------------------------------------------/<br>";
        #ksort()
        ksort($ciutats);

        foreach($ciutats as $x=>$x_value) {
            echo "Key=" . $x . ", Value=" . $x_value;
            echo "<br>";
        };
        echo "/-----------------------------------------------------------------------------------/<br>";
        #krsort()
        krsort($ciutats);

        foreach($ciutats as $x=>$x_value) {
            echo "Key=" . $x . ", Value=" . $x_value;
            echo "<br>";
        };
        echo "/-----------------------------------------------------------------------------------/<br>";
        #shuffle()
        shuffle($ciutats);
        print_r($ciutats);
    ?>
</body>
</html>