function afegirNavegador() {
    const menu = ['home', 'about', 'products', 'contact'];
    let navegador = document.createElement('nav');
    navegador.classList.add("menu");
    let llista = document.createElement('ul');

    for (let i = 0; i < menu.length; i++) {
        const extensio = ".html";
        let temp = document.createElement('li');
        let enllac = document.createElement('a');
        enllac.href = menu[i].concat(extensio);
        enllac.innerHTML = menu[i].charAt(0).toLocaleUpperCase().concat(menu[i].slice(1));
        temp.appendChild(enllac);
        llista.appendChild(temp);
    }

    navegador.appendChild(llista);
    document.body.appendChild(navegador);
    document.body.appendChild("<p>Hola</p>");
}