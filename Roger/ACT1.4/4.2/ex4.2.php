<!DOCTYPE html>
<html lang="ca">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Formulari i resposta</title>

    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 500px;
            margin: 50px auto;
            padding: 20px;
        }

        h1 {
            text-align: center;
            font-size: 24px;
            margin-bottom: 30px;
        }

        .form-group {
            margin-bottom: 15px;
            display: flex;
            align-items: center;
        }

        label {
            display: inline-block;
            width: 100px;
            font-weight: normal;
        }

        input[type="text"] {
            padding: 5px;
            border: 1px solid #ccc;
            flex: 1;
        }

        .short-input {
            width: 80px;
        }

        .radio-group {
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .radio-group label {
            width: auto;
            margin-left: 5px;
        }

        .options-group {
            margin-top: 20px;
        }

        select {
            width: 200px;
            height: 80px;
            padding: 5px;
            border: 1px solid #ccc;
        }

        .button-group {
            margin-top: 20px;
            text-align: center;
        }

        button {
            padding: 5px 20px;
            margin: 0 10px;
            background-color: #f0f0f0;
            border: 1px solid #999;
            border-radius: 3px;
            cursor: pointer;
        }

        button:hover {
            background-color: #e0e0e0;
        }
    </style>
</head>

<body>

    <h1>Formulari i resposta</h1>

    <form action="proc_ex4.2.php" method="POST">
        <div class="form-group">
            <label for="model">Model:</label>
            <input type="text" id="model" name="model">
        </div>

        <div class="form-group">
            <label for="marca">Marca:</label>
            <input type="text" id="marca" name="marca">
        </div>

        <div class="form-group">
            <label for="motor">Motor:</label>
            <input type="text" id="motor" name="motor" class="short-input">
            <label for="cilindrada" style="margin-left: 20px;">Cilindrada:</label>
            <input type="text" id="cilindrada" name="cilindrada" class="short-input">
        </div>

        <div class="form-group">
            <label>Energia:</label>
            <div class="radio-group">
                <input type="radio" id="gasolina" name="energia" value="gasolina" checked required>
                <label for="gasolina">Gasolina</label>

                <input type="radio" id="diesel" name="energia" value="diesel" required>
                <label for="diesel">Diesel</label>

                <input type="radio" id="hibrid" name="energia" value="hibrid" required>
                <label for="hibrid">Híbrid</label>

                <input type="radio" id="electric" name="energia" value="electric" required>
                <label for="electric">Elèctric</label>
            </div>
        </div>

        <div class="form-group options-group">
            <label>Opcions:</label>
            <select multiple>
                <option>Pack Sport</option>
                <option>Millora seguretat</option>
                <option>Climatitzador</option>
                <option>Ordinador a bord</option>
            </select>
        </div>

        <div class="button-group">
            <button type="submit">Envia</button>
            <button type="reset">Inicialitza</button>
        </div>
    </form>
</body>

</html>