//14. Mitjançant JavaScript crea un element HTML amb les mateixes característiques que el què es mostra.
//Al final elimina l'atribut id
// Crear un contenidor per veure el resultat
const container = document.createElement('div');
container.innerHTML = '<h3>Input creat:</h3>';
document.body.appendChild(container);

const emailInput = document.createElement('input');
Object.assign(emailInput, {
    type: 'email',
    name: 'email', 
    id: 'email',
    className: 'form-element',
    required: true,
    placeholder: 'Please enter a valid email account'
});

container.appendChild(emailInput);

console.log('ABANS:', emailInput.outerHTML);

emailInput.removeAttribute('id');

console.log('DESPRÉS:', emailInput.outerHTML);