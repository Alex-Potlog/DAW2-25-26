/*1. Crea un script que comprovi si una variable és del tipus Number, en cas afirmatiu s'ha d'arrodonir a 2
decimals i mostrar-la per la consola, en cas contrari mostrar el tipus per la consola */
const forma = "redonda";
const tamano = 1.3491;

console.log(typeof forma);
console.log(typeof tamano);

if (typeof tamano === "number") {
    console.log(tamano.toFixed(2))
}

/*2. Donat un Array d'Strings:
const title = ['La casa de paper', 'La catedral del mar', 'Pa negre', 'Polseres vermelles'];
    1. Canvia els espais en blanc per -
    2. Converteix cada element a LowerCase */
const title = ['La casa de paper', 'La catedral del mar', 'Pa negre', 'Polseres vermelles'];

/*map() recorre cada element de l'array i retorna un nou array amb els valors transformats */
const title2 = title.map(t => t.replaceAll(' ', '-')); /*t és el nom que li donem a cada element mentre el processem */

const title3 = title2.map(l => l.toLowerCase());
console.log(title3);

/*3. Suma tots el valors numèrics d'un array
const arrSuma = [3, false, 7, 'Maria', 9] */

const arrSuma = [3, false, 7, 'Maria', 9];

num = 0;

for (const i in arrSuma) {
    if (typeof arrSuma[i] === "number") {
        num += arrSuma[i];
    }
}

console.log(num)

/*4. Comprova si un string està buit o no. Comprova si un string és null o undefined */
//let cadena;
const cadena = "";

if (typeof cadena === "undefined") {
    console.log("String no definit");
} else if (typeof cadena === "string" && cadena.length === 0) {
    console.log("String buit");
} else if (cadena === null) {
    console.log("String null");
} else {
    console.log("String no està buit, no és null");
}

/*5. Desa les paraules d'un string cadascuna en una posició d'un array
const str2 = 'Desenvolupament web en entorn client' */
const str2 = 'Desenvolupament web en entorn client';

const arrSTR = str2.split(" ");

console.log(arrSTR);

/*6 Compta les aparicions d'una subcadena en una cadena
const str3 = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua'*/
const str3 = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua';
const subcadena = 'i';
let contador = 0;

for (let i = 0; i < str3.length; i++) {
    const str4 = str3.toLowerCase();
    if (subcadena == str4[i]) {
        contador++;
    }
}

console.log("La subcadena '" + subcadena + "' a aparegut " + contador + " cops");

/*7.Escriu un script per obtenir una part d'una cadena després d'un caràcter especificat */
const phrase = "a) M61-JavaScript";

const index = phrase.indexOf(")");
const indexSub = phrase.substring(index + 1);
const index2 = phrase.indexOf("-");
const index2Sub = phrase.substring(index2 + 1);

console.log(indexSub);
console.log(index2Sub);

/*8.Crea una funció per comprovar si una cadena acaba amb el sufix especificat */
function myFunc(thePhrase) {
    const suf = thePhrase.substring(thePhrase.length - 3);
    if (suf === "abc") {
        return ("La frase SI acaba amb abc");
    } else {
        return ("La frase NO acaba amb abc");
    }
}

const phraseSTR = "Hola mundo";

console.log(phraseSTR);
myFunc(phraseSTR);
console.log(myFunc(phraseSTR));