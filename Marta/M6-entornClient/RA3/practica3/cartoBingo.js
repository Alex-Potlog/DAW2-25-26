// =================================== Part 1 ===================================
function generaNumeros(){
    // Paso 1: Generar 3 números por columna
    const columns = Array.from({ length: 9 }, (_, i) => {
        const min = i === 0 ? 1 : i * 10
        const max = i === 8 ? 90 : min + 9
        const nums = []
        while (nums.length < 3) {
            const num = Math.floor(Math.random() * (max - min + 1)) + min
            if (!nums.includes(num)) nums.push(num)
        }

        return nums;
    })

    return columns;
}

function ordenaNums(carto){
    carto.forEach((element, i) =>{
        if (i % 2 === 0) {
            carto[i].sort((a,b) => a-b);
        } else {
            carto[i].sort((a,b) => b-a)
        }
    })
    return carto;
}

function assignaNumsAColumnes(carto){
    const cartoFi = Array.from({ length: 3 }, () => Array(9).fill(null)) //genera una array  de 3x9 on tots els valors son null
    const colIndices = Array.from({ length: 9 }, (_, i) => i)
    const columAmbDos = colIndices.sort(() => 0.5 - Math.random()).slice(0, 6)
    const columAmbUn = colIndices.filter((i) => !columAmbDos.includes(i))

    columAmbDos.forEach((colum) =>{
        console.log("COLUM", colum);
        for(let i=0; i<2; i++){
            let row;
            do{
                row=Math.floor(Math.random()*3);
            } while (cartoFi[row][colum] !== null)
            cartoFi[row][colum] = carto[colum][row];
            console.log("ROW", row);
            console.log("carto FI", cartoFi[row][colum]);
        }

        console.log(" ");
    })

    columAmbUn.forEach((colum) =>{
        let row;
        do{
            row =Math.floor(Math.random()*3);
        }while (cartoFi[row][colum] !== null)
        cartoFi[row][colum] = carto[colum][row];
    })
    
    
    return cartoFi;
}

function validaCarto(cartoFi){
    // Paso 5: Validar que cada fila tenga 5 números
    for (let row = 0; row < 3; row++) {
        const filled = cartoFi[row].filter((cell) => cell !== null).length
        if (filled !== 5) {
        return false // No cumpleix la validació
        }
    }

    return true //Quan totes les fiels tenen 5 números.
}

function creaCartoEstruc(){
    const div=document.querySelector('.divTable');
    let numsAColumns;
    let intents=0;
    let maxIntents=100;

    do {
        const carto=generaNumeros();
        console.log("carto", carto);
        const cartoOrdenat=ordenaNums(carto)
        console.log("carto ordenat", cartoOrdenat);

        numsAColumns=assignaNumsAColumnes(cartoOrdenat);
        intents++;

        if (intents >= maxIntents){
            console.error("No es pot generar cartó vàlid després de ",maxIntents," intents")
            return;
        }
    } while(!validaCarto(numsAColumns));
    
    console.log("Assignar Numeros a Columnes", numsAColumns);
    console.log("Generat en ",intents," intents");

    const divRow= Array.from({length: 3}, (_, i) => `
        <div class="row" id="row"></div>
    `).join('');

    div.innerHTML=divRow;
    
    document.querySelectorAll('.row').forEach((row, rowIndex) =>{
        const caselles = Array.from({length: 9}, (_, i) => {
            let div;
            if (numsAColumns[rowIndex][i] !==null){
                div= `<div class="caselles num${numsAColumns[rowIndex][i]}">${numsAColumns[rowIndex][i]}</div>`
            } else {
                div= `<div class="caselles buida"></div>`
            }
            return div;
        }
            
        ).join('');

        row.innerHTML=caselles;
    });
}


// =================================== Part 2 ===================================
function creaBoto(){
    const section=document.querySelector('#bingo');

    const botoExtreu=document.createElement('button');
    botoExtreu.type='submit';
    botoExtreu.className='extreuBola';
    botoExtreu.id='extreuBola';
    botoExtreu.innerHTML='Extreu bola';

    section.appendChild(botoExtreu);
}


// Variable global pel joc
let numExtret=[];

function extreuBola (){
    let num;

    do{
        num=Math.floor((Math.random()*90)+1);
    } while (numExtret.includes(num)) 

    //Afegim el número per a que sempre es quedi a l'esquerra
    numExtret.unshift(num)

    //Actualitzar la visualtizació
    mostraNombreExtret();

    //
    const numeroCasella= document.querySelector('.num'+num);
    console.log(numeroCasella);
    if (numeroCasella){
        numeroCasella.classList.add('marcar');
    }
}

function mostraNombreExtret(){
    const container= document.querySelector('.numerosExtrets');

    container.innerHTML=numExtret.map(num =>
        `<div class="bola">${num}</div>`
    ).join('');
}

function iniciaJoc(){
    const section=document.querySelector('#bingo');
    
    const divExtrets=document.createElement('div');
    divExtrets.className='numerosExtrets';
    divExtrets.id='numerosExtrets';
    section.appendChild(divExtrets);

    document.getElementById('extreuBola').addEventListener('click', extreuBola);
}

creaCartoEstruc();
creaBoto();
iniciaJoc();