

function add(a, b) {
    return a + b;
}

function subtract(a, b) {
    return a - b;
}

function multiply(a, b) {
    return a * b;
}

function divide(a, b) {
    if (b === 0) {
        return 'Cannot divide by zero';
    }
    return a / b;
}

function isEven(num) {
    return num % 2 === 0;
}

function isOdd(num) {
    return num % 2 !== 0;
}

function findMax(arr) {
    return Math.max(...arr);
}

function findMin(arr) {
    return Math.min(...arr);
}

function reverseString(str) {
    return str.split('').reverse().join('');
}

function capitalize(str) {
    return str.charAt(0).toUpperCase() + str.slice(1);
}