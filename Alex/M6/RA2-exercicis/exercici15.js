function afegirFormulari() {
    const formulari = document.createElement('form');
    formulari.action = '#';
    formulari.method = 'post';
    formulari.id = 'user-data';
    formulari.name = 'user-data';

    let entra = document.createElement('input');
    entra.type = "email";
    entra.name = "email";
    entra.placeholder = "Please enter a valid email account";
    entra.required = true;
    entra.classList.add("form-control");
    formulari.appendChild(entra);

    let boto = document.createElement('button');
    boto.type = "submit";
    boto.id = "send";
    boto.innerHTML = "Send";
    formulari.appendChild(boto);
    document.body.appendChild(formulari);
}