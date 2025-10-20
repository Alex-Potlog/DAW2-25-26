window.onload = function () {
    const headItem = ['Codi', 'Imatge', 'Descripció', 'Quantitat', 'Preu', 'Import'];
    const products = [
        [101, 'steelseires-arctis-5-rgb-negros.webp', 'Steelseires Arctis 5 Auriculars Gaming RGB Negres', 108.59],
        [102, '1202-agfa-photo-ac7000-camara-deportiva-16mp.webp', 'Agfa Photo AC7000 Càmera Esportiva 16MP', 119.50],
        [103, '1920-xiaomi-poco-m3-pro-5g-4-64gb-amarillo-libre.webp', 'Xiaomi POCO M3 Pro 5G 4/64GB Groc LLiure', 315.99],
        [104, 'logitech.webp', 'Logitech G Saitek X52 Flight Control System Sistema de Control de Vol', 158.60],
        [105, '115-msi-raider.webp', 'MSI Raider GE77HX 12UGS-020ES Intel Core i9-12900HX/64GB/2TB SSD/RTX 3070Ti/17.3"', 3599.00]
    ];

    const table = document.createElement("table");
    document.body.appendChild(table);

    const thead = document.createElement("thead");
    table.appendChild(thead);

    const tr = document.createElement("tr");
    thead.appendChild(tr);

    headItem.forEach(item => {
        const th = document.createElement("th");
        th.textContent = item;
        tr.appendChild(th);
    })
    const tbody = document.createElement("tbody");
    table.appendChild(tbody);

    products.forEach(producte => {
        const [codi, imatge, descripcio, preu] = producte;

        tbody.insertAdjacentHTML('beforeend', `
            <tr>
                <td>${codi}</td>
                <td><img src="img/${imatge}" alt="${descripcio}" width="100"></td>
                <td>${descripcio}</td>
                <td><input type="number" value="1" min="0" max="10" class="quantity"></td>
                <td>${preu.toFixed(2)} €</td>
                <td class="import">${preu.toFixed(2)} €</td>
                <td><span class="delete" style="cursor:pointer;color:red;font-weight:bold;">X</span></td>
            </tr>
        `);
    });
    //Calcul

    const tbodyRows = tbody.querySelectorAll('tr');
    tbodyRows.forEach(row => {
        const quantityInput = row.querySelector('.quantity');
        const importCell = row.querySelector('.import');
        const price = Number.parseFloat(row.children[4].textContent);

        quantityInput.addEventListener('input', () => {
            const quantity = Number.parseInt(quantityInput.value);
            importCell.textContent = `${(price * quantity).toFixed(2)} €`;

        });
    });
    //afegir import total 
    const totalRow = document.createElement('tr');
    totalRow.innerHTML = `
        <td colspan="5" style="text-align:right;font-weight:bold;">Total:</td>
        <td id="total-amount" style="font-weight:bold;">0.00 €</td>
        <td></td>
    `;
    tbody.appendChild(totalRow);

    const totalAmount = document.getElementById('total-amount');

    function updateTotal() {
        let total = 0;
        const importCells = tbody.querySelectorAll('.import');
        importCells.forEach(cell => {
            const importValue = Number.parseFloat(cell.textContent);
            total += importValue;
        });
        totalAmount.textContent = `${total.toFixed(2)} €`;
    }

    // Actualitzar el total inicialment
    updateTotal();

    // Actualitzar el total quan canvia la quantitat
    const quantityInputs = tbody.querySelectorAll('.quantity');
    quantityInputs.forEach(input => {
        input.addEventListener('input', updateTotal);
    });




    // Afegir funcionalitat de eliminar fila
    const spanDelete = document.querySelectorAll('.delete')
    spanDelete.forEach(span => {
        span.addEventListener('click', (e) => {
            const tr = e.target.closest('tr')
            tr.remove()
        })
    })
    // afegir funcionalitat de buidar carret 
    const clearCartButton = document.createElement('button');
    clearCartButton.textContent = 'Buidar Carretó';
    document.body.appendChild(clearCartButton);

    clearCartButton.addEventListener('click', () => {
        tbody.innerHTML = '<tr><td colspan="7">No hi ha productes al carretó</td></tr>';
    });



}