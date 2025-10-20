//9. Crea un script per fusionar dos arrays
const arr1 = [1, 2, 3];
const arr2=[4,5,6];

const fusio = arr1.concat(arr2);
console.log(fusio);

//10. Converteix la data actual al següent format: '9/6/2022, 17:46:49' de la manera més concisa possible
const data = new Date();
const text = data.getDate()+"/"+data.getMonth()+"/"+data.getFullYear() +", "+data.getHours()+":"+data.getMinutes()+":"+data.getSeconds();
console.log(text);

//11. Crea un script per comparar dues dates. En el cas de comparar dues dates iguals s'ha d'utilitzar l'operador '==='
const data1 = new Date("2022, 5, 9");
const data2 = new Date("2022, 5, 9");

if (data1.getTime()===data2.getTime()){
    console.log("Són iguals");
}else{
    console.log("No són iguals");
}

//12. Crea un script que mostri els dies que han passat des de l'inici d'any
const data3 = new Date("2022, 1, 1");
const data4 = new Date("2022, 5, 9");

const millis1 = data4 - data3;
const dies = millis1 /86400000;

console.log(dies);

//13. Crea un script que retorni la data actual amb el següent format
const data5 = Date.now();
const aviu = Date(data5);

console.log(aviu.getFullYear());
