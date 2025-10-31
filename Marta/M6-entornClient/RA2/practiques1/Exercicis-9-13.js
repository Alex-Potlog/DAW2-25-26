// 9. Crea un script per fusionar dos arrays

const array = [1, 2, 3];
const array2 = [4, 5, 6];

const array1 = array.concat(array2);

console.log(array1);


//10. Converteix la data actual al següent format: '9/6/2022, 17:46:49' de la manera més concisa possible
Date();
const fecha = new Date();
const dia = fecha.getDate(); //getDate - Retorna el día del mes (1–31) p ara la fecha especificada acorde a la hora local.

const mes = fecha.getMonth();//getMonth()- Retorna el mes(0–11) para la fecha especificada acorde a la hora local.

const ano = fecha.getFullYear();//getFullYear() - Retorna el año (4 dígitos para años de 4 dígitos) para la fecha especificada acorde a la hora local.

const hora = fecha.getHours();//getHours() - Retorna la hora (0–23) para la fecha especificada acorde a la hora local.

const min = fecha.getMinutes();//getMinutes() - Retorna los minutos (0–59) para la fecha especificada acorde a la hora local.

const sec = fecha.getSeconds();//getSeconds - Retorna los segundos (0–59) para la fecha especificada acorde a la hora local.

console.log("'" + dia + "/" + mes + "/" + ano + ", " + hora + ":" + min + ":" + sec + "'");
/*Date.prototype.getDay() - Retorna el día de la semana (0–6) para la fecha especificada acorde a la hora local.

Date.prototype.getMilliseconds() - Retorna los milisegundos (0–999) para la fecha especificada acorde a la hora local.

Date.prototype.getTime() - Retorna el valor númerico de la fecha especificada como el número de milisegundos transcurridos desde el 1 de Enero de 1970, 00:00:00 UTC. (Retona valores negativos para fechas previas.)
*/

//11. Crea un script per comparar dues dates. En el cas de comparar dues dates iguals s'ha d'utilitzar l'operador '==='

const fecha1 = new Date(2022, 11, 30);
const fecha2 = new Date(2014, 10, 31);

if (fecha1 > fecha2) {
    console.log("La data 1 és gran a la data 2");
} else if (fecha1 < fecha2) {
    console.log("La data 2 és gran a la data 1");
} else {
    console.log("Les dos dates són iguals")
}

//12. Crea un script que mostri els dies que han passat des de l'inici d'any
// Función para calcular los días transcurridos entre dos fechas
/*restaFechas = function (f1, f2) {
    var aFecha1 = f1.split('/');
    var aFecha2 = f2.split('/');
    var fFecha1 = Date.UTC(aFecha1[2], aFecha1[1] - 1, aFecha1[0]);
    var fFecha2 = Date.UTC(aFecha2[2], aFecha2[1] - 1, aFecha2[0]);
    var dif = fFecha2 - fFecha1;
    var dias = Math.floor(dif / (1000 * 60 * 60 * 24));
    return dias;
}

var f1 = '10/09/2014';
var f2 = '15/10/2014';

console.log(restaFechas(f1, f2));*/

const dia1 = '01/01/2025';

const fe = new Date();
const dia2 = fe.getDate();
const mes2 = fe.getMonth();
const ano2 = fe.getFullYear();

const day = dia2 + "/" + mes2 + "/" + ano2;

function restaFechas(f1, f2) {
    var aFecha1 = f1.split('/');
    var aFecha2 = f2.split('/');
    var fFecha1 = Date.UTC(aFecha1[2], aFecha1[1] - 1, aFecha1[0]);
    var fFecha2 = Date.UTC(aFecha2[2], aFecha2[1] - 1, aFecha2[0]);
    var dif = fFecha2 - fFecha1;
    var dias = Math.floor(dif / (1000 * 60 * 60 * 24));
    return dias;
}

console.log(restaFechas(dia1, day));

//13. Crea un script que retorni la data actual amb el següent format
// 17/6/2022, 8:43:49
console.log(dia + "/" + mes + "/" + ano + ", " + hora + ":" + min + ":" + sec);
