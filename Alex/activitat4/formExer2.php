<!DOCTYPE html>
<html lang="ca">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Formulari i resposta</title>
    <style>
        body {
            font-family: Arial, Helvetica, sans-serif;
        }

        .container {
            width: 640px;
            margin: 30px auto;
        }

        h1 {
            text-align: center;
        }

        table {
            width: 100%;
        }

        td.label {
            width: 120px;
            vertical-align: top;
            padding: 6px 8px;
        }

        td.input {
            vertical-align: top;
            padding: 6px 8px;
        }

        .controls {
            text-align: center;
            margin-top: 12px;
        }

        /* Caja que imita el aspecto del <select> */
        .opcions-box {
            width: 220px;
            height: 96px;
            /* parecido a size="4" */
            border: 1px solid #ccc;
            border-radius: 2px;
            overflow-y: auto;
            background: #fff;
            padding: 6px;
        }

        .opcions-box label {
            display: block;
            padding: 4px 6px;
            cursor: pointer;
        }

        .opcions-box label:hover {
            background: #f0f0f0;
        }

        .opcions-box input[type="checkbox"] {
            margin-right: 8px;
        }
    </style>
</head>

<body>
    <div class="container">
        <h1>Formulari i resposta</h1>

        <form action="procExer2.php" method="post">
            <table>
                <tr>
                    <td class="label"><label for="model">Model:</label></td>
                    <td class="input"><input type="text" id="model" name="model" size="40" aria-required="true"></td>
                </tr>
                <tr>
                    <td class="label"><label for="marca">Marca:</label></td>
                    <td class="input"><input type="text" id="marca" name="marca" size="40" aria-required="true"></td>
                </tr>
                <tr>
                    <td class="label"><label for="motor">Motor:</label></td>
                    <td class="input">
                        <input type="text" id="motor" name="motor" size="12">
                        &nbsp;&nbsp;<label for="cilindrada">Cilindrada:</label>
                        <input type="text" id="cilindrada" name="cilindrada" size="13" aria-required="true">
                    </td>
                </tr>
                <tr>
                    <td class="label">Energia:</td>
                    <td class="input">
                        <label><input type="radio" name="energia" value="Gasolina" checked> Gasolina</label>
                        <label><input type="radio" name="energia" value="Diesel"> Diesel</label>
                        <label><input type="radio" name="energia" value="Hibrid"> Híbrid</label>
                        <label><input type="radio" name="energia" value="Electric"> Elèctric</label>
                    </td>
                </tr>
                <tr>
                    <td class="label"><label for="opcions">Opcions:</label></td>
                    <td class="input">
                        <fieldset>
                            <label><input type="checkbox" name="opcions[]" value="pack_sport"> Pack Sport</label><br>
                            <label><input type="checkbox" name="opcions[]" value="millora_segur"> Millora
                                seguretat</label><br>
                            <label><input type="checkbox" name="opcions[]" value="climatitzador">
                                Climatitzador</label><br>
                            <label><input type="checkbox" name="opcions[]" value="ordinador"> Ordinador a
                                bord</label><br>
                        </fieldset>
                    </td>
                </tr>
            </table>

            <div class="controls">
                <input type="submit" value="Envia">
                <input type="reset" value="Inicialitza">
            </div>
        </form>
    </div>
</body>

</html>