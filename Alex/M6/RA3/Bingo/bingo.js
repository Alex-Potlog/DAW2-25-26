function creaTargeta() {
    const bingo = document.querySelector(".bingo-card");
    for (let i = 0; i < 9; i++) {
        let columna = document.createElement('div');
        columna.className = 'columna';

        const cell1 = document.createElement("div");
        cell1.className = "cell";
        const num1 = Math.floor(Math.random() * 7) + 3;
        cell1.textContent = num1 + (10 * i);
        columna.append(cell1);

        const cell2 = document.createElement("div");
        cell2.className = "cell";
        const num2 = Math.floor(Math.random() * (num1 - 2)) + 2;
        cell2.textContent = num2 + (10 * i);
        columna.append(cell2);

        const cell3 = document.createElement("div");
        cell3.className = "cell";
        const num3 = Math.floor(Math.random() * (num2 - 1)) + 1;
        cell3.textContent = num3 + (10 * i);
        columna.append(cell3);

        if (i % 2 === 0) {
            columna.style.flexDirection = "column-reverse";
        }
        bingo.appendChild(columna);
    }

    let columnes = bingo.getElementsByClassName('columna');
    let fila1 = [], fila2 = [], fila3 = [];
    for (const element of columnes) {
        if (element.style.flexDirection == "column-reverse") {
            fila3.push(element.children[0]);
            fila1.push(element.children[2]);
        } else {
            fila1.push(element.children[0]);
            fila3.push(element.children[2]);
        }
        fila2.push(element.children[1]);
    }

    let posicionsBlanques1 = new Set(afegeixNegre(fila1));
    let posicionsBlanques2 = new Set(afegeixNegre(fila2));

    let sonIguals = JSON.stringify([...posicionsBlanques1].sort()) === JSON.stringify([...posicionsBlanques2].sort());

    if (sonIguals) {
        for (const element of columnes) {
            if (element.children[1].className === "cell black") {
                element.children[1].className = "cell";
                let nuevaPosicionNegra = [...posicionsBlanques2][0];
                columnes[nuevaPosicionNegra].children[1].className = "cell black";
                columnes[nuevaPosicionNegra].children[1].textContent = "";
                break;
            }
        }
    }

    let todasPosiciones = [0, 1, 2, 3, 4, 5, 6, 7, 8];
    let posicionesNegras1 = todasPosiciones.filter(pos => !posicionsBlanques1.has(pos));
    let posicionesNegras2 = todasPosiciones.filter(pos => !posicionsBlanques2.has(pos));

    let iguals = [...posicionsBlanques1].filter(pos => posicionsBlanques2.has(pos));
    let ambdos = posicionesNegras1.filter(pos => posicionesNegras2.includes(pos));

    console.log("Posiciones negras en ambas filas:", iguals)
    console.log("Posiciones blancas en ambas filas:", ambdos)

    afegirNegreFila3(fila3, iguals, ambdos)
}

window.addEventListener('DOMContentLoaded', creaTargeta);

function afegeixNegre(fila) {
    let negres = [];
    let disponibles = [0, 1, 2, 3, 4, 5, 6, 7, 8];

    for (let i = 0; i < 4; i++) {
        let index = Math.floor(Math.random() * disponibles.length);
        negres[i] = disponibles[index];
        disponibles.splice(index, 1);
    }

    negres.sort((a, b) => b - a);

    for (let i = 0; i < 4; i++) {
        fila[negres[i]].className = "cell black";
        fila[negres[i]].textContent = "";
        fila.splice(negres[i], 1);
    }

    return disponibles;
}
// 0,1,2,3,4,5,6,7,8
function afegirNegreFila3(fila3, iguals, ambdos) {
    let disponibles = [];
    let negres = [];

    console.log("iguals type:", typeof iguals);
    console.log("iguals content:", iguals);

    for (let i = 0; i < 9; i++) {
        if (iguals.includes(i)) {
            fila3[i].className = "cell black";
            fila3[i].textContent = "";
        } else if (!ambdos.includes(i)) {
            disponibles.push(i);
        }
    }

    for (let i = 0; i < 4 - iguals.length; i++) {
        let posicioEscollida = Math.floor(Math.random() * disponibles.length);
        negres[i] = disponibles[posicioEscollida]
        disponibles.splice(posicioEscollida, 1);
    }

    for (const element of negres) {
        fila3[element].className = "cell black"
        fila3[element].textContent = ""
        fila3.splice(element, 1);
    }

    console.log("disponibles:", disponibles);
}

function reiniciaTargeta() {
    const bingo = document.body.querySelector(".bingo-card");
    const tirades = document.body.querySelector(".tirades");
    numsBingoDisponibles = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89]
    bingo.innerHTML = "";
    tirades.innerHTML = "";
    creaTargeta();
}

let numsBingoDisponibles = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89]

function tiraNumero() {
    let numEscollit;
    if (numsBingoDisponibles.length != 0) {
        const posicioEscollida = Math.floor(Math.random() * numsBingoDisponibles.length);
        numEscollit = numsBingoDisponibles[posicioEscollida]
        const contenidor = document.querySelector(".tirades");
        const numero = document.createElement('div')
        numero.className = "tirada"
        numero.textContent = numEscollit;
        contenidor.appendChild(numero);
        numsBingoDisponibles.splice(posicioEscollida, 1);
        const caselles = document.querySelectorAll(".cell");
        for (const element of caselles) {
            if (element.textContent == numEscollit) {
                console.log("Numero coincident!")
                element.classList.add("green");
            }
        }
    }
}