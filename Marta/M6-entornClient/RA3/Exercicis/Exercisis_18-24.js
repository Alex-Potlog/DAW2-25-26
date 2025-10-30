//Exercici 18: Crea un script per clonar un array
// const array2= [...array1] ->per clonar?
const arr1 = [1, 3, 5];

const arr2 = [...arr1];

console.log(arr1);
console.log(arr2);

// json.stringify() // per recuperar utilitzo json.parse //
const arr3 = [1, ['a', 'b', 'c'], 5]
const arr4 = JSON.stringify(arr3);
const obj = JSON.parse(arr4);
console.log(arr4);
console.log(obj);

//Exercici 19
// per ordenar tenim el mètode sort(), hem de tenir en compte que ordena per codi asci. Per ordenar per valor numeric he de fer una funció
/* number.sort(function (a, b){
    return a - b
});
console.log(number) */

const numbers = [5, 2, 15, 4, 6, 1, 17, 3, 7];

numbers.sort(function (a, b) {
  return a - b;
});

console.log(numbers);

//Exercici 20
function desorden(array) {
  array = array.sort(function () { return Math.random() - 0.5 })
  return array;
}// Aquesta funció em desordena un array

const numsOrdre = [1, 2, 3, 4, 5, 6, 7, 8, 9];

const numsDesordre = [];

for (let i = 0; i < 1; i++) {
  numsDesordre[i] = desorden(numsOrdre);
} //creo bucle per omplir array buit

console.log(numsDesordre);

//Exercici 21
//A la funcio de comparacio del sort he de tenir en compte el camp "libraryID"
function ordenat(arrayL) {
  arrayL = arrayL.sort(function (a, b) {
    if (a.libraryID > b.libraryID) {
      return 1;
    }
    if (a.libraryID < b.libraryID) {
      return -1;
    }
    return 0;
  });

  return arrayL
}

const library = [
  { author: 'Bill Gates', title: 'The Road Ahead', libraryID: 1254 },
  { author: 'Steve Jobs', title: 'Walter Isaacson', libraryID: 4264 },
  { author: 'Suzanne Collins', title: 'Mockingjay: The Final Book of The Hunger Games', libraryID: 3245 }
];

const libOrder = ordenat(library);

console.log(libOrder);

//Exercici 22
//Es fa servir el math.random() (i multiplicar per 10) i arrodonir amb el math.floor, math.round o math.ceil.
function aleatoris(final) {
  for (let i = 0; i < 6; i++) {
    const numAl = Math.round(Math.random(0, 10) * 10);
    final[i] = numAl;
  }

  return final;
}

const arrAleatoris = [];

const final = aleatoris(arrAleatoris);

console.log(final);

//Exercici 23
const min = Math.min(...arrAleatoris);
const max = Math.max(...arrAleatoris);

console.log("Minim: " + min + "; Màxim: " + max)

//Exercici 24
function aleatoris2() {

  const arrAleatoris2 = [];
  let iteracions = 0;

  while (arrAleatoris2.length < 10) {
    iteracions++;
    const numAl = Math.round(Math.random(0, 10) * 10);

    if (!arrAleatoris2.includes(numAl)) {
      arrAleatoris2.push(numAl);
    }
  }

  return { array: arrAleatoris2, Iteracions: iteracions };
}

const final2 = aleatoris2();

console.log("Array: " + final2.array + "; Iteracions: " + final2.Iteracions);
