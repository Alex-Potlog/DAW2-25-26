//Exercici 25
function arrayBidi(filas, columnas, valorMin, valorMax, arrayB) {
    const nums = [];

    for (let i = valorMin; i <=valorMax; i++) {
        const k= Math.floor(Math.random() * (valorMax - valorMin + 1)) + valorMin
        if (!nums.includes(k)) {
            nums.push(k);
        }
    }

    let index=0;
    for (let i=0; i<filas; i++){
        arrayB[i]=[];
        for (let j=0; j<columnas; j++){
            arrayB[i][j]=nums[index];
            index++;
        }
    }
    return arrayB;
}

const filas = 3;
const columnas = 3;
const valorMin = 1;
const valorMax = 29;
const arrayB=[];

const resultat = arrayBidi(filas, columnas, valorMin, valorMax, arrayB);

console.log(resultat);

//Exercici 26
function arrayBiNums(array){
    const col0=[];
    for (let i=0; i<=2; i++){
        let p;
        do{
            p=Math.floor(Math.random() *9 ) + 1;
        }while (col0.includes(p));
        
        col0.push(p);

        array[i][0]=p;
    }

    const col1=[];
    for (let i=0; i<=2; i++){
        let s;

        do{
            s=Math.floor(Math.random() * 10) + 10;
        } while (col1.includes(s));
        
        col1.push(s);

        array[i][1]=s;
    }

    const col2=[];
    for (let i=0; i<=2; i++){
        let t;

        do{
            t=Math.floor(Math.random() * 10) + 20;
        }while(col2.includes(t));

        col2.push(t);

        array[i][2]=t;
    }

    return array;
}

const numsPerColumna=arrayBiNums(arrayB);

console.log(numsPerColumna);

//Exercici 27

function ordenar (arrayB){
    const col0=[];
    //For per generar els numeros que necessito
    for (let i=0; i<=2; i++){
        let p;
        do{
            p=Math.floor(Math.random() *9 ) + 1;
        }while (col0.includes(p));
        
        col0.push(p);
        
    }
    //Fora del bucle ordenem l'array per complet de forma ascenent
    col0.sort((a,b) => a-b);
    
    //Tornem a fer un bucle per assignar els valors ordenats a l'array anterior a
    //la columna 0 i que corri per les diferents files.
    for (let i=0; i<=2; i++){
        arrayB[i][0]= col0[i];
    }
    //----------------------------------------------------------------------------
    const col1=[];
    for (let i=0; i<=2; i++){
        let s;

        do{
            s=Math.floor(Math.random() * 10) + 10;
        } while (col1.includes(s));
        
        col1.push(s);
    }

    col1.sort((a,b)=> b-a);

    for (let i=0; i<=2; i++){
        arrayB[i][1]=col1[i];
    }
    //----------------------------------------------------------------------------
    const col2=[];
    for (let i=0; i<=2; i++){
        let t;

        do{
            t=Math.floor(Math.random() * 10) + 20;
        }while(col2.includes(t));

        col2.push(t);
    }

    col2.sort((a,b)=>a-b)
    for (let i=0; i<=2; i++){
        arrayB[i][2]=col2[i];
    }

    return arrayB;
}


const ordena=ordenar(arrayB);

console.log(ordena);