//Exercici 28
const calc=document.getElementById("calculadora");

function creaInputs (){
    let divInputPrimer=document.querySelector("#div");
    
    const inputFirst=document.createElement("input");
    inputFirst.type='text';
    inputFirst.className='primerDigit';
    inputFirst.id='primerDigit';

    const selectOperacions=document.createElement("select");
    selectOperacions.name='operacions';
    selectOperacions.id='operacio-select';

    const op =['suma', 'resta', 'multiplica', 'divisio', 'potencia'];
    const op2 =['+', '-', '*', '/', '^'];


    op.forEach((element, index) =>{
        const opcio=document.createElement("option");
        opcio.value=element;
        opcio.textContent=op2[index];
        selectOperacions.appendChild(opcio);
    })

    const inputSecond=document.createElement("input");
    inputSecond.type='text';
    inputSecond.className='segonDigit';
    inputSecond.id='segonDigit';

    const igual=document.createTextNode('=');

    const inputResult=document.createElement("input");
    inputResult.type='text';
    inputResult.className='result';
    inputResult.id='result';

    const botoCalcul= document.createElement("button");
    botoCalcul.type='submit';
    botoCalcul.className='ferCalcul';
    botoCalcul.id='ferCalcul';
    botoCalcul.innerHTML='Calcula';

    const botoReset= document.createElement("button");
    botoReset.type='submit';
    botoReset.className='reset';
    botoReset.id='reset';
    botoReset.innerHTML='Reseteja';

    divInputPrimer.append(inputFirst);
    divInputPrimer.append(selectOperacions);
    divInputPrimer.append(inputSecond);
    divInputPrimer.append(igual);
    divInputPrimer.append(inputResult);
    divInputPrimer.append(document.createElement("br"), botoCalcul, botoReset);
    calc.insertAdjacentElement("afterbegin", divInputPrimer);
}

function calcul(){
    const ferCalculs=document.querySelector("#ferCalcul");

    ferCalculs.addEventListener('click', () =>{
        const selectOpera=document.querySelector("#operacio-select");
        const operacioEscollida= selectOpera.value;

        let primerDi= parseFloat(document.querySelector("#primerDigit").value.replace(',', '.'));
        let segonDi=parseFloat(document.querySelector("#segonDigit").value.replace(',', '.'));

        const inputResultat=document.querySelector('#result');
        
        let resultat;

        //Per resetejar el color
        inputResultat.style.color='';
        switch (operacioEscollida){
            case 'suma':
                resultat=primerDi+segonDi;
                break;
            case 'resta':
                resultat=primerDi-segonDi;
                break;
            case 'multiplica':
                resultat=primerDi*segonDi;
                break;
            case 'divisio':
                resultat=primerDi/segonDi;
                break;
            case 'potencia':
                segonDi=Math.trunc(segonDi);
                document.querySelector("#segonDigit").value=segonDi;
                resultat=primerDi ** segonDi;
                break;
        }

        if (!isFinite(resultat)){
            inputResultat.style.color='red';
        }

        inputResultat.value=resultat.toFixed(2);
    })
}

//Exercici 29
function crearInputs2 (){
    let divInputSegon=document.querySelector("#div2");

    const inputEmail=document.createElement("input");
    inputEmail.type='text';
    inputEmail.className='email';
    inputEmail.id='email';

    const botoExecuta= document.createElement("button");
    botoExecuta.type='submit';
    botoExecuta.className='executa';
    botoExecuta.id='executa';
    botoExecuta.innerHTML='Executa';

    const botoReset2= document.createElement("button");
    botoReset2.type='submit';
    botoReset2.className='reset';
    botoReset2.id='reset';
    botoReset2.innerHTML='Reseteja';

    const paragraf=document.createElement("p");
    paragraf.innerHTML="Primera part";

    divInputSegon.append(paragraf, inputEmail, document.createElement("br"), botoExecuta, botoReset2);
    //calc.insertAdjacentElement("beforeend", divInputSegon);
}

function dades(){
    const executa=document.querySelector("#executa");

    executa.addEventListener('click', () => {
        const getEmail=document.querySelector("#email");
        const valueEmail= getEmail.value;

        //part per extreure la longitud satring del usuari
        const str=valueEmail.split('@');

        let leng="";
        if (valueEmail.includes('@')){
            leng= str[0].length;
        }

        document.querySelector("#div2").insertAdjacentHTML('beforeend', "<br>"+"Longitud subtring usuari = "+leng);
        
        //Per agafar el tipus de TLD
        const str2=valueEmail.split('.');

        let TLD="";
        if(valueEmail.includes('.')){
            TLD=str2[1];
        }

        document.querySelector("#div2").insertAdjacentHTML('beforeend', "<br>"+"Tipus de TLD = "+TLD);

        //Email amb nou domini
        const nouDomini="thosicodina";

        let newMail="";
        if (valueEmail.includes('@') && valueEmail.includes('.')){
            newMail=str[0]+'@'+nouDomini+'.'+str2[1];
        }
        document.querySelector("#div2").insertAdjacentHTML('beforeend', "<br>"+"Email amb nou domini = "+newMail);
    })
}

function creaInputs3(){
    let divInputTercer=document.querySelector("#div3");

    const botoFiltra= document.createElement("button");
    botoFiltra.type='submit';
    botoFiltra.className='filtra';
    botoFiltra.id='filtra';
    botoFiltra.innerHTML='Filtra';

    const botoReset3= document.createElement("button");
    botoReset3.type='submit';
    botoReset3.className='reset';
    botoReset3.id='reset';
    botoReset3.innerHTML='Reseteja';

    const paragraf2=document.createElement("p");
    paragraf2.className="paragraf2";
    paragraf2.innerHTML="Segona part";

    divInputTercer.prepend(document.createElement("br"), paragraf2,  document.createElement("br"), botoFiltra, botoReset3);
    //calc.insertAdjacentHTML('beforeend', "<br>Segona part");
    //calc.insertAdjacentElement("beforeend", divInputTercer);
}

function dades2(){
    const emails = [
        "p.escosa@gmail.com",
        "j.garcia@info.yahoo.es",
        "r.esteban@sales.gmail.com",
        "a.gomez@gmail.es",
        "l.mesa@gmail.com",
        "t.sants@hotmail.es",
        "v.ros@hotmail.com"
    ]

    let gmailCom=[]
    let TLDes=[];

    emails.forEach((element) => {
        //perque em busqui els elements de l'array i m'ho separi entre els de "gmail.com" i TLD ".es"
            if (element.includes('gmail') && element.endsWith('.com')){
                gmailCom.push(element);
            }
            
            if (element.endsWith('.es')){
                TLDes.push(element);
            }
    })
    document.querySelector(".paragraf2").insertAdjacentHTML('afterend', "<br>"+"<u>Emails gmail.com:</u>"+"<br>"+gmailCom.join('<br>'));
    document.querySelector(".paragraf2").insertAdjacentHTML('afterend', "<u>Emails TLD .es:</u>"+"<br>"+TLDes.join('<br>'));
    
    //Quan faig click al botó per filtrar
    const filtra=document.querySelector("#filtra");
    filtra.addEventListener('click', () => {
        let primeraPart=[];
        let dominiComplert =[];
        let domini=[];
        
        let subdominis=[];
        emails.forEach((element) => {
            //Per filtrar els subdominis
            const parts= element.split('@'); //De l'array emails em separa en dos cada email a partir del '@'
            primeraPart.push(parts[0]); //Aqui guardem la part[0] que es la de l'usuari
            dominiComplert.push(parts[1]); //Aqui guardem la part[1] que és la del domini
            const altrePart= parts[1].split('.'); //Aqui em separa la part[1] (del domini) per parts a partir del caracter '.'
            domini.push(altrePart);

            if (altrePart.length > 2){
                subdominis.push("Subdomini de l'element " + element + " --> "+altrePart[0]); //Un cop tenim separada cada part del domini, guardem el primer element quan la longitud es mes gran a 3
                
            }
        })
        document.querySelector("#div3").insertAdjacentHTML('beforeend', "<br><br>"+"<strong>FILTRATGE:</strong>"+"<br>"+subdominis.join('<br>'));
    })

}
//Exercici 30
//hem de fer servir el setInterval() i em de fer servir una funció i cada quant volem que s'executi
//El mètode/funció que al fer doble click canvii d'un format a l'altre és
const divCuart=document.querySelector("#div4");
const contenidor=document.createElement("div")
contenidor.id="data";

divCuart.append(contenidor);

let tiempo;
function formatPrimer(){
        tiempo= new Date();
        const dia=tiempo.getDate().toString().padStart(2, '0');
        const mes=(tiempo.getMonth()+1).toString().padStart(2, '0');
        const ano=tiempo.getFullYear();

        const hora=tiempo.getHours().toString().padStart(2, '0');
        const min=tiempo.getMinutes().toString().padStart(2, '0');
        const seg=tiempo.getSeconds().toString().padStart(2, '0');

        const format1= `${dia}-${mes}-${ano} ${hora}:${min}:${seg}`;

    contenidor.innerHTML=format1;
}

function formatSegon(){
    tiempo= new Date();

    const diaSetmana=tiempo.toLocaleDateString('en-US', {weekday: 'short'});
    const dia2=tiempo.getDate().toString().padStart(2, '0');
    const mesText= tiempo.toLocaleDateString('en-US', {month: 'short'});
    const ano2=tiempo.getFullYear();

    const hora2=tiempo.getHours().toString().padStart(2, '0');
        const min2=tiempo.getMinutes().toString().padStart(2, '0');
        const seg2=tiempo.getSeconds().toString().padStart(2, '0');

        const format2= `${diaSetmana} ${dia2} ${mesText} ${ano2} ${hora2}:${min2}:${seg2}`;

    contenidor.innerHTML=format2;
}

let formatAct=1;
function actualitzaData(){
    if (formatAct === 1) {
        formatPrimer();
    } else {
        formatSegon();
    }
}

setInterval (actualitzaData, 1000);

contenidor.addEventListener('dblclick', () =>{
    formatAct = formatAct=== 1 ? 2 : 1;
})

creaInputs();
    calcul();

    crearInputs2();
    dades();

    creaInputs3();
    dades2();

    formatPrimer();
    formatSegon();
    actualitzaData();