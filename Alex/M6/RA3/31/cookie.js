const nameInput = document.getElementById('name');
const cognomInput = document.getElementById('cognom');
const emailInput = document.getElementById('email');
const adrecaInput = document.getElementById('adreca');

function updateCookie(name, value) {
    document.cookie = `${name}=${value}`;
}

nameInput.addEventListener('change', () => {
    updateCookie('nom', nameInput.value);
});

cognomInput.addEventListener('change', () => {
    updateCookie('cognom', cognomInput.value);
});

emailInput.addEventListener('change', () => {
    updateCookie('email', emailInput.value);
});

adrecaInput.addEventListener('change', () => {
    updateCookie('adreca', adrecaInput.value);
});

function recarregaHistorial() {
    let llista = document.cookie;

    let dicc = {};

    llista.split(';').forEach(element => {
        const [key, value] = element.trim().split('=');
        dicc[key] = value;
    });

    nameInput.value = dicc[0];

    cognomInput.value = dicc[1];

    emailInput.value = dicc[2];

    adrecaInput.value = dicc[3];

    



    /*     document.getElementById('name').value = llista[0];
        document.getElementById('cognom').value = llista[1];
        document.getElementById('email').value = llista[2];
        document.getElementById('adreca').value = llista[3]; */

}
