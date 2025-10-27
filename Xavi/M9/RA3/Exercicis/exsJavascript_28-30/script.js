//Exercici 28

/*
28. Realitza un script amb funcionalitat de calculadora. Utilitza un formulari com es mostra en la següent
imatge. Operacions: suma, resta, multiplicació, divisió i potència.
El resultat s’ha de mostrar amb dos decimals.
El separador decimal és el punt (.), si s’introdueix una coma (,) s’ha de substituir.
Si en el càlcul es produeix un error NaN o Infinity s’ha de mostrar de color vermell
En el cas de l'operació de potència (^) si el segon operador és un número decimal.
S'ha de truncar i mostrar el nou valor en el camp del segon operand
*/

//Solucio 28

function calcula() {
    const op1 = Number.parseFloat(document.querySelector(".op1").value.replace(",", "."));
    const operador = document.getElementById("operations").value;
    const op2 = Number.parseFloat(document.querySelector(".op2").value.replace(",", "."));
    const res = document.querySelector(".res");
    let total;

    if (isNaN(op1) || isNaN(op2)) {
        res.value = "Error: NaN";
        res.classList.add("error");
        return;
    }

    switch (operador) {
        case '+':
            total = op1 + op2;
            break;
        case '-':
            total = op1 - op2;
            break;
        case '*':
            total = op1 * op2;
            break;
        case '/':
            total = op2 !== 0 ? op1 / op2 : NaN;;
            break;
        case '^':
            total = Math.pow(op1, Math.floor(op2));
            document.querySelector(".op2").value = Math.floor(op2);
            break;
    }
    if (isNaN(total)) {
        res.value = "Error : Infinity";
        res.classList.add("error");
    } else {
        res.value = total.toFixed(2);
        res.classList.remove("error");

    }
}

//Exercici 29

/*
29. Crea un formulari amb un camp de text.
Introdueix una adreça de correu electrònic i crea un script per mostrar: (2 punts)
La longitud del substring que identifica a l’usuari.
El TLD (com, es, cat, etc.)
L’adreça amb el domini canviat a thosicodina però conservant el TLD.
1. Donat el següent array d’emails.
 const email = [
 "p.escosa@gmail.com",
 "j.garcia@info.yahoo.es",
 "r.esteban@sales.gmail.com",
 "a.gomez@gmail.es",
 "l.mesa@gmail.com",
 "t.sants@hotmail.es",
 "v.ros@hotmail.com"
 ]
Mostra per pantalla el llistat dels email que tenen:
Com a domini gmail i TLD .com
Com a TLD .es
2. Mostra el subdomini dels emails que en tenen.
*/

//Solucio 29

const email = [
    "p.escosa@gmail.com",
    "j.garcia@info.yahoo.es",
    "r.esteban@sales.gmail.com",
    "a.gomez@gmail.es",
    "l.mesa@gmail.com",
    "t.sants@hotmail.es",
    "v.ros@hotmail.com"
]

function getElementsMail(string) {
    let arr = string.split("@");
    let user = arr[0];

    let dominiComp = arr[1];
    let arr2 = dominiComp.split(".");
    let domini = null;
    let subdomini = null;
    let tld = null;
    if (arr2.length == 2) {
        domini = arr2[0];
        tld = arr2[1];
    } else if (arr2.length == 3) {
        subdomini = arr2[0];
        domini = arr2[1];
        tld = arr2[2];
    }

    return [user, subdomini, domini, tld, dominiComp];
}

function executa() {
    let newMail = document.querySelector(".newMail").value;
    email.push(newMail);

    arr = getElementsMail(newMail);

    let user = arr[0];
    let tld = arr[3];



    document.querySelector(".lonUs").textContent = user.length;


    document.querySelector(".tld").textContent = tld;

    nouDom = user + "@thosicodina." + tld;

    document.querySelector(".domTho").textContent = nouDom;

}

let ulGmail = document.querySelector(".gmail");
let ulEs = document.querySelector(".es");

function filtra() {

    ulGmail.innerHTML = "";
    ulEs.innerHTML = "";

    for (let i = 0; i < email.length; i++) {
        arr = getElementsMail(email[i]);

        let domini = arr[2] + arr[3];
        let tld = arr[3];



        if (domini == "gmailcom") {
            let li = document.createElement("li");
            li.textContent = email[i];
            ulGmail.appendChild(li);
        }

        if (tld == "es") {
            let li = document.createElement("li");
            li.textContent = email[i];
            ulEs.appendChild(li);
        }
    }

}

function reset() {
    ulGmail.innerHTML = "";
    ulEs.innerHTML = "";
}




let ulSubdo = document.querySelector(".subDo");

for (let i = 0; i < email.length; i++) {
    arr = getElementsMail(email[i]);

    let subdomini = arr[1];

    if (subdomini !== null) {
        let li = document.createElement("li");
        li.textContent = email[i];
        ulSubdo.appendChild(li);
    }
}



//Exercici 30

/*
30. Realitza un script que mostri la data i l’hora actual amb precisió de segon amb diferents formats.
Format 1:
El dia i mes de la data i tots els camps de l’hora han de tenir dos dígits
Format 2:
Tots els camps de l’hora han de tenir dos dígits
Quan es faci dobleclick damunt de la data s’ha de canviar d’un format a l’altre
*/

//Solucio 30

let fecha = document.querySelector(".fecha");
let cont = false;

function canviFormatFecha() {
    let now = new Date()

    let dia = String(now.getDate()).padStart(2, '0');
    let any = now.getFullYear();

    let hora = String(now.getHours()).padStart(2, '0');
    let minuts = String(now.getMinutes()).padStart(2, '0');
    let segons = String(now.getSeconds()).padStart(2, '0');

    if (cont) {
        let arr = now.toString().split(" ");

        let diaSem = arr[0];
        let nomMes = arr[1];

        fecha.textContent = `${diaSem} ${dia} ${nomMes} ${any} ${hora}:${minuts}:${segons}`;

        cont = false;
    } else {
        let mes = String(now.getMonth() + 1).padStart(2, '0');

        fecha.textContent = `${dia}-${mes}-${any} ${hora}:${minuts}:${segons}`;

        cont = true;
    }

}

fecha.addEventListener("dblclick", function (e) {
    canviFormatFecha();
});

canviFormatFecha();