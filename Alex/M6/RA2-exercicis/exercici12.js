const data = new Date();
const iniciAny = new Date(data.getFullYear(), 0, 1);
const diff = data - iniciAny;
const unDia = 1000 * 60 * 60 * 24;
const diaAny = Math.ceil(diff / unDia);
console.log(`Avui és el dia ${diaAny} de l'any.`);