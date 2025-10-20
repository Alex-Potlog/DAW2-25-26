// Què ocorre si es fa assignant-lo mitjançant l'operador "="

// L'array no es clona, el segon array serà un punter a l'altre array

let arr1 = [1, 3, 5];

let arr2 = clonaUni(arr1);

function clonaUni(arr1) {
    let arr2 = [];
    if (Array.isArray(arr1)) {
        for (let i = 0; i < arr1.length; i++) {
            arr2.push(arr1[i]);
        }
        return arr2;
    }
    return arr2;
}

arr1.push("23");

console.log(arr2)

// La clonació és idèntica

