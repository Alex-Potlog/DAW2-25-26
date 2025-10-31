//14. Mitjançant JavaScript crea un element HTML amb les mateixes característiques que el què es mostra. Al final elimina l'atribut id
/*<input type="email" name="email" id="email" class="form-element"
required="required" placeholder="Please enter a valid email account">*/

function afegir() {
    let newInput = document.createElement("input");

    newInput.type = 'email';
    newInput.name = 'email';
    newInput.id = 'email';
    newInput.className = 'form-element';
    newInput.required = true;
    newInput.placeholder = 'Please enter a valid email account';
    //Eliminar atribut id
    newInput.removeAttribute('id');
    //afegir el nou element al body
    document.body.appendChild(newInput);
}
console.log('Element creat i atribut id eliminat');

//15. Crea un element <form> i afegeix l'<input> del punt anterior i un <button>
/*<form action="#" method="post" id="user-data" name="user-data" novalidate>
    <input type="email" name="email" id="email" class="form-element"
        required="required" placeholder="Please enter a valid email account">
        <button type="submit" id="send">Send</button>
    </input>
</form>*/
function afegirForm() {
    let newForm = document.createElement("form");
    newForm.action = '#';
    newForm.method = 'post';
    newForm.id = 'user-data';
    newForm.name = 'user-data';

    let input = document.createElement("input");
    input.type = 'email';
    input.name = 'email';
    input.id = 'email';
    input.className = 'form-element';
    input.required = true;
    input.placeholder = 'Please enter a valid email account';


    let boton = document.createElement("button");
    boton.type = 'submit';
    boton.id = 'send';
    boton.innerHTML = 'send';

    newForm.appendChild(input);
    newForm.appendChild(boton);
    document.body.appendChild(newForm);
}


//16. Crea un menú a partir dels valors d'un array
/*const menu = ['home', 'about', 'products', 'contact']
    < nav class="menu" >
        <ul>
            <li><a href="home.html">Home</a></li>
            <li><a href="about.html">About</a></li>
            <li><a href="products.html">Products</a></li>
            <li><a href="contact.html">Contact</a></li>
        </ul>
</nav>*/

//per repetir els <li> es pot fer amb els TEMPLATE STRING
//un accent obert (`) em permet barrejar text html i variables de javascript

function afegirMenu() {
    const menu = ['home', 'about', 'products', 'contact'];
    let template = '<nav class = "menu"><ul>';

    menu.forEach(element => {
        template += `<li><a href="${element}.html">${element.charAt(0).toUpperCase() + element.slice(1).toLowerCase()}</a></li>`;
    })

    template += '</ul></nav>';

    document.body.innerHTML += template;
}


console.log(template);