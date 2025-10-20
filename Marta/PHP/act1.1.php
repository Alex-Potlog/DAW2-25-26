<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, inicial-scale=1.0">
    <title>Activitat 1.1</title>
</head>
    <body>
        <h3>Exercici 1</h3>
            <?php
            #1. Defineix una variable amb el preu d'un article i una constant 
            #almb el valor de l'IVA vigent. Calcular i mostrar el preu final de l'article en aplicar l'IVA. 
            #Arrodonir als cèntims d'euro.
            $preuProducte = 18;
            define("IVA", 1.21);

            echo "El preu del producte és ".$preuProducte."€<br>";
            echo "El preu amb l'IVA inclòs és de ".$preuProducte * IVA."€<br>";
            echo "El preu arrodonit és ".round($preuProducte * IVA)."€";
            ?>
        <h3>Exercici 2</h3>
            <?php
            /*2. Escriu un script que demani al sistema la data i hora i que mostri pel 
            navegador l'estació de l'any, el mes de l'any, el dia de la setmana i que 
            doni "bon dia", "bona tarda" o "bona nit" segons l'hora.*/
            $numDiaSetmana= date("N");#Dia de la setmana en números (1 dilluns al 7 diumenge). En el cas que vulguem el dia de la setmana escrit hem de fer: $diaSetmana = date("l");
            $diaNum = date("jS");
            $numMes= date("n");#Número del més que estem (1 Gener al 12 Desembre). En el cas que ja ho volguem escrit tenim: $mes = date("F");
            $hora =date("H");

            if ($numMes==1 || $numMes==2 || ($numMes==3 && $diaNum<21) || ($numMes==12 && $diaNum>=21)){
                echo "Estació: Hivern";
            } elseif ($numMes==4 || $numMes==5 || ($numMes==3 && $diaNum>=21) || ($numMes==6 && $diaNum<21)){
                echo "Estació: Primavera";
            }elseif ($numMes==7 || $numMes==8 || ($numMes==9 && $diaNum<21) || ($numMes==6 && $diaNum>=21)){
                echo "Estació: Estiu";
            } else {
                echo "Estació: Tardor";
            }

            switch ($numMes){
                case 1:
                    $nomMes= "Gener";
                    break;
                case 2:
                    $nomMes= "Febrer";
                    break;
                case 3:
                    $nomMes= "Març";
                    break;
                case 4:
                    $nomMes= "Abril";
                    break;
                case 5:
                    $nomMes= "Maig";
                    break;
                case 6:
                    $nomMes= "Juny";
                    break;
                case 7:
                    $nomMes= "Juliol";
                    break;
                case 8:
                    $nomMes= "Agost";
                    break;
                case 9:
                    $nomMes= "Setembre";
                    break;
                case 10:
                    $nomMes= "Octubre";
                    break;
                case 11:
                    $nomMes= "Novembre";
                    break;
                case 12:
                    $nomMes= "Desembre";
                    break;
                default:
                    $nomMes="No existeix més";
            }

            switch ($numDiaSetmana){
                case 1:
                    $dia="Dilluns";
                    break;
                case 2:
                    $dia="Dimarts";
                    break;
                case 3:
                    $dia="Dimecres";
                    break;
                case 4:
                    $dia="Dijous";
                    break;
                case 5:
                    $dia="Divendres";
                    break;
                case 6:
                    $dia="Dissabte";
                    break;
                case 7:
                    $dia="Diumenge";
                    break;
            }

            if ($hora>=06 && $hora<13){
                $momentDia="Bon dia";
            } elseif ($hora>=13 && $hora<21){
                $momentDia="Bona tarda";
            } else {
                $momentDia="Bona nit";
            }
            
            echo "<br> Estem al més de: ".$nomMes;
            echo "<br> El dia de la setmana: ".$dia;
            echo "<br>".$momentDia."!!";

            ?>
        <h3>Exercici 3</h3>
            <?php
            #3. Mostra una contrasenya aleatòria de 8 caràcters de longitud. Els caràcters vàlids són "abcdefghijklmnopqrstuvwxyz0123456789 # $% & @".
            $carValids="abcdefghijklmnopqrstuvwxyz0123456789#$%&@";

            $longitud=8;

            $contrasenya="";
            
            for ($i=0; $i<$longitud; $i++){
                $nou=rand(0, strlen($carValids)-1);
                $contrasenya.=$carValids[$nou];
            };

            echo "Contrasenya generada: ".$contrasenya;
            ?>

        <h3>Exercici 4</h3>
            <?php
            /*4. Escriu un script que generi un enter de 8 dígits, calculi la lletra que li correspon 
            de DNI i mostri pel navegador el resultat de manera llegible.*/

            $numDNI=rand(10000000, 99999999);

            $caract="TRWAGMYFPDXBNJZSQVHLCKE";

            $divi=23;

            $resta=$numDNI%$divi;

            $lletraDNI = substr($caract, $resta, 1);

            echo "El dni generat és ".$numDNI." ".$lletraDNI;
            #echo($resta);

            /*
            $x="ABCD...."
            echo substr ($x, 10, 1)
            */
            ?>
        
        <h3>Exercici 5</h3>
            <?php
            /*5. Implementa un script per a generar els dorsals dels corredors d'una cursa. El format del 
            dorsal és: H, D o X en funció del gènere + les tres primeres lletres del nom (la 1a en majúscula) 
            + les tres primeres lletres del primer cognom (la 1a en majúscula). Inicialitza variables amb
            els valors que vulguis i mostra pel navegador de el dorsal resultant. */
            $genere="D";
            $nom="mArta";
            $cognom="LLabrés";

            $dorsal=$genere.strtoupper(substr($nom, 0, 1)).strtolower(substr($nom, 1, 2)).strtoupper(substr($cognom, 0, 1)).strtolower(substr($cognom, 1, 2));

            echo $dorsal;
            ?>
    </body>
</html>