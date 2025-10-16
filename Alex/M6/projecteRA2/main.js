function crea() {
    const headItem = ['Codi', 'Imatge', 'Descripció', 'Quantitat', 'Preu', 'Import', 'Esborra'];

    let cap = document.createElement("thead");
    headItem.forEach(elm => {
        let th = document.createElement("th");
        th.textContent = elm;
        cap.appendChild(th);
    });
    document.querySelector("table").appendChild(cap);

    const products = [
        [101, 'steelseires-arctis-5-rgb-negros.webp', 'Steelseires Arctis 5 Auriculars Gaming RGB Negres', 108.59],
        [102, '1202-agfa-photo-ac7000-camara-deportiva-16mp.webp', 'Agfa Photo AC7000 Càmera Esportiva 16MP', 119.50],
        [103, '1920-xiaomi-poco-m3-pro-5g-4-64gb-amarillo-libre.webp', 'Xiaomi POCO M3 Pro 5G 4/64GB Groc LLiure', 315.99],
        [104, 'logitech.webp', 'Logitech G Saitek X52 Flight Control System Sistema de Control de Vol', 158.60],
        [105, '115-msi-raider.webp', 'MSI Raider GE77HX 12UGS-020ES Intel Core i9-12900HX/64GB/2TB SSD/RTX 3070Ti/17.3"', 3599.00]
    ];

    let entra = `<tbody>`;
    products.forEach(element => {
        entra += `<tr>`;
        element.forEach(product => {
            entra += `<td>`
            if (product.toString().includes('.webp')) {
                const img = document.createElement('img');
                img.src = 'img/' + product.toString();
                entra += img.outerHTML;
            } else if (product == element[3]) {
                entra += `${product.toFixed(2)} €`;
            } else {
                entra += product;
            }
            if (product == element[2]) {
                entra += `<td><input type="number" class="quantitat" data-preu="${element[3]}" value="1" min="1" max="10"></td>`;
            }

            entra += `</td>`;
        });
        entra += `<td class="preu">${element[3]} €</td>`;
        entra += `<td><button class="elimina"><img src="img/x-roja.png" alt="Esborra"></button></td>`;
        entra += `</tr>`;
    });

    entra += `</tbody>`;
    document.querySelector("table").insertAdjacentHTML("beforeend", entra);

    document.querySelectorAll('.quantitat').forEach(input => {
        input.addEventListener('change', actualitzaPreu);
    });

    document.querySelector('.preu').forEach(input =>
        input.addEventListener('change', actualitzaTotal)
    );
}

let total = 0;
document.querySelector('.preu').forEach(input =>
    total += parseFloat(input)
);
document.querySelector('')

function actualitzaPreu(event) {
    const input = event.target;
    const quantitat = parseInt(input.value);
    const preuBase = parseFloat(input.dataset.preu);
    const preuCell = input.closest('tr').querySelector('.preu');

    const total = quantitat * preuBase;
    preuCell.textContent = total.toFixed(2) + ' €';
}

function actualitzaTotal() {
    let total = 0;
    const mostra = document.querySelector('.preu_total');
    document.querySelector('.preu').forEach(preu =>
        total += parseFloat(input.textContent)
    );
    mostra.textContent = total;
}