//Exercici 18

/*
18. Crea un script per clonar un array

Què ocorre si es fa assignant-lo mitjançant l'operador "=".

const arr1 = [1,3,5]
const arr2 = arr1;

Si és un array multidimensional com afecta la clonació.

const arr1 = [1,[a,b,c],5]

Descriu com treballes els mètodes utilitzats per clonar arrays multidimensionals.
*/

//Solucio 18

/*
function clonArray(arr) {
    const arrClon = [];
    for (let i = 0; i < arr.length; i++) {
        if (Array.isArray(arr[i])) {
            arrClon[i] = clonArray(arr[i]);
        } else {
            arrClon[i] = arr[i];
        }
    }
    return arrClon;
}
*/ //funcio alternativa

function clonArray(arr) {
    return arr.map(el => Array.isArray(el) ? clonArray(el) : el);
}

let arr1 = [1, 3, 5];

console.log(clonArray(arr1));

const a = 0, b = 0, c = 0;

arr1 = [1, [a, b, c], 5];

console.log(clonArray(arr1));

/*
Si per fer una clonació d'un array assignes la copia amb "arr1=arr2" no estas creant una copia,
ja que els dos arrays apunten al mateix espai en la memoria per tant si canvies un array el altre també canvia.
La manera correcta seria per exemple: arr1 = [...arr2]
D'aquesta manera es fa una copia de cada element de l'array i es transporta a l'altre array.
En el cas de un array multidimensional hauriem de utilitzar una funcio recursiva com he utilitzat per resoldre l'exercici,
ja que si ho fas aixi "arr1 = [...arr2]" estarias creant una copia superficial que no clonaria els elements que son arrays
sino que apuntarien al mateix espai en la memoria
*/



//Exercici 19

/*
19. Crea un script per ordenar pel valor numèric els elements d'un array de manera ascendent
*/

//Solucio 19

let numeros = [15, 3, 27, 8, 2, 19];

numeros.sort((a, b) => a - b);

console.log(numeros);



//Exercici 20

/*
20. Crea una funció per desordenar un array numèric
*/

//Solucio 20

function desordenaArray(arr) {
    const copia = [...arr];
    for (let i = copia.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [copia[i], copia[j]] = [copia[j], copia[i]];
    }
    return copia;
}

numeros = [1, 2, 3, 4, 5, 6];
console.log(desordenaArray(numeros));



//Exercici 21

/*
21. Escriu una funció per ordenar el següent array d'objectes pel valor del libraryID

 const library = [
 { author: 'Bill Gates', title: 'The Road Ahead', libraryID: 1254},
 { author: 'Steve Jobs', title: 'Walter Isaacson', libraryID: 4264},
 { author: 'Suzanne Collins', title: 'Mockingjay: The Final Book of The
Hunger Games', libraryID: 3245}
 ];
*/

const library = [
    { author: 'Bill Gates', title: 'The Road Ahead', libraryID: 1254 },
    { author: 'Steve Jobs', title: 'Walter Isaacson', libraryID: 4264 },
    { author: 'Suzanne Collins', title: 'Mockingjay: The Final Book of The Hunger Games', libraryID: 3245 }
];

console.log([...library].sort((a, b) => a.libraryID - b.libraryID));

//Exercici 22

/*
22. Genera 6 números aleatoris enters entre 0 i 10 i desa'ls en un array
*/

//Solucio 22

let arr = [];

for (let i = 0; i < 6; i++) {
    arr[i] = Math.floor(Math.random() * 11);
}

console.log(arr);



//Exercici 23

/*
23. Troba els valors màxim i mínim de l'array del punt anterior
*/

//Solucio 23

console.log("Màxim: ", Math.max(...arr));
console.log("Minim: ", Math.min(...arr));

let min = 10;
let max = 0;

for (let i = 0; i < arr.length; i++) {
    if (arr[i] < min) min = arr[i];
    if (arr[i] > max) max = arr[i];
}

console.log("Màxim: ", max);
console.log("Minim: ", min);




//Exercici 24

/*
24. Crea un script que retorni un array d'enters entre 1 i 10 aleatoris sense que es repeteixi cap número.
Mostra el nombre d'iteracions que es realitzen
*/

//Solucio 24

arr = [];
let nIter = 0;

while (arr.length < 10) {
    const num = Math.floor(Math.random() * 10) + 1;

    if (!arr.includes(num)) {
        arr.push(num);
    }
    nIter++;
}

console.log(arr);
console.log("Iteracions: ", nIter);
