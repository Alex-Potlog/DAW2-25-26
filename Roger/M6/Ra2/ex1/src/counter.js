export function setupCounter(element) {
  let counter = 0
  const setCounter = (count) => {
    counter = count
    element.innerHTML = `count is ${counter}`
  }
  element.addEventListener('click', () => setCounter(counter + 1))
  setCounter(0)
}


// Error que ESLint corregirà automàticament
function suma(a, b) {
  let x = 10
  let y = 20
  return a + b + x + y
}

console.log(suma(5, 3))