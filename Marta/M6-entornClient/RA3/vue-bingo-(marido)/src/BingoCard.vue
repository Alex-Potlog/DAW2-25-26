<template>
  <div class="bingo-card">
    <table>
      <tbody>
        <BingoRow
          v-for="(row, index) in card"
          :key="index"
          :row="row"
          :numerosExtraidos="numerosExtraidos"
        />
      </tbody>
    </table>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import BingoRow from './BingoRow.vue'

defineProps({ numerosExtraidos: Array })

function generateCard() {
  // Paso 1: Generar 3 números únicos por cada una de las 9 columnas
  const columns = Array.from({ length: 9 }, (_, i) => {
    const min = i === 0 ? 1 : i * 10 // Rango mínimo por columna
    const max = i === 8 ? 90 : min + 9 // Rango máximo por columna
    const nums = []

    // Generar 3 números únicos dentro del rango
    while (nums.length < 3) {
      const num = Math.floor(Math.random() * (max - min + 1)) + min
      if (!nums.includes(num)) nums.push(num)
    }

    // Alternar orden: columnas pares descendente, impares ascendente
    return i % 2 === 0 ? nums.sort((a, b) => a - b) : nums.sort((a, b) => b - a)
  })
  //console.log('columns', JSON.parse(JSON.stringify(columns)))

  // Paso 2: Inicializar matriz vacía 3x9
  const card = Array.from({ length: 3 }, () => Array(9).fill(null))

  // Paso 3: Asignar 2 números a 6 columnas, y 1 número a 3 columnas
  const colIndices = Array.from({ length: 9 }, (_, i) => i)
  const colsWithTwo = colIndices.sort(() => 0.5 - Math.random()).slice(0, 6)

  const colsWithOne = colIndices.filter((i) => !colsWithTwo.includes(i))

  // Contador de números por fila para asegurar que cada una tenga exactamente 5
  const rowCounts = [0, 0, 0]

  // Función auxiliar para colocar números en filas válidas
  function placeNumber(col, count) {
    // Filas disponibles que aún no tienen 5 números y no tienen número en esta columna
    const availableRows = [0, 1, 2].filter((r) => card[r][col] === null && rowCounts[r] < 5)

    for (let i = 0; i < count; i++) {
      // Seleccionar una fila aleatoria entre las disponibles
      const row = availableRows.splice(Math.floor(Math.random() * availableRows.length), 1)[0]

      // Colocar el número en la celda correspondiente
      card[row][col] = columns[col][row]
      rowCounts[row]++
    }
  }

  // Paso 4: Distribuir los números en el cartón respetando las reglas
  colsWithTwo.forEach((col) => placeNumber(col, 2)) // Colocar 2 números en 6 columnas
  colsWithOne.forEach((col) => placeNumber(col, 1)) // Colocar 1 número en 3 columnas

  // El cartón ya cumple todas las reglas: 5 números por fila, 1–2 por columna
  return card
}

const card = ref(generateCard())
</script>

<style lang="scss" scoped>
$bingo-border: #333;
$bingo-bg: #fff;
$empty-bg: #000;
$hover-bg: #f0c040;

table {
  border-collapse: collapse;
  font-size: 1.5rem;
  width: 100%;

  td {
    border: 2px solid $bingo-border;
    width: 60px;
    height: 60px;
    text-align: center;
    font-weight: bold;
    background-color: $bingo-bg;
    color: $bingo-border;
    transition: all 0.2s ease-in-out;

    &:hover {
      background-color: $hover-bg;
      transform: scale(1.1);
      cursor: pointer;
    }

    &.empty {
      background-color: #000;
      color: #000;

      &:hover {
        background-color: #000;
        transform: none;
        cursor: auto;
      }
    }
  }
}
</style>
