const arrSuma = [3, false, 7, 'Maria', 9];
let suma = 0;
for (let i = 0; i < arrSuma.length; i++) {
    if (arrSuma[i] === 'Number') {
        suma += arrSuma[i];
    }
}

console.log(suma);