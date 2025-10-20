const menu = ['home','about','products','contact']

const nav = document.createElement('nav');
nav.className = 'menu';

const ul = document.createElement('ul');

menu.forEach(item => {
    const li = document.createElement('li');
    
    const a = document.createElement('a');
    a.href = item.enlace;
    a.textContent = item.texto;
    
    li.appendChild(a);
    ul.appendChild(li);
});

nav.appendChild(ul);

document.body.appendChild(nav);