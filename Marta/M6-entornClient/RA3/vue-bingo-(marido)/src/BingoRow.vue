<template>
  <tr>
    <BingoCell
      v-for="(cell, index) in row"
      :key="index"
      :value="cell"
      :numerosExtraidos="numerosExtraidos"
    />
  </tr>
</template>

<script setup>
import BingoCell from './BingoCell.vue'
defineProps({
  row: Array,
  numerosExtraidos: Array,
})
</script>
