/*28. Realitza un script amb funcionalitat de calculadora. 
Utilitza un formulari amb 2 inputs i un selector de operador.
Operacions: suma, resta, multiplicació, divisió i potència.
El resultat s’ha de mostrar amb dos decimals.
El separador decimal és el punt (.), si s’introdueix una coma (,) s’ha de substituir.
Si en el càlcul es produeix un error NaN o Infinity s’ha de mostrar de color vermell
En el cas de l'operació de potència (^) si el segon operador és un número decimal.
S'ha de truncar i mostrar el nou valor en el camp del segon operand
*/
console.log("---- Exercici 28 ----");
const formulari = document.createElement('div');


// Crear el título
const title = document.createElement('h2');
title.textContent = 'Calculadora';

// Crear el formulario
const form = document.createElement('form');
form.id = 'calculadoraForm';

// Función para crear campos del formulario
function createField(labelText, inputName) {
    const fieldDiv = document.createElement('div');

    const label = document.createElement('label');
    label.textContent = labelText + ':';

    const br = document.createElement('br');

    const input = document.createElement('input');
    input.type = 'text';
    input.name = inputName;
    input.id = inputName;

    fieldDiv.appendChild(label);
    fieldDiv.appendChild(br);
    fieldDiv.appendChild(input);
    return fieldDiv;
}


form.appendChild(createField('Operand 1', 'operand1'));


// Crear selector de operador
const operatorDiv = document.createElement('div');
const operatorLabel = document.createElement('label');
operatorLabel.textContent = 'Operador:';
const br = document.createElement('br');
const operatorSelect = document.createElement('select');
operatorSelect.name = 'operator';
operatorSelect.id = 'operator';

const operators = ['+', '-', '*', '/', '^'];
for (let op of operators) {
    const option = document.createElement('option');
    option.value = op;
    option.textContent = op;
    operatorSelect.appendChild(option);
}

operatorDiv.appendChild(operatorLabel);
operatorDiv.appendChild(br);
operatorDiv.appendChild(operatorSelect);
form.appendChild(operatorDiv);
form.appendChild(createField('Operand 2', 'operand2'));

// Crear botón de calcular
const calculateBtn = document.createElement('button');
calculateBtn.type = 'button';
calculateBtn.textContent = 'Calcula';

// Crear área para mostrar el resultado
const resultDiv = document.createElement('div');
resultDiv.id = 'result';

// Función para realizar el cálculo
calculateBtn.addEventListener('click', () => {
    let operand1 = document.getElementById('operand1').value.replace(',', '.');
    let operand2 = document.getElementById('operand2').value.replace(',', '.');
    const operator = document.getElementById('operator').value;

    let num1 = Number.parseFloat(operand1);
    let num2 = Number.parseFloat(operand2);

    // Truncar operand2 si el operador es potencia y num2 es decimal
    if (operator === '^' && !Number.isInteger(num2)) {
        num2 = Math.trunc(num2);
        document.getElementById('operand2').value = num2;
    }

    let result;
    switch (operator) {
        case '+':
            result = num1 + num2;
            break;
        case '-':
            result = num1 - num2;
            break;
        case '*':
            result = num1 * num2;
            break;
        case '/':
            result = num1 / num2;
            break;
        case '^':
            result = Math.pow(num1, num2);
            break;
        default:
            result = Number.NaN;
    }

    // Mostrar resultado
    if (isNaN(result)) {
        resultDiv.style.color = 'red';
        resultDiv.textContent = 'Error: NaN';
    } else if (!isFinite(result)) {
        resultDiv.style.color = 'red';
        resultDiv.textContent = 'Error: Infinity';
    } else {
        resultDiv.style.color = 'black';
        resultDiv.textContent = 'Resultat: ' + result.toFixed(2);
    }
});

form.appendChild(calculateBtn);
form.appendChild(resultDiv);

formulari.appendChild(title);
formulari.appendChild(form);

document.body.appendChild(formulari);

