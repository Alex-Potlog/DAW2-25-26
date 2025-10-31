let tiempo= new Date();

const dia=tiempo.getDate();
const mes=tiempo.getMonth();
const ano=tiempo.getFullYear();

const hora=tiempo.getHours();
const min=tiempo.getMinutes();
const seg=tiempo.getSeconds();

const localSTR=tiempo.toLocaleString();

const localDate=tiempo.toLocaleDateString();

const dateLetra=tiempo.toDateString();

console.log(tiempo);
console.log(dia);
console.log(mes);
console.log(ano);
console.log(hora);
console.log(min);
console.log(seg);
console.log(localSTR);
console.log(localDate);
console.log(dateLetra);