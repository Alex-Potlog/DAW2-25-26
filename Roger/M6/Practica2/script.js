const doc = document.querySelector('.container'); 

const taula = document.getElementById('cart-table');

const headItem = ['Codi', 'Imatge', 'Descripció', 'Quantitat', 'Preu',
    'Import', 'Eliminar'];

const thead = document.createElement('thead');
thead.id = 'table-head';

const LineaCapceleraTaula = document.createElement('tr');

headItem.forEach(element => {
    const th = document.createElement("th");
    th.textContent = element;
    LineaCapceleraTaula.appendChild(th)
});

thead.appendChild(LineaCapceleraTaula)

taula.appendChild(thead)


const products = [
    [101, '/img/steelseires-arctis-5-rgb-negros.webp', 'Steelseires Arctis 5Auriculars Gaming RGB Negres', 108.59],
    [102, '/img/1202-agfa-photo-ac7000-camara-deportiva-16mp.webp', 'AgfaPhoto AC7000 Càmera Esportiva 16MP', 119.50],
    [103, '/img/1920-xiaomi-poco-m3-pro-5g-4-64gb-amarillo-libre.webp', 'Xiaomi POCO M3 Pro 5G 4/64GB Groc LLiure', 315.99],
    [104, '/img/logitech.webp', 'Logitech G Saitek X52 Flight Control SystemSistema de Control de Vol', 158.60],
    [105, '/img/115-msi-raider.webp', 'MSI Raider GE77HX 12UGS-020ES IntelCore i9-12900HX/64GB/2TB SSD/RTX 3070Ti/17.3"', 3599.00]
];

const cos = document.getElementById('table-body');

products.forEach(element => {
    const productHTML = `
        <tr>
            <td>${element[0]}</td>
            <td><img src="${element[1]}" class="product-image" alt=""></td>
            <td>${element[2]}</td>
            <td><input type="number" min="0" max="10" value="1" class="quantity-input" data-preu="${element[3]}"></td>
            <td class="price">${element[3]} €</td>
            <td class="import">${element[3]} €</td>
            <td><button class="delete-icon">🗑️</button></td>
            <br/>
        </tr>
    `;

    cos.insertAdjacentHTML('beforeend', productHTML)
})
taula.appendChild(cos)

const filaTotal = `
    <tr class="total-row">
        <td colspan="5" style="text-align: right; font-weight: bold;">TOTAL:</td>
        <td class="import">0.00 €</td>
        <td></td>
    </tr>
`;
cos.insertAdjacentHTML('beforeend', filaTotal)


function calculTotal() {
    let total = 0;
    const filesProductes = cos.querySelectorAll('tr:not(.total-row)');

    filesProductes.forEach(element => {
        const importotal = element.querySelector('.import');
        if (importotal) {
            const import_text = importotal.textContent.replace(' €', '').trim();//per eliminar els euros que estan a import
            const import_valor = parseFloat(import_text) || 0;
            total += import_valor;
        }
    });

    return total;
}


function actualitzarTotal() {
    const total = calculTotal();
    const lloctotal = document.querySelector(".total-row .import");

    if (lloctotal) {
        lloctotal.textContent = `${total.toFixed(2)} €`;
    }
}

actualitzarTotal()

cos.addEventListener("input", (e) => {

    if (e.target.classList.contains('quantity-input')) {
        const quantitat = parseInt(e.target.value) || 0;//Obte la informació del camp i la transforma en un int tant si es 0 o un altre numero
        const preu = parseFloat(e.target.dataset.preu);
        const import_calculat = preu * quantitat;

        // Trobar la cel·la import de la mateixa fila
        const fila = e.target.closest('tr');//S'obte la fila completa del imput
        const cellaImport = fila.querySelector('.import');//Slecciono l'apartat del import
        cellaImport.textContent = `${import_calculat.toFixed(1)} €`;//I modifico aquest en 1 decimals

        actualitzarTotal();
    }
})

cos.addEventListener("click", (e) => {
    if (e.target.classList.contains('delete-icon')) {
        const fila = e.target.closest('tr');
        if (fila) {
            fila.remove();
        }
    }
    actualitzarTotal()
})

document.addEventListener("click", (e) => {
    if (e.target.classList.contains("clear-cart-btn")) {
        const filesProductes = cos.querySelectorAll('tr:not(.total-row)');
        if (filesProductes) {
            // filesProductes.forEach(fila => fila.remove());
            // actualitzarTotal();

            taula.remove();


            const noelementsHTML =`
                    <h1>No hi ha elements al carreto</h1>
            `;

            doc.insertAdjacentHTML("beforeend", noelementsHTML);
        }
    }

   
});

taula.appendChild(cos);