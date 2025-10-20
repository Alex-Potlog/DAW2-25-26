//18. Crea un script per clonar un array
const arr1 = [1,3,5];
const arr2= Array.from(arr1);

console.log(arr2);

const arr3 = [1,["a","b","c"],5];
const arr4= Array.from(arr3);

console.log(arr4);


//19. Crea un script per ordenar pel valor numèric els elements d'un array de manera ascendent
let arrNum = [5, 3, 8, 1, 4];
arrNum = [...arrNum.sort()];
console.log(arrNum);

//20. Crea una funció per desordenar un array numèric
function desordenar(array){
    const arrtemp = [...array].sort(() => Math.random() - 0.5);//Es 0.5 a-0.5 perque el sort funciona en si es negatiu ordena d'una forma i si es positiu d'una altra
    return arrtemp;
}

const arr_resultat=[...desordenar(arrNum)]
console.log(arr_resultat)

//21. Escriu una funció per ordenar el següent array d'objectes pel valor del libraryID
const library = [
{ author: 'Bill Gates', title: 'The Road Ahead', libraryID: 1254},
{ author: 'Steve Jobs', title: 'Walter Isaacson', libraryID: 4264},
{ author: 'Suzanne Collins', title: 'Mockingjay: The Final Book of TheHunger Games', libraryID: 3245}
];

function ordenar2(array){
    
}