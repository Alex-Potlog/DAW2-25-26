/*1. Crea un script que comprovi si una variable és del tipus Number, en cas afirmatiu s'ha d'arrodonir a 2
decimals i mostrar-la per la consola, en cas contrari mostrar el tipus per la consola*/
console.log("---- Exercici 1 ----");
const variable1 = 34.666666666666;
if (typeof variable1 === 'number') {
    console.log(variable1.toFixed(2));
} else {
    console.log("No es un numero");
}

/*
2. Donat un Array d'Strings:
    const title = ['La casa de paper', 'La catedral del mar', 'Pa negre', 'Polseres vermelles'];
    2.1. Canvia els espais en blanc per -
    2.2. Converteix cada element a LowerCase
3. Suma tots el valors numèrics d'un array
    const arrSuma = [3, false, 7, 'Maria', 9]
4. Comprova si un string està buit o no. Comprova si un string és null o undefined
5. Desa les paraules d'un string cadascuna en una posició d'un array
const str2 = 'Desenvolupament web en entorn client'
6. Compta les aparicions d'una subcadena en una cadena
const str3 = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua'
7. Escriu un script per obtenir una part d'una cadena després d'un caràcter especificat
8. Crea una funció per comprovar si una cadena acaba amb el sufix especificat */