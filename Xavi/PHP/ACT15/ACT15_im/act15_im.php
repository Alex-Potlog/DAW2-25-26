<?php

$url = "http://www.portalmochis.net/humor/ilusiones/";
$dades = file_get_contents($url);
$links = [];
preg_match_all('/<a href="([^"]+\.(jpg|jpeg|png|gif))"/i', $dades, $links);
$noms = $links[1];


echo "<table cellspacing='30' style='margin: 0 auto';>";


for ($i = 0; $i < count($noms); $i++) {

    if ($i % 2 == 0) {
        echo "<tr>";
    }

    $nomIm = basename($noms[$i]);

    echo "<td><img src='{$url}{$nomIm}' alt='{$nomIm}' width='300'></td>";

    if ($i % 2 == 1) {
        echo "</tr>";
    }
}


echo "</table>";
