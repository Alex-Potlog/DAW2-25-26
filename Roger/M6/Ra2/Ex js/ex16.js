const menu = ['home','about','products','contact']

const nav = document.createElement('nav');
nav.className = 'menu';

// Crear la lista ul
const ul = document.createElement('ul');

// Crear cada elemento li con su enlace a partir del array
menu.forEach(item => {
    const li = document.createElement('li');
    
    const a = document.createElement('a');
    a.href = item.enlace;
    a.textContent = item.texto;
    
    li.appendChild(a);
    ul.appendChild(li);
});

// Ensamblar la estructura
nav.appendChild(ul);

// Añadir el menú al documento
document.body.appendChild(nav);