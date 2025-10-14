<?php
if ($_SERVER["REQUEST_METHOD"] === "POST") {

    $dades = [];

    foreach ($_POST as $clau => $valor) {
        $valor = trim($valor);             // Elimina espais inicials i finals
        $valor = strip_tags($valor);       // Elimina etiquetes HTML/PHP
        $valor = htmlspecialchars($valor); // Evita XSS

        if (empty($valor)) {
            echo "<p>El camp <strong>$clau</strong> és obligatori.</p>";
            exit;
        }

        if ($clau === "cilindrada" && !filter_var($valor, FILTER_VALIDATE_INT)) {
            echo "<p>La cilindrada ha de ser un nombre enter.</p>";
            exit;
        }

        $dades[$clau] = $valor;
    }

    foreach ($dades as $clau => $valor) {
        echo "<strong>" . ucfirst($clau) . ":</strong> $valor</li>";
    }

} else {
    echo "acces no permes";
}
?>