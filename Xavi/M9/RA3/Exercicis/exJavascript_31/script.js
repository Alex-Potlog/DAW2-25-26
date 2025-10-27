//Exercici 31

/*
31. Crea un qüestionari amb els elements que s'indiquen en la imatge següent:
Crea un script que desi els valors dels diferents camps quan s'introdueixin o hagi un canvi, de
manera que si es tanca la finestra del navegador, quan es torni a obrir recuperi els valors
introduïts fins el moment.
El botó Reseteja ha d'eliminar les dades emmagatzemades.
*/

//Solucio 31

const camps = ["nom", "cognom", "email", "adreca"];

window.addEventListener("load", () => {
    camps.forEach(camp => {
        const dada = localStorage.getItem(camp);
        if (dada) document.getElementById(camp).value = dada;
    })
})


camps.forEach(camp => {
    document.getElementById(camp).addEventListener("input", e => {
        localStorage.setItem(camp, e.target.value);
    })
})

document.getElementById("reseteja").addEventListener("click", () => {
    camps.forEach(camp => {
        localStorage.removeItem(camp);
        document.getElementById(camp).value = "";
    })
})
