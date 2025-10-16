
//1. Crea un script que comprovi si una variable és del tipus Number, en cas afirmatiu s'ha d'arrodonir a 2
//decimals i mostrar-la per la consola, en cas contrari mostrar el tipus per la consola
let num = 84.56
//num = 'Hola'
if (typeof num === 'number') {
  console.log(num.toFixed(2))
} else {
  console.log(typeof num)
}

//2
const title = ['La casa de paper', 'La catedral del mar', 'Pa negre', 'Polseres vermelles'];
// Canvia els espais en blanc per -
for (let i = 0; i < title.length; i++) {
  title[i] = title[i].replace(/ /g, '-')
  title[i] = title[i].toLowerCase()
}

console.log(title)
//3
//suma tots els valors numerics d'un array
const valors = [1, 'Hola', 2, 3, 'Adéu', 4, 5, true, false, 6];
let suma = 0
valors.forEach(element => {
  if (typeof element === 'number') {
    suma += element
  }
});
console.log(suma)

//4