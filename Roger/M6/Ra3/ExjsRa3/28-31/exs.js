// 28. Realitza un script amb funcionalitat de calculadora. Utilitza un formulari com es mostra en la següent
// imatge. Operacions: suma, resta, multiplicació, divisió i potència.
// El resultat s’ha de mostrar amb dos decimals.
// El separador decimal és el punt (.), si s’introdueix una coma (,) s’ha de substituir.
// Si en el càlcul es produeix un error NaN o Infinity s’ha de mostrar de color vermell
// En el cas de l'operació de potència (^) si el segon operador és un número decimal.
// S'ha de truncar i mostrar el nou valor en el camp del segon operand
// 28. Realitza un script amb funcionalitat de calculadora.

function calcular() {
    // 1. Agafar els VALORS, no els elements
    let num1 = parseFloat(document.getElementById("num1").value.replace(',', '.'));
    let num2 = parseFloat(document.getElementById("num2").value.replace(',', '.'));
    
    // 2. Agafar l'operació 
    const operacio = document.getElementById("operacio").value;
    
    let resultat = 0;

    // 3. Validar que són números
    if (isNaN(num1) || isNaN(num2)) {
        mostrarError("Si us plau, introdueix números vàlids");
        return;
    }

    // 4. Switch 
    switch (operacio) {
        case "+":
            resultat = num1 + num2;
            break;
        case "-":
            resultat = num1 - num2;
            break;
        case "/":
            if (num2 === 0) {
                mostrarError("No es pot dividir per zero");
                return;
            }
            resultat = num1 / num2;
            break;
        case "*":
            resultat = num1 * num2;
            break;
        case "^":
            num2 = Math.trunc(num2);
            document.getElementById("num2").value = num2; // Actualitzar el camp
            resultat = Math.pow(num1, num2);
            break;
        default:
            mostrarError("Operació no vàlida");
            return;
    }

    // 5. Mostrar resultat amb 2 decimals
    const field = document.getElementById("resultat");
    if (isNaN(resultat) || !isFinite(resultat)) {
        mostrarError("Resultat no vàlid");
    } else {
        field.value = resultat.toFixed(2); 
        field.style.color = "black"; 
    }
}

function mostrarError(missatge) {
    const field = document.getElementById("resultat");
    field.value = missatge;
    field.style.color = "red";
}

function reset() {
    document.getElementById("num1").value = "";
    document.getElementById("num2").value = "";
    document.getElementById("resultat").value = ""; 
    document.getElementById("resultat").style.color = "black";
}

document.addEventListener('DOMContentLoaded', function() {
    const calcul = document.getElementById("calcula"); 
    const resetBtn = document.getElementById("reset"); 
    
    calcul.addEventListener("click", calcular);
    resetBtn.addEventListener("click", reset);
});





// 29. Crea un formulari amb un camp de text.
// Introdueix una adreça de correu electrònic i crea un script per mostrar: (2 punts)
// La longitud del substring que identifica a l’usuari.
// El TLD (com, es, cat, etc.)
// L’adreça amb el domini canviat a thosicodina però conservant el TLD.



function longitud(){
    const text = document.getElementById("mail").value;

    // Validar que hi ha text
    if (!text) {
        alert("Si us plau, introdueix un email");
        return;
    }

    const arr_elements = text.split(".",2);
    const nom = arr_elements[0].split("@")[0];
    const llargada = nom.length; 
    const tld = arr_elements[1];
    const nou_domini = nom + "@iesthosicodina.es";

    // Crear o actualitzar el paràgraf
        const paragraf = document.createElement("p");
        paragraf.id = "paragraf";
        document.body.appendChild(paragraf);
    
    
    paragraf.innerHTML = "Longitud del substring: " + llargada + "<br>Tipus TLD: " + tld + "<br>Email en nou domini: " + nou_domini;
}

function eliminar(){
    const text = document.getElementById("mail");
    text.value = ""; 
    
    const paragraf = document.getElementById("paragraf"); 
    paragraf.remove();  
      
}

const boto = document.getElementById("boto");
boto.addEventListener("click", longitud);

const bot_eliminar =document.getElementById("eliminar")
bot_eliminar.addEventListener("click", eliminar)


const email = [
"p.escosa@gmail.com",
"j.garcia@info.yahoo.es",
"r.esteban@sales.gmail.com",
"a.gomez@gmail.es",
"l.mesa@gmail.com",
"t.sants@hotmail.es",
"v.ros@hotmail.com"
]

function filtar_mail(){
    const llista_es=[]
    const llista_com=[]


    email.forEach(element => {
        const separat = element.split(".");
        const tld =separat[separat.length-1];
        
        if (tld === "com"){
            llista_com.push(element);
        } else {
            llista_es.push(element); 
        }
    });

   const contenidor = document.createElement("div");
    contenidor.id = "resultats-mail";
    
    const titol = document.createElement("h3");
    titol.textContent = "Emails filtrats per TLD";
    contenidor.appendChild(titol);

    const paragrafCom = document.createElement("p");
    paragrafCom.innerHTML = `<strong>Domini .com (${llista_com.length}):</strong><br>${llista_com.join('<br>')}`;
    contenidor.appendChild(paragrafCom);

    const paragrafEs = document.createElement("p");
    paragrafEs.innerHTML = `<strong>Domini .es (${llista_es.length}):</strong><br>${llista_es.join('<br>')}`;
    contenidor.appendChild(paragrafEs);

    // Eliminar resultats anteriors si existeixen
    const resultatAnterior = document.getElementById("resultats-mail");
    if (resultatAnterior) {
        resultatAnterior.remove();
    }

    document.body.appendChild(contenidor);
}
document.addEventListener('DOMContentLoaded', filtar_mail);


//Extreure subdominis
function extreure_subdominis(){
    const emailsAmbSubdomini = [];
    
    email.forEach(element => {
        // Separar el domini (part després de @)
        const parts = element.split("@");
        if (parts.length === 2) {
            const domini = parts[1]; 
            const partsDomini = domini.split(".");
            
            if (partsDomini.length > 2) {
                const subdomini = partsDomini[0]; 
                emailsAmbSubdomini.push({
                    email: element,
                    subdomini: subdomini
                });
            }
        }
    });

    // Crear elements per mostrar els resultats
    const contenidor = document.createElement("div");
    contenidor.id = "resultats-subdominis";
    
    const titol = document.createElement("h3");
    titol.textContent = "Subdominis dels emails";
    contenidor.appendChild(titol);

    emailsAmbSubdomini.forEach(item => {
        const paragraf = document.createElement("p");
        paragraf.innerHTML = `<strong>Subdomini de l'email ${item.email}</strong> --> ${item.subdomini}`;
        contenidor.appendChild(paragraf);
    });

    // Eliminar resultats anteriors si existeixen
    const resultatAnterior = document.getElementById("resultats-subdominis");
    if (resultatAnterior) {
        resultatAnterior.remove();
    }

    document.body.appendChild(contenidor);
}

// Executar automàticament
document.addEventListener('DOMContentLoaded', extreure_subdominis);





//30. Realitza un script que mostri la data i l’hora actual amb precisió de segon amb diferents formats.
function data_act(){
    const data= new Date()

    const any = data.getFullYear();  
    const mes = (data.getMonth() + 1).toString().padStart(2, '0');
    const dia = data.getDate().toString().padStart(2, '0');
    const hora = data.getHours().toString().padStart(2, '0');
    const minuts = data.getMinutes().toString().padStart(2, '0');
    const segons = data.getSeconds().toString().padStart(2, '0');       

    const contenidor = document.createElement("div")

    const titol = document.createElement("h3");
    titol.textContent = "Data act";
    contenidor.appendChild(titol);

    const fecha = document.createElement("p");
    fecha.id="data"
    fecha.textContent = `${dia}-${mes}-${any} ${hora}:${minuts}:${segons}`;
    contenidor.appendChild(fecha);

    document.body.appendChild(contenidor)



    const elementData = document.getElementById("data");
    elementData.addEventListener("dblclick", function(){
        // Comprovar si el text conté guions (format actual)
        if (this.textContent.includes("-")) {
            // Canviar a format amb barres
            const diesAngles = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];
            // Mesos en anglès (abreujats)
            const mesosAngles = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];

            const diaSetmana = data.getDay(); // 0-6
            const mesNum = data.getMonth();
            
            this.textContent = `${diesAngles[diaSetmana]} ${dia} ${mesosAngles[mesNum]} ${any} ${hora}:${minuts}:${segons}`;
        } else {
            // Tornar al format amb guions
            
            this.textContent = `${dia}-${mes}-${any} ${hora}:${minuts}:${segons}`;
        }
    });
}
document.addEventListener("DOMContentLoaded",data_act) 


