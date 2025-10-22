// 25. Crea un array bidimensional 3x3 i emplena'l amb números aleatoris des de l'1 al 29 sense repetits.
// Fes-ho de manera que l'script funcioni per a qualsevol array bidimensional, per exemple: 2x3. 4x4,
// 5x2, etc. sense fer cap modificació


function crearArrayBidimensional(files, columnes) {
    const totalElements = files * columnes;
    const numerosUnics = [];
    
    // Generar números únics
    while (numerosUnics.length < totalElements) {
        const num = Math.floor(Math.random() * 29) + 1;
        if (!numerosUnics.includes(num)) {
            numerosUnics.push(num);
        }
    }
    
    // Crear l'array bidimensional
    const arrayBidimensional = [];
    for (let i = 0; i < files; i++) {
        const fila = [];
        for (let j = 0; j < columnes; j++) {
            fila.push(numerosUnics[i * columnes + j]);
        }
        arrayBidimensional.push(fila);
    }
    
    return arrayBidimensional;
}

console.log(crearArrayBidimensional(4,1))

// 26. A l'array anterior, fes que:
// 1. La primera columna contingui els números entre 1 i 9
// 2. La segona columna contingui els números entre 10 i 19
// 3. La tercera columna contingui els números entre 20 i 29

function crearArrayBidimensional2() {
    const arrayBidimensional = [];

    // Fila 0: números entre 1-9
    const fila0 = [];
    while (fila0.length < 3) {
        const num = Math.floor(Math.random() * 9) + 1;
        if (!fila0.includes(num)) {
            fila0.push(num);
        }
    }
    arrayBidimensional.push(fila0);

    // Fila 1: números entre 10-19
    const fila1 = [];
    while (fila1.length < 3) {
        const num = Math.floor(Math.random() * 10) + 10;
        if (!fila1.includes(num)) {
            fila1.push(num);
        }
    }
    arrayBidimensional.push(fila1);

    // Fila 2: números entre 20-29
    const fila2 = [];
    while (fila2.length < 3) {
        const num = Math.floor(Math.random() * 10) + 20;
        if (!fila2.includes(num)) {
            fila2.push(num);
        }
    }
    arrayBidimensional.push(fila2);
    
    return arrayBidimensional;
}

const arrbid = crearArrayBidimensional2();
console.log(arrbid);



// const object = {name:"si"}
// const json = JSON.stringify(object);

// localStorage.setItem("object",json);

// const recuperada= JSON.parse(localStorage.getItem("object"))

// 27. A l'array anterior, fes que:
// 1. La primera columna sigui amb ordre ascendent
// 2. La segona columna sigui amb ordre descendent
// 3. La tercera columna sigui amb ordre ascendent