# Apuntes de JavaScript

## 1. Tipos de Datos y Operadores

### Verificación de Tipos
```javascript
typeof variable // Devuelve el tipo de dato como string
```

**Tipos principales:**
- `'string'` - Cadenas de texto
- `'number'` - Números (enteros y decimales)
- `'boolean'` - true/false
- `'undefined'` - Variable sin valor asignado
- `'object'` - Objetos, arrays, null
- `'function'` - Funciones

### Métodos de Números
```javascript
const num = 34.666666;
num.toFixed(2); // "34.67" - Redondea a 2 decimales
```

## 2. Strings (Cadenas de Texto)

### Métodos Principales
```javascript
const texto = "Hola Mundo";

// Transformación
texto.toLowerCase();     // "hola mundo"
texto.toUpperCase();     // "HOLA MUNDO"
texto.replaceAll(' ', '-'); // "Hola-Mundo"

// Extracción
texto.charAt(0);         // "H"
texto.slice(1);          // "ola Mundo"
texto.split(' ');        // ["Hola", "Mundo"]

// Combinación
texto.concat(" !!!");    // "Hola Mundo !!!"
```

### Ejemplo Práctico
```javascript
const titles = ['La casa de papel', 'La catedral del mar'];
for (let i = 0; i < titles.length; i++) {
    titles[i] = titles[i].replaceAll(' ', '-').toLowerCase();
}
// Resultado: ['la-casa-de-papel', 'la-catedral-del-mar']
```

## 3. Arrays (Listas)

### Métodos Comunes
```javascript
const arr1 = [1, 2, 3];
const arr2 = [4, 5, 6];

// Combinar arrays
arr1.concat(arr2);       // [1, 2, 3, 4, 5, 6]

// Recorrer arrays
arr1.forEach(elemento => {
    console.log(elemento);
});

// Propiedades
arr1.length;             // 3
```

### Validación de Contenido
```javascript
const arr = ["", null, undefined, "Hola"];

for (let i = 0; i < arr.length; i++) {
    if (arr[i]) {
        console.log("Tiene contenido");
    } else if (arr[i] === null) {
        console.log("Es null");
    } else if (arr[i] === undefined) {
        console.log("Es undefined");
    } else {
        console.log("No tiene contenido"); // String vacío
    }
}
```

### Suma de Números en Array Mixto
```javascript
const arr = [3, false, 7, 'Maria', 9];
let suma = 0;

for (let i = 0; i < arr.length; i++) {
    if (typeof arr[i] === 'number') {
        suma += arr[i];
    }
}
console.log(suma); // 19
```

## 4. Fechas (Date)

### Crear y Mostrar Fechas
```javascript
const fecha = new Date();

// Mostrar fecha formateada
fecha.toLocaleString(); // "21/10/2025, 14:30:45"
```

### Calcular Día del Año
```javascript
const hoy = new Date();
const inicioAno = new Date(hoy.getFullYear(), 0, 1);
const diferencia = hoy - inicioAno;
const unDia = 1000 * 60 * 60 * 24; // milisegundos en un día
const diaDelAno = Math.ceil(diferencia / unDia);

console.log(`Hoy es el día ${diaDelAno} del año`);
```

### Comparar Fechas
```javascript
function compareTo(fecha1, fecha2) {
    if (fecha1.getDate() === fecha2.getDate()) {
        return 0;  // Iguales
    }
    if (fecha1.getDate() < fecha2.getDate()) {
        return -1; // fecha1 es anterior
    }
    return 1;      // fecha1 es posterior
}
```

## 5. Manipulación del DOM

### Crear Elementos
```javascript
const elemento = document.createElement("tagName");

// Ejemplo: crear input
const input = document.createElement("input");
input.type = "email";
input.name = "email";
input.placeholder = "Ingresa tu email";
input.required = true;
```

### Atributos y Clases
```javascript
// Agregar/modificar atributos
elemento.id = "miId";
elemento.setAttribute("data-info", "valor");

// Eliminar atributos
elemento.removeAttribute("id");

// Clases CSS
elemento.classList.add("clase1");
elemento.classList.remove("clase2");
```

### Agregar al DOM
```javascript
// Agregar hijo
document.body.appendChild(elemento);

// Insertar HTML
elemento.innerHTML = "<p>Contenido</p>";
elemento.textContent = "Texto simple";

// Insertar en posición específica
elemento.insertAdjacentHTML("beforeend", "<div>Nuevo</div>");
```

### Seleccionar Elementos
```javascript
// Selección única
document.querySelector(".clase");
document.querySelector("#id");

// Selección múltiple
document.querySelectorAll(".clase");
```

## 6. Formularios Dinámicos

### Crear Formulario Completo
```javascript
function crearFormulario() {
    const form = document.createElement('form');
    form.action = '#';
    form.method = 'post';
    form.id = 'user-data';
    
    // Input
    const input = document.createElement('input');
    input.type = "email";
    input.name = "email";
    input.classList.add("form-control");
    form.appendChild(input);
    
    // Botón
    const boton = document.createElement('button');
    boton.type = "submit";
    boton.innerHTML = "Enviar";
    form.appendChild(boton);
    
    document.body.appendChild(form);
}
```

### Crear Menú de Navegación
```javascript
function crearMenu() {
    const opciones = ['home', 'about', 'products', 'contact'];
    const nav = document.createElement('nav');
    const lista = document.createElement('ul');
    
    opciones.forEach(opcion => {
        const li = document.createElement('li');
        const enlace = document.createElement('a');
        
        enlace.href = opcion + '.html';
        enlace.innerHTML = opcion.charAt(0).toUpperCase() + opcion.slice(1);
        
        li.appendChild(enlace);
        lista.appendChild(li);
    });
    
    nav.appendChild(lista);
    document.body.appendChild(nav);
}
```

## 7. Eventos

### Event Listeners
```javascript
// Agregar evento
elemento.addEventListener('click', function(event) {
    console.log('Click detectado');
});

// Evento change para inputs
input.addEventListener('change', function(event) {
    const valor = event.target.value;
    console.log('Nuevo valor:', valor);
});

// Evento al cargar página
window.onload = function() {
    console.log('Página cargada');
};
```

### Data Attributes
```javascript
// Establecer
elemento.dataset.precio = "10.50";

// Obtener
const precio = parseFloat(elemento.dataset.precio);
```

## 8. Bucles

### For Clásico
```javascript
for (let i = 0; i < array.length; i++) {
    console.log(array[i]);
}
```

### ForEach
```javascript
array.forEach(elemento => {
    console.log(elemento);
});
```

### For...of
```javascript
for (const elemento of array) {
    console.log(elemento);
}
```

## 9. Funciones

### Declaración
```javascript
function nombre(parametro1, parametro2) {
    return parametro1 + parametro2;
}
```

### Arrow Functions
```javascript
const suma = (a, b) => a + b;

const saludar = nombre => {
    console.log(`Hola ${nombre}`);
};
```

## 10. Conversión de Tipos

```javascript
// String a Number
parseInt("123");      // 123
parseFloat("123.45"); // 123.45
Number("123");        // 123

// Number a String
(123).toString();     // "123"
String(123);          // "123"
```

## 11. Operadores de Comparación

```javascript
// Igualdad estricta (tipo y valor)
=== 
!==

// Igualdad débil (solo valor)
==
!=

// Comparación
< > <= >=
```

## Consejos Prácticos

1. **Usa `const` y `let`**, evita `var`
2. **Verifica tipos** antes de operar: `typeof variable`
3. **Valida datos** de formularios antes de procesar
4. **Usa template literals** para concatenar: `` `Hola ${nombre}` ``
5. **Maneja errores** con try-catch en operaciones sensibles
6. **Nombra variables** de forma descriptiva
7. **Comenta código complejo** para futuras referencias