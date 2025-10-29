const myObj = {
    "Nombre": "Juan",
    "Apellido": "Alberto"
};

const objetoStringificado = JSON.stringify(myObj);
localStorage.setItem("Mi objeto", objetoStringificado)