//1.Crea una funció constructora Llibres() amb els següents paràmetres.
// Funció constructora
function Llibres(titol, pagines, tematica, nomAutor, cognomAutor) {
    this.titol = titol;
    this.pagines = pagines;
    this.tematica = tematica;
    this.nomAutor = nomAutor;
    this.cognomAutor = cognomAutor;
}

// Afegir mètode info() al prototype
Llibres.prototype.info = function () {
    return `${this.titol}, ${this.pagines} pàg. ${this.tematica}, ${this.nomAutor} ${this.cognomAutor}`;
};

// Crear una instància
const llibre1 = new Llibres("El Quijote de la Mancha", 650, "Novel·la", "Miguel", "Cervantes");
console.log(llibre1.info());
// Output: "El Quijote de la Mancha, 650 pàg. Novel·la, Miguel Cervantes"

// Afegir propietat valoracio i mètode rating() al prototype
Llibres.prototype.valoracio = 0;

Llibres.prototype.rating = function () {
    return `${this.titol} - Valoració: ${this.valoracio}`;
};

// Crear dues instàncies
const llibre2 = new Llibres("1984", 328, "Distopia", "George", "Orwell");
const llibre3 = new Llibres("Cent anys de solitud", 471, "Realisme màgic", "Gabriel", "García Márquez");

console.log(llibre2.rating()); // "1984 - Valoració: 0"
console.log(llibre3.rating()); // "Cent anys de solitud - Valoració: 0"

// Modificar valoracio en les instàncies individuals
llibre2.valoracio = 5;
llibre3.valoracio = 4;

console.log(llibre2.rating()); // "1984 - Valoració: 5"
console.log(llibre3.rating()); // "Cent anys de solitud - Valoració: 4"

// Afegir valoracio com a "own property" en la funció constructora
function LlibresModificat(titol, pagines, tematica, nomAutor, cognomAutor) {
    this.titol = titol;
    this.pagines = pagines;
    this.tematica = tematica;
    this.nomAutor = nomAutor;
    this.cognomAutor = cognomAutor;
    this.valoracio = 3; // Own property
}

LlibresModificat.prototype = Llibres.prototype;

const llibre4 = new LlibresModificat("La plaça del Diamant", 220, "Novel·la", "Mercè", "Rodoreda");
const llibre5 = new LlibresModificat("Tirant lo Blanc", 1088, "Novel·la cavalleresca", "Joanot", "Martorell");

console.log(llibre4.rating()); // "La plaça del Diamant - Valoració: 3"
console.log(llibre5.rating()); // "Tirant lo Blanc - Valoració: 3"

// Modificar valoracio individual
llibre4.valoracio = 5;
console.log(llibre4.rating()); // "La plaça del Diamant - Valoració: 5"
console.log(llibre5.rating()); // "Tirant lo Blanc - Valoració: 3"


//2.Crea una funció que recorri la instància creada ue mitjançant hasOwnProperty() o propertyIsEnumerable():
// Funció per mostrar own properties
function mostrarOwnProperties(objecte) {
    console.log("=== OWN PROPERTIES ===");
    for (let propietat in objecte) {
        if (objecte.hasOwnProperty(propietat)) {
            console.log(`${propietat}: ${objecte[propietat]}`);
        }
    }
}

// Funció per mostrar prototype properties
function mostrarPrototypeProperties(objecte) {
    console.log("=== PROTOTYPE PROPERTIES ===");
    for (let propietat in objecte) {
        if (!objecte.hasOwnProperty(propietat)) {
            console.log(`${propietat}: ${typeof objecte[propietat]}`);
        }
    }
}

// Provar amb llibre4
console.log("\n--- Llibre 4 ---");
mostrarOwnProperties(llibre4);
mostrarPrototypeProperties(llibre4);

console.log("\n--- Llibre 2 (sense own property valoracio) ---");
mostrarOwnProperties(llibre2);
mostrarPrototypeProperties(llibre2);




//3.Herència per Prototypes

// Constructor base: Vehicle
function Vehicle(dades) {
    this.marca = dades.marca;
    this.model = dades.model;
    this.matricula = dades.matricula;
    this.color = dades.color;
    this.combustible = dades.combustible;
    this.disponibilitat = false;
}

Vehicle.prototype.mostrarCaracteristiques = function () {
    return `Vehicle: ${this.marca} ${this.model}, Matrícula: ${this.matricula}, Color: ${this.color}, Combustible: ${this.combustible}`;
};

Vehicle.prototype.teDisponibilitat = function () {
    return this.disponibilitat ? "Vehicle disponible" : "Vehicle no disponible";
};

// Constructor: QuatreRodes (hereda de Vehicle)
function QuatreRodes(dades, numRodes, tipusCarnet) {
    Vehicle.call(this, dades); // Cridar al constructor pare
    this.numRodes = numRodes;
    this.tipusCarnet = tipusCarnet;
}

QuatreRodes.prototype = Object.create(Vehicle.prototype);
QuatreRodes.prototype.constructor = QuatreRodes;

// Constructor: Cotxe (hereda de QuatreRodes)
function Cotxe(dades, nPlaces) {
    QuatreRodes.call(this, dades, 4, "B");
    this.tipusVehicle = "cotxe";
    this.nPlaces = nPlaces;
}

Cotxe.prototype = Object.create(QuatreRodes.prototype);
Cotxe.prototype.constructor = Cotxe;

// Constructor: Furgoneta (hereda de QuatreRodes)
function Furgoneta(dades, nPlaces, pesCarrega) {
    QuatreRodes.call(this, dades, 4, "B");
    this.tipusVehicle = "furgoneta";
    this.nPlaces = nPlaces;
    this.pesCarrega = pesCarrega;
}

Furgoneta.prototype = Object.create(QuatreRodes.prototype);
Furgoneta.prototype.constructor = Furgoneta;

// Constructor: DuesRodes (hereda de Vehicle)
function DuesRodes(dades, numRodes, tipusCarnet) {
    Vehicle.call(this, dades);
    this.numRodes = numRodes;
    this.tipusCarnet = tipusCarnet;
}

DuesRodes.prototype = Object.create(Vehicle.prototype);
DuesRodes.prototype.constructor = DuesRodes;

// Constructor: Moto (hereda de DuesRodes)
function Moto(dades) {
    DuesRodes.call(this, dades, 2, "A");
    this.tipusVehicle = "moto";
}

Moto.prototype = Object.create(DuesRodes.prototype);
Moto.prototype.constructor = Moto;

// Constructor: Bicicleta (hereda de DuesRodes)
function Bicicleta(dades, esElectrica) {
    DuesRodes.call(this, dades, 2, "No requerit");
    this.tipusVehicle = "bicicleta";
    this.esElectrica = esElectrica;
}

Bicicleta.prototype = Object.create(DuesRodes.prototype);
Bicicleta.prototype.constructor = Bicicleta;

// EXEMPLES D'ÚS
console.log("\n=== PROVES D'HERÈNCIA ===\n");

// Crear un cotxe
const cotxe1 = new Cotxe({
    marca: "Seat",
    model: "Ibiza",
    matricula: "1234-ABC",
    color: "Vermell",
    combustible: "Gasolina"
}, 5);

console.log(cotxe1.mostrarCaracteristiques());
console.log(`Tipus: ${cotxe1.tipusVehicle}, Places: ${cotxe1.nPlaces}, Rodes: ${cotxe1.numRodes}`);
console.log(cotxe1.teDisponibilitat());

// Crear una furgoneta
const furgoneta1 = new Furgoneta({
    marca: "Mercedes",
    model: "Sprinter",
    matricula: "5678-DEF",
    color: "Blanc",
    combustible: "Dièsel"
}, 3, 1500);

furgoneta1.disponibilitat = true;
console.log("\n" + furgoneta1.mostrarCaracteristiques());
console.log(`Tipus: ${furgoneta1.tipusVehicle}, Places: ${furgoneta1.nPlaces}, Pes càrrega: ${furgoneta1.pesCarrega}kg`);
console.log(furgoneta1.teDisponibilitat());

// Crear una moto
const moto1 = new Moto({
    marca: "Yamaha",
    model: "MT-07",
    matricula: "9012-GHI",
    color: "Negre",
    combustible: "Gasolina"
});

console.log("\n" + moto1.mostrarCaracteristiques());
console.log(`Tipus: ${moto1.tipusVehicle}, Rodes: ${moto1.numRodes}, Carnet: ${moto1.tipusCarnet}`);

// Crear una bicicleta
const bici1 = new Bicicleta({
    marca: "Trek",
    model: "FX 3",
    matricula: "N/A",
    color: "Blau",
    combustible: "Cap"
}, true);

console.log("\n" + bici1.mostrarCaracteristiques());
console.log(`Tipus: ${bici1.tipusVehicle}, És elèctrica: ${bici1.esElectrica ? "Sí" : "No"}`);

// Verificar la cadena de prototips
console.log("\n=== VERIFICACIÓ D'HERÈNCIA ===");
console.log("cotxe1 instanceof Cotxe:", cotxe1 instanceof Cotxe);
console.log("cotxe1 instanceof QuatreRodes:", cotxe1 instanceof QuatreRodes);
console.log("cotxe1 instanceof Vehicle:", cotxe1 instanceof Vehicle);
console.log("moto1 instanceof Moto:", moto1 instanceof Moto);
console.log("moto1 instanceof DuesRodes:", moto1 instanceof DuesRodes);
console.log("moto1 instanceof Vehicle:", moto1 instanceof Vehicle);