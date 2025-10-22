const objecteRandom = {
    "nom": "Si",
    "descripcio": "De vegades",
    "posibilitattsssss": "El bicho"
};

const myJSON = JSON.stringify(objecteRandom);
localStorage.setItem("Mi objeto", myJSON);

const provaRecuperada = JSON.parse(localStorage.getItem("Mi objeto"));
console.log(provaRecuperada)