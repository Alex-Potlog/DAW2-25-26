<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Activitat 1.4 - Formularis</title>
</head>
<body>
    <!-- Implementa en un únic fitxer (exercici1) un formulari que demani a l'usuari el seu nom i la seva data de naixement. 
    Utilitza action="php echo $_SERVER["PHP_SELF"];"
        
    Per introduir la data de naixement, utilitza un menú de selecció generant els nombres de dia, mes i any (des de 1990 fins 2020) mitjançant php.

    Fes-lo amb el mètode GET.
    
    Processar el formulari serà calcular l'edat del usuari i mostrar-li d'aquesta manera: " Ets la Laia i tens 25 anys" -->

    <?php
        echo "<b>EXERCICI 1</b><br>";
        echo "------------------------------------------";
    
    if ($_SERVER["REQUEST_METHOD"]=="GET" && isset ($_GET['nom']) && isset ($_GET['dia']) && isset ($_GET['mes']) && isset ($_GET['any'])){
        $nom=$_GET['nom'];
        $diaNaixement=$_GET['dia'];
        $mesNaixement=$_GET['mes'];
        $anyNaixement=$_GET['any'];
        
        $anyActual=date("Y");
        $mesActual=date("m");
        $diaActual=date("d");

        $edat=$anyActual-$anyNaixement;

        if ($mesActual<$mesNaixement || ($mesActual==$mesNaixement && $diaActual<$diaNaixement)){
            $edat--;
        }

        echo "<p><strong>Ets $nom i tens $edat anys</strong></p>";
        echo "<p><a href='" . $_SERVER['PHP_SELF'] . "'>Tornar al formulari</a></p>";
    } else{
    ?>

        <form method="GET" action="<?php echo $_SERVER["PHP_SELF"];?>">
            Name: <input type="text" name="nom"><br>
            <label for="date">Data de naixement </label>
            <select name="dia" id="date">
                <?php
                    for ($i=1; $i<=31; $i++){
                        echo "<option value='$i'>$i</option>";
                    }
                ?>
            </select>
            <select name="mes" id="date">
                <?php
                    for ($i=1; $i<=12; $i++){
                        echo "<option value='$i'>$i</option>";
                    }
                ?>
            </select>
            <select name="any" id="date">
                <?php
                    for ($i=1990; $i<=2020; $i++){
                        echo "<option value='$i'>$i</option>";
                    }
                ?>
            </select>
            <br>
            <input type="submit">

        
        </form>
    <?php
    }
    ?>
</body>
</html>