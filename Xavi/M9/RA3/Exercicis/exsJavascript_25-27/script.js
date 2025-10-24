//Exercici 25

/*
25. Crea un array bidimensional 3x3 i emplena'l amb números aleatoris des de l'1 al 29 sense repetits.
Fes-ho de manera que l'script funcioni per a qualsevol array bidimensional, per exemple: 2x3. 4x4,
5x2, etc. sense fer cap modificació
*/

//Solucio 25

function OmplArr(arr) {
    const allValues = [];
    for (let i = 0; i < arr.length; i++) {
        for (let j = 0; j < arr[i].length;) {
            const random = Math.floor(Math.random() * 29) + 1;
            if (!allValues.includes(random)) {
                arr[i][j] = random;
                allValues.push(random);
                j++;
            }
        }
    }

    return arr;
}

arr = [[undefined, undefined, undefined],
[undefined, undefined, undefined],
[undefined, undefined, undefined]];

console.log(OmplArr(arr));




//Exercici 26

/*
26. A l'array anterior, fes que:
1. La primera columna contingui els números entre 1 i 9
2. La segona columna contingui els números entre 10 i 19
3. La tercera columna contingui els números entre 20 i 29
*/

//Solucio 26

let arr2 = [[], [], []];

const allValues = [];
for (let i = 0; i < 3; i++) {
    for (let j = 0; j < 9;) {
        const random = Math.floor(Math.random() * 9) + 1 + 10 * i;
        if (!allValues.includes(random)) {
            arr2[i][j] = random;
            allValues.push(random);
            j++;
        }
    }
}

console.log(arr2);




//Exercici 27

/*
27. A l'array anterior, fes que:
1. La primera columna sigui amb ordre ascendent
2. La segona columna sigui amb ordre descendent
3. La tercera columna sigui amb ordre ascendent
*/

arr2[0].sort((a, b) => a - b);
arr2[1].sort((a, b) => b - a);
arr2[2].sort((a, b) => a - b);

console.log(arr2)