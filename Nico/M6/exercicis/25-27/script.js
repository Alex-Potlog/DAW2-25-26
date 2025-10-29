/*Crea un array bidimensional 3x3 i emplena'l amb números aleatoris des de l'1 al 29 sense repetits.
Fes-ho de manera que l'script funcioni per a qualsevol array bidimensional, per exemple: 2x3. 4x4,
5x2, etc. sense fer cap modificació */

console.log("---- Exercici 25 ----");
const filas = 3; //max 9 para evitar problemas
const columnas = 3;
const arrBidimensional = [];
for (let i = 0; i < filas; i++) {
    arrBidimensional[i] = [];
    for (let j = 0; j < columnas; j++) {
        let numeroAleatori;
        let existeix = false;
        do {
            numeroAleatori = Math.floor(Math.random() * 10 * columnas - 1) + 1; //de 1 a X9
            existeix = false;
            //Comprovar si ja existeix el numero en l'array bidimensional
            for (let x of arrBidimensional) {
                for (let y of x) { //Cuando se usa of, no es index, es el valor en si
                    if (y === numeroAleatori) {
                        existeix = true;
                    }
                }
            }
        } while (existeix);
        arrBidimensional[i][j] = numeroAleatori;
    }
}
console.log("Array bidimensional de " + filas + "x" + columnas + " amb números aleatoris sense repetir:");
console.log(arrBidimensional);

/*26.
A l'array anterior, fes que:
1. La primera columna contingui els números entre 1 i 9
2. La segona columna contingui els números entre 10 i 19
3. La tercera columna contingui els números entre 20 i 29
*/
console.log("---- Exercici 26 ----");
const unificador = arrBidimensional.flat();
unificador.sort((a, b) => a - b)
console.log(unificador)
//Si tiene mas columnas de 9, habria que hacer mas filtros
const arrColumna1 = unificador.filter(num => num >= 1 && num <= 9);
const arrColumna2 = unificador.filter(num => num >= 10 && num <= 19);
const arrColumna3 = unificador.filter(num => num >= 20 && num <= 29);
const arrColumna4 = unificador.filter(num => num >= 30 && num <= 39);
const arrColumna5 = unificador.filter(num => num >= 40 && num <= 49);
const arrColumna6 = unificador.filter(num => num >= 50 && num <= 59);
const arrColumna7 = unificador.filter(num => num >= 60 && num <= 69);
const arrColumna8 = unificador.filter(num => num >= 70 && num <= 79);
const arrColumna9 = unificador.filter(num => num >= 80 && num <= 89);


const arrFinal = [];
for (let i = 0; i < filas; i++) {
    arrFinal[i] = [];
    for (let j = 0; j < columnas; j++) {
        if (j === 0) {
            arrFinal[i][j] = arrColumna1[i];
        } else if (j === 1) {
            arrFinal[i][j] = arrColumna2[i];
        } else if (j === 2) {
            arrFinal[i][j] = arrColumna3[i];
        } else if (j === 3) {
            arrFinal[i][j] = arrColumna4[i];
        } else if (j === 4) {
            arrFinal[i][j] = arrColumna5[i];
        } else if (j === 5) {
            arrFinal[i][j] = arrColumna6[i];
        } else if (j === 6) {
            arrFinal[i][j] = arrColumna7[i];
        } else if (j === 7) {
            arrFinal[i][j] = arrColumna8[i];
        } else if (j === 8) {
            arrFinal[i][j] = arrColumna9[i];
        }//si, se que esta mal hacer esto 
    }
}
console.log("Array bidimensional de " + filas + "x" + columnas + " amb números ordenats per columnes:");
console.log(arrFinal); //No se ven bien cuando hay un numero diferente a 3 por columna (4 numneros en la primera, 0 en la segunda, etc)

/*27. A l'array anterior, fes que:
1. La primera columna sigui amb ordre ascendent
2. La segona columna sigui amb ordre descendent
3. La tercera columna sigui amb ordre ascendent */
console.log("---- Exercici 27 ----");
for (let j = 0; j < columnas; j++) {
    //Extraer columna
    const columna = [];
    for (let i = 0; i < filas; i++) {
        columna.push(arrFinal[i][j]);
    }
    //Ordenar columna
    if (j % 2 === 0) { //si es par, ascendente
        columna.sort((a, b) => a - b);
    } else { //si es impar, descendente
        columna.sort((a, b) => b - a);
    }
    //Volver a colocar la columna ordenada en el array bidimensional
    for (let i = 0; i < filas; i++) {
        arrFinal[i][j] = columna[i];
    }
}
console.log("Array bidimensional de " + filas + "x" + columnas + " amb números ordenats per columnes alternant ordre:");
console.log(arrFinal);