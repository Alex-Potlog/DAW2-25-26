//Es necessita crear aquesta constant per obtenir una referència 
// de l'element <table> del DOM per a poder afegir el <thead>
const taula = document.getElementById("taula");

function init() {
    afegirCapcelera();
    afegirProducte();
    afegirBoto();
    preuTotal();
    calculTotal();
    eliminaFila();
    modificaQuantitatPreu();
    eliminaTaula();
}

function afegirCapcelera() {
    const headItem = ['Codi', 'Imatge', 'Descripció', 'Quantitat', 'Preu', 'Import', ''];

    let cap = document.createElement("thead");
    let row = document.createElement("tr");

    headItem.forEach(element => {
        let th = document.createElement("th");
        th.textContent = element;
        row.appendChild(th);
    });

    cap.appendChild(row);
    taula.insertAdjacentElement("afterbegin", cap);
}

function afegirProducte() {
    const products = [
        [101, 'steelseires-arctis-5-rgb-negros.webp', 'Steelseires Arctis 5 Auriculars Gaming RGB Negres', 108.59],
        [102, '1202-agfa-photo-ac7000-camara-deportiva-16mp.webp', 'Agfa Photo AC7000 Càmera Esportiva 16MP', 119.50],
        [103, '1920-xiaomi-poco-m3-pro-5g-4-64gb-amarillo-libre.webp', 'Xiaomi POCO M3 Pro 5G 4/64GB Groc LLiure', 315.99],
        [104, 'logitech.webp', 'Logitech G Saitek X52 Flight Control System Sistema de Control de Vol', 158.60],
        [105, '115-msi-raider.webp', 'MSI Raider GE77HX 12UGS-020ES Intel Core i9 - 12900HX / 64GB / 2TB SSD / RTX 3070Ti / 17.3"', 3599.00]
    ];

    //S'utilitza per agafar la referència del <tbody> del html
    let tabBody = document.querySelector("#tbody");

    products.forEach(element => {
        let trProduct = `<tr>
        <td class="codi">${element[0]}</td>
        <td class="imatge"><img src="img/${element[1]}"/></td>
        <td class="descripcio">${element[2]}</td>
        <td class="quant"><input type="number" class="inputQ" id="quant" min="0" max="10" value="1"></td>
        <td class="preu">${element[3]}</td>
        <td class="import">${element[3]}</td>
        <td><span class="falsi"><img src="img/Falsi.webp"></span></td></tr>`
        tabBody.insertAdjacentHTML("beforeend", trProduct);
    });
}

function preuTotal() {
    //S'utilitza per agafar la referència del <tbody> del html

    let tfoot = document.querySelector("#tfoot");

    let trTotal = `<tr><td colspan="4"></td><td><strong>Import total:</strong></td><td class="iTotal">()</td></tr>`;

    tfoot.insertAdjacentHTML("beforeend", trTotal);
}

function calculTotal() {
    let im = document.querySelectorAll(".import");

    let valor = 0;
    im.forEach(element => {
        valor += parseFloat(element.innerText);
    })

    // Guardes el valor calcular a la cel·la de la taula amb la classe que
    // hi ha als parentesis.
    document.querySelector(".iTotal").innerHTML = valor;
}

function afegirBoto() {
    let divBoto = document.querySelector("#div");
    const boto = document.createElement("button");
    boto.type = 'submit';
    boto.className = 'buit';
    boto.id = 'buit';
    boto.innerHTML = 'Buidar Carretó';

    divBoto.insertAdjacentElement("beforeend", boto)
    //taula.insertAdjacentElement("afterend", div);
}

function eliminaFila() {
    const elimina = document.querySelectorAll('.falsi');
    elimina.forEach(button => {
        button.addEventListener('click', (e) => {
            const tr = e.target.closest('tr');

            // Captura el preu de la fila abans d'eliminar-la
            const importR = parseFloat(tr.querySelector('.import').textContent);

            tr.remove();

            //Cridem a la funció per a que actualitzi el total quan cliquem a la creu
            actualitzaImportFinal1(importR);
        })
    })
}

function actualitzaImportFinal1(importRestar) {
    const importTotal = document.querySelector('.iTotal'); //Amb el selector busquem la classe d'on volem agafar la dada
    let importCarretoTotal = parseFloat(importTotal.textContent); //Extreiem el contingut de la variable inicialitzada just a sobre
    importCarretoTotal -= importRestar; //restem el contingut de la variable inicialitzada dins la funció amb el valor obtingut per parametre.

    importTotal.textContent = importCarretoTotal.toFixed(2); //Guardem el nou valor a la cel·la on teniem el valor inicial. El .toFix(2) ens serveix per indicar quans decimals volem, en aquest cas 2
}

function modificaQuantitatPreu() {
    const cantidad = document.querySelectorAll('.inputQ');

    cantidad.forEach(input => {
        input.addEventListener('change', (e) => {
            const tr = e.target.closest('tr');
            let cantidadDiferente = parseInt(input.value);

            const precio = parseFloat(tr.querySelector('.preu').textContent);
            const totFi = precio * cantidadDiferente;
            const importe = tr.querySelector('.import');
            importe.textContent = totFi.toFixed(2);

            calculTotal();
        })
    })
}

function eliminaTaula() {
    const botoBuit = document.querySelectorAll(".buit");
    botoBuit.forEach(button => {
        button.addEventListener('click', (e) => {
            const tbody = document.getElementById("tbody");

            tbody.remove();
            //Cridem a la funció per a que actualitzi el total quan cliquem a la creu
            calculTotal(0);


            const body = document.createElement("tbody");
            const msg = "No hi ha productes al carretó";
            body.insertAdjacentHTML("beforeend", msg);
            taula.insertAdjacentElement("afterbegin", body);

        })
    })


}