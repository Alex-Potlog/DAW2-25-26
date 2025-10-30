//31
//local storage -> la informació que introdueixo a un formulari es guarda a un local storage i si o clicko a f5 dons se'm manté la informació introduida
//Exemple -> window.localStorrage.setItem("myCat", "Tom")
//Per llegir -> const cat=localStorage.getItem("myCat")
//Per eliminar -> localStorage.removeItem("myCat")

const myObj = {name: "Marta", age: 33, city:"Mataró"};

const myJson=JSON.stringify(myObj);

localStorage.setItem('myObj', myJson);

const recuperada= JSON.parse(localStorage.getItem('myObj'))

console.log(recuperada)

//StruturedClone -> 

//-----------------------------------------------------------------------

function creaForm(){
    const createFormField = (label, name, type = 'text', required = false) => `
    <div>
        <label for="${name}">${label}${required ? ' *' : ''}:</label><br>
        <input type="${type}" id="${name}" name="${name}" ${required ? 'required' : ''}>
    </div>
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
    botoReset.className='reset';
    botoReset.id='reset';
    botoReset.innerHTML='Reseteja';

    divForm.append(document.createElement("br"),botoEnvia, botoReset);
}

function carregaDades(){
    const formRef=document.querySelector('form');
    const storageKey='formData'; //Clau per guardades les dades
    let formData={}; //objecte per guardar les dades del formulari

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
    }) 

    
}
// Save the entered date
/*formRef.addEventListener ('change', function (e) {
    console.log(e);
    formData[e.target.name]=e.target.value;
    console.log(formData)
    localStorage.setItem(storageKey, JSON.stringify(formData))
}) 
    
document.getElementById('submit).addEventListener('click'...)
document.getElementById('reset').addEventListener('click',)
*/



creaForm();
creaBotons();
carregaDades();