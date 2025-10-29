// Crear el contenedor del formulario
const formulari = document.createElement('div');

// Crear el título
const title = document.createElement('h2');
title.textContent = 'Cookies i Web Storage';

// Crear el formulario
const form = document.createElement('form');
form.id = 'cookiesForm';

// Función para crear campos del formulario
function createField(labelText, inputName, isRequired = false) {
    const fieldDiv = document.createElement('div');

    const label = document.createElement('label');
    label.textContent = labelText;
    if (isRequired) {
        const asterisk = document.createElement('span');
        asterisk.textContent = '*';
        label.appendChild(asterisk);
    }
    label.appendChild(document.createTextNode(':'));

    const br = document.createElement('br');

    const input = document.createElement('input');
    input.type = inputName === 'email' ? 'email' : 'text';
    input.name = inputName;
    input.id = inputName;
    if (isRequired) input.required = true;

    fieldDiv.appendChild(label);
    fieldDiv.appendChild(br);
    fieldDiv.appendChild(input);
    return fieldDiv;
}

// Añadir campos al formulario
form.appendChild(createField('Nom', 'nom', true));
form.appendChild(createField('Cognom', 'cognom'));
form.appendChild(createField('E-mail', 'email', true));
form.appendChild(createField('Adreça', 'adreca'));

// Botón Envia
const submitBtn = document.createElement('button');
submitBtn.type = 'submit';
submitBtn.textContent = 'Envia';

// Botón Reseteja
const resetBtn = document.createElement('button');
resetBtn.type = 'reset';
resetBtn.textContent = 'Reseteja';

form.appendChild(submitBtn);
form.appendChild(resetBtn);


formulari.appendChild(title);
formulari.appendChild(form);

// Añadir al final del documento
document.body.appendChild(formulari);

// Recuperar valores guardados al cargar la página
const fields = ['nom', 'cognom', 'email', 'adreca'];
fields.forEach(field => {
    const savedValue = localStorage.getItem(field);
    if (savedValue) {
        document.getElementById(field).value = savedValue;
    }
});

// Guardar valores cuando cambian
fields.forEach(field => {
    const input = document.getElementById(field);
    input.addEventListener('input', function () {
        localStorage.setItem(field, this.value);
    });
});

// Event listener para el envío del formulario
form.addEventListener('submit', function (e) {
    e.preventDefault();
    const formData = new FormData(form);
    const data = Object.fromEntries(formData);
    console.log('Datos del formulario:', data);
    alert('Formulario enviado correctamente!');
});

// Event listener para el botón reset
resetBtn.addEventListener('click', function () {
    // Eliminar todos los datos guardados
    fields.forEach(field => {
        localStorage.removeItem(field);
    });
});