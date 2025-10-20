//1. Crea un script que comprovi si una variable és del tipus Number, en cas afirmatiu s'ha d'arrodonir a 2
//decimals i mostrar-la per la consola, en cas contrari mostrar el tipus per la consola

let variable = 3.14159;

if (typeof variable === 'number') {
    console.log(variable.toFixed(2));
} else {
    console.log(typeof variable);
}

/*2. Donat un Array d'Strings:
const title = ['La casa de paper', 'La catedral del mar', 'Pa
negre', 'Polseres vermelles'];
1. Canvia els espais en blanc per -
2. Converteix cada element a LowerCase
*/

const title = ['La casa de paper', 'La catedral del mar', 'Panegre', 'Polseres vermelles'];

const senseEspais = [];

for (let i = 0; i < title.length; i++) {
    title[i] = title[i].toLowerCase();
    title[i] = title[i].replaceAll(' ', '-');
    senseEspais.push(title[i]);
}

console.log(senseEspais);

/*3. Suma tots el valors numèrics d'un array
const arrSuma = [3, false, 7, 'Maria', 9]*/

const arrSuma = [3, false, 7, 'Maria', 9];
let suma = 0;

for (let i = 0; i < arrSuma.length; i++) {
    if (typeof arrSuma[i] === 'number') {
        suma += arrSuma[i];
    }
}

console.log(suma);

/*4. Comprova si un string està buit o no. Comprova si un string és null o undefined*/

let str1 = null;


if(typeof(str1)=== "string"){
    console.log("Es un string")
}else if(typeof(str1)==="undefined"){
    console.log("No esta definit")
}else{ 
    console.log("Es null")
}

//5. Desa les paraules d'un string cadascuna en una posició d'un array
const str2 = 'Desenvolupament web en entorn client'
const array2 = str2.split(' ');
console.log(array2);

//6. Compta les aparicions d'una subcadena en una cadena
const str3 = 'Lorem ipsum dolor sit amet, consectetur adipiscing, elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua'
const element = "do"
const separat = str3.split(" ");
let contador = 0;

for (let i =0; i<separat.length; i++){
    if (separat[i] === element){
        contador = contador+1;
    }
}
console.log(contador);

//7. Escriu un script per obtenir una part d'una cadena després d'un caràcter especificat
const caracter = ",";
const [principi,...resto] = str3.split(caracter);
console.log(resto.join(caracter));

//8. Crea una funció per comprovar si una cadena acaba amb el sufix especificat
const cadena = "Prova de cadena";
const sufix = "cadena";



function final(cadena, sufix) {
  if (cadena.endsWith(sufix)){
    return true;
  }else{
    return false;
  }
}

const resultat = final(cadena, sufix);
console.log(resultat);

//9. Crea un script per fusionar dos arrays
const arr1 = [1, 2, 3];
const arr2=[4,5,6];

const fusio = arr1.concat(arr2);
console.log(fusio);

//10. Converteix la data actual al següent format: '9/6/2022, 17:46:49' de la manera més concisa possible
const data = new Date();
const text = data.getDate()+"/"+data.getMonth()+"/"+data.getFullYear() +", "+data.getHours()+":"+data.getMinutes()+":"+data.getSeconds();
console.log(text);

//11. Crea un script per comparar dues dates. En el cas de comparar dues dates iguals s'ha d'utilitzar l'operador '==='
const data1 = new Date("2022, 5, 9");
const data2 = new Date("2022, 5, 9");

if (data1.getTime()===data2.getTime()){
    console.log("Són iguals");
}else{
    console.log("No són iguals");
}

//12. Crea un script que mostri els dies que han passat des de l'inici d'any
const data3 = new Date("2022, 1, 1");
const data4 = new Date("2022, 5, 9");

const millis1 = data4 - data3;
const dies = millis1 /86400000;

console.log(dies);

//13. Crea un script que retorni la data actual amb el següent format
const data5 = Date.now();
const aviu = Date(data5);

console.log(aviu.getFullYear());



