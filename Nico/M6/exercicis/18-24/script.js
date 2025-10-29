/*18. Crea un script per clonar un array
Què ocorre si es fa assignant-lo mitjançant l'operador "=".
    const arr1 = [1,3,5]
    const arr2 = arr1;
Si és un array multidimensional com afecta la clonació.
    const arr1 = [1,[a,b,c],5]
Descriu com treballes els mètodes utilitzats per clonar arrays multidimensionals.*/
console.log("---- Exercici 18 ----");
const arr1 = [1, 3, 5];
const arr2 = arr1; // Assignació per referència
console.log("Arr2 després de l'assignació per referència:", arr2);
arr2[0] = 10; // Modificant arr2 també afecta arr1
console.log("Arr1 després de modificar arr2:", arr1);

// Clonació d'un array unidimensional utilitzant l'operador spread
const arr3 = [...arr1];
arr3[0] = 20; // Modificant arr3 no afecta arr1
console.log("Arr1 després de modificar arr3 (clonació amb spread):", arr1);
console.log("Arr3 (clonat amb spread):", arr3);

// Clonació d'un array multidimensional utilitzant structuredClone
const arr4 = [1, ['a', 'b', 'c'], 5];
const arr5 = structuredClone(arr4); // Clonació profunda , no referència
arr5[1][0] = 'z'; // Modificant arr5 no afecta arr4
console.log("Arr4 després de modificar arr5 (clonació profunda):", arr4);
console.log("Arr5 (clonat profundament):", arr5);
/*19. Crea un script per ordenar pel valor numèric els elements d'un array de manera ascendent*/
console.log("---- Exercici 19 ----");
const arrNum = [34, 2, 23, 67, 4, 89, 1];
arrNum.sort((a, b) => a - b);
console.log("Array ordenat de manera ascendent:", arrNum);

/*
20. Crea una funció per desordenar un array numèric */
console.log("---- Exercici 20 ----");
function desordenarArray(arr) {
    return arr.sort(() => Math.random() - 0.5);
}
const arrDesordenat = desordenarArray([...arrNum]);
console.log("Array desordenat:", arrDesordenat);

/*21. Escriu una funció per ordenar el següent array d'objectes pel valor del libraryID*/
console.log("---- Exercici 21 ----");
const library = [
    { author: 'Bill Gates', title: 'The Road Ahead', libraryID: 1254 },
    { author: 'Steve Jobs', title: 'Walter Isaacson', libraryID: 4264 },
    { author: 'Suzanne Collins', title: 'Mockingjay: The Final Book of The Hunger Games', libraryID: 3245 }
];
library.sort((a, b) => a.libraryID - b.libraryID);
console.log(library);
//22. Genera 6 números aleatoris enters entre 0 i 10 i desa'ls en un array
console.log("---- Exercici 22 ----");
const numAleatoriEnter = [];
for (let i = 0; i < 7; i++) {
    numAleatoriEnter[i] = Math.floor(Math.random() * 10);
};
console.log(numAleatoriEnter);
//23. Troba els valors màxim i mínim de l'array del punt anterior
console.log("---- Exercici 23 ----");
let valmax = 0;
let valmin = 10; //Si comença amb 0, mai sera diferent despres
for (let valor of numAleatoriEnter) {
    if (valor > valmax) {
        valmax = valor
    };
    if (valor < valmin) {
        valmin = valor
    };
};
console.log("Valor maxim del array: " + valmax)
console.log("Valor minim del array: " + valmin)
//24. Crea un script que retorni un array d'enters entre 1 i 10 aleatoris sense que es repeteixi cap número.
//Mostra el nombre d'iteracions que es realitzen
console.log("---- Exercici 24 ----");
let iteracions = 0;
const numAleatoriFins10 = [];
while (numAleatoriFins10.length != 10) {
    let numero = Math.floor(Math.random() * 10);
    //si numero no esta en el array, añadirlo (dos bucles?)
    let existeix = false;
    for (let index of numAleatoriFins10) {
        if (numero == index) {
            existeix = true;
        }
    }
    if (!existeix) {
        numAleatoriFins10.push(numero)
    }
    iteracions++; //lo normal son 20-25 iteracions
};
console.log("Array aleatori sense repetir: " + numAleatoriFins10)
console.log("Numero d'iteracions: " + iteracions)
console.log("---- Exercici Finalitzat ----");