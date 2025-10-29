<?php
/*1-. Implementa una aplicació web senzilla on la pàgina inicial demanarà el nom al usuari connectat i si es torna a connectar altra vegada,
l'aplicació mostrarà un missatge personalitzat de benvinguda.

Hauràs de crear una galeta per guardar el nom dels usuaris que es van connectant.

A cada connexió hauràs de comprovar si existeix la galeta corresponent per saludar o no de manera personalitzada.

A més, afegeix un camp que permeti a l’usuari comunicar que vol esborrar la cookie. En aquest cas s'haurà d’eliminar.



2-. Implementa utilitzant cookies una pàgina web que ens mostri la data actual, la data de l'últim accés i el nombre de visites que ha rebut.

A més afegeix dos enllaços, un per actualitzar la pàgina en quant a data, hora i nombre d'accessos) i l'altre per tornar a començar, com si mai s'anés connectat. La pàgina pot tenir el següent aspecte:



3-. Implementa, ara utilitzant sessions, la mateixa pàgina demanada en el punt 2 */

?>
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cookies</title>
</head>

<body>
    <form action="pt06_2.php" method="post">
        <label for="nomusuari">Nom d'usuari</label>
        <input type="text" name="nomusuari" id="nomusuari">
        <input type="submit" value="Enviar">
        <br>
        <p><a href="pt06_2.php?erase=1">Eliminar cookie</a></p>

    </form>
</body>

</html>