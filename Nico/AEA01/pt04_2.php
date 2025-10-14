<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Formulari i resposta</title>
</head>

<body>

    <h1>Formulari i resposta</h1>
    <form action="pt04_3.php" method="post">
        <label for="model">Model:</label>
        <input type="text" name="model" id="model" required><br>

        <label for="marca">Marca:</label>
        <input type="text" name="marca" id="marca" required><br>

        <label for="motor">Motor:</label>
        <input type="text" name="motor" id="motor" required>

        <label for="cilindrada">Cilindrada:</label>
        <input type="text" name="cilindrada" id="cilindrada" required><br>

        <label for="energia-gasolina">Energia:</label>
        <input type="radio" name="energia" id="energia-gasolina" value="Gasolina" required> Gasolina
        <input type="radio" name="energia" id="energia-diesel" value="Diesel" required> Diesel
        <input type="radio" name="energia" id="energia-hibrid" value="Híbrid" required> Híbrid
        <input type="radio" name="energia" id="energia-electric" value="Elèctric" required> Elèctric<br>

        <label for="opcions">Opcions:</label>
        <select name="opcions[]" id="opcions" multiple required>
            <option value="Pack Sport">Pack Sport</option>
            <option value="Millora seguretat">Millora seguretat</option>
            <option value="Climatitzador">Climatitzador</option>
            <option value="Ordinador a bord">Ordinador a bord</option>
        </select><br>

        <input type="submit" value="Envia">
        <input type="reset" value="Inicialitza">
    </form>
</body>

</html>