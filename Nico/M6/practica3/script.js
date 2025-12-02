function generarCartro() {
    let cartro;
    let valid = false;

    // Intentar generar un cartró vàlid
    while (!valid) {
        cartro = [];

        // Generar 3 files
        for (let fila = 0; fila < 3; fila++) {
            cartro[fila] = [];

            // Calcular 4 buides i 5 amb números per fila
            const columnesBuides = [];
            while (columnesBuides.length < 4) {
                const col = Math.floor(Math.random() * 9);
                if (!columnesBuides.includes(col)) {
                    columnesBuides.push(col);
                }
            }

            // Crear la fila
            for (let col = 0; col < 9; col++) {
                if (columnesBuides.includes(col)) {
                    cartro[fila][col] = null;
                } else {
                    cartro[fila][col] = 0; // Marcar temporalment per omplir després
                }
            }
        }

        // Verificar que no hi hagi columnes amb 3 plenes o 3 buides
        valid = true;
        for (let col = 0; col < 9; col++) {
            let comptador = 0;
            for (let fila = 0; fila < 3; fila++) {
                if (cartro[fila][col] !== null) comptador++;
            }

            // Si hi ha 0 o 3 números, el cartró no és vàlid
            if (comptador === 0 || comptador === 3) {
                valid = false;
                break;
            }
        }
    }

    // Omplir amb números
    const numerosUsats = new Set();

    for (let col = 0; col < 9; col++) {
        const numeros = [];
        const min = col === 0 ? 1 : col * 10;
        const max = col === 8 ? 90 : (col + 1) * 10 - 1;

        // Comptar quants números calen per a aquesta columna
        let necessaris = 0;
        for (let fila = 0; fila < 3; fila++) {
            if (cartro[fila][col] !== null) necessaris++;
        }

        // Generar números únics per a aquesta columna
        while (numeros.length < necessaris) {
            const num = Math.floor(Math.random() * (max - min + 1)) + min;
            if (!numerosUsats.has(num)) {
                numeros.push(num);
                numerosUsats.add(num);
            }
        }

        // Determinar si la columna és ascendent o descendent
        const esAscendent = col % 2 === 0;
        numeros.sort((a, b) => esAscendent ? a - b : b - a);

        // Assignar números a les cel·les
        let indexNum = 0;
        for (let fila = 0; fila < 3; fila++) {
            if (cartro[fila][col] !== null) {
                cartro[fila][col] = numeros[indexNum++];
            }
        }
    }

    mostrarCartro(cartro);
}

function mostrarCartro(cartro) {
    const cartróBingo = document.getElementById('cartroBingo');
    cartróBingo.innerHTML = '';

    for (let fila = 0; fila < 3; fila++) {
        for (let col = 0; col < 9; col++) {
            const cell = document.createElement('div');
            cell.className = 'cell';

            if (cartro[fila][col] === null) {
                cell.classList.add('buit');
            } else {
                cell.textContent = cartro[fila][col];
                cell.onclick = function () {
                    this.classList.toggle('marcat');
                };
            }

            cartróBingo.appendChild(cell);
        }
    }
}
