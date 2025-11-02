//31
//local storage -> la informació que introdueixo a un formulari es guarda a un local storage i si o clicko a f5 dons se'm manté la informació introduida
//Exemple -> window.localStorrage.setItem("myCat", "Tom")
//Per llegir -> const cat=localStorage.getItem("myCat")
//Per eliminar -> localStorage.removeItem("myCat")

function creaForm(){
    const createFormField = (label, name, type = 'text', required = false) => `
    <label for="${name}">${label}${required ? ' *' : ''}:</label><br>
    <input type="${type}" id="${name}" name="${name}" ${required ? 'required' : ''}><br>

`;

const form = `
    ${createFormField('Nom', 'nom', 'text', true)}
    ${createFormField('Cognom', 'cognom')}
    ${createFormField('E-mail', 'email', 'email', true)}
    ${createFormField('Adreça', 'adreca')}
`;

// Això és el que falta: inserir-ho al DOM
document.getElementById('form1').innerHTML = form;
}

function creaBotons(){
    let divForm=document.querySelector("#form1");
    
    const botoEnvia= document.createElement("button");
    botoEnvia.type='submit';
    botoEnvia.className='envia';
    botoEnvia.id='envia';
    botoEnvia.innerHTML='Envia';

    const botoReset= document.createElement("button");
    botoReset.type='submit';
    botoReset.className='borrar';
    botoReset.id='borrar';
    botoReset.innerHTML='Reseteja';

    divForm.append(document.createElement("br"),botoEnvia, botoReset);
}

function carregaDades(){
    const formRef=document.getElementById('form1');
    const storageKey='formData'; //Clau per guardar les dades
    let formData=[]; //objecte per guardar les dades del formulari

    //Per a poder carregar les dades guardades
    const saveData= localStorage.getItem(storageKey);

    if (saveData){
        formData=JSON.parse(saveData);

        //Recuperar els valors
        Object.keys(formData).forEach(function(key) {
            const fiel=formRef.elements[key];
            if (fiel){
                fiel.value = formData[key];
            }
        });
    }

    //EventListener per a guardar els canvis
    formRef.addEventListener ('input', function (e) {
        formData[e.target.name]=e.target.value;
        console.log(formData)
        localStorage.setItem(storageKey, JSON.stringify(formData))
    });

    //EventListener del botó submit/enviar
    document.getElementById('envia').addEventListener('click', function(e) {
        e.preventDefault(); //Atura la execució per defecte del event (un submit d'un formulari no l'envia)
        
        alert('Formulari enviat correctament!')
    });
    
    //EventListener del botó reset
    document.getElementById('borrar').addEventListener('click', function(e){
        e.preventDefault(); //Atura la execució per defecte del event

        //Per netejar el localStorage i el formulari sencer
        localStorage.removeItem(storageKey);
        formData={};
        formRef.reset();

        console.log('Formulari i localStorage nets!');
    });
}

// Cridar la funció quan el DOM estigui llest
document.addEventListener('DOMContentLoaded', carregaDades);

creaForm();
creaBotons();
carregaDades();