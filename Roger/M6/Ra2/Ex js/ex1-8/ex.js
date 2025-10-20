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