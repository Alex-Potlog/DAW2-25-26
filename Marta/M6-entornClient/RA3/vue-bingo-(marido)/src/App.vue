<template>
  <BingoCard :numerosExtraidos="numerosExtraidos" />
  <NumberFrame @nuevo-numero="agregarNumero" />
</template>

<script setup>
import { ref } from 'vue';

import BingoCard from './BingoCard.vue';
import NumberFrame from './NumberFrame.vue';

const numerosExtraidos = ref([]);

function agregarNumero(n) {
  if (!numerosExtraidos.value.includes(n)) {
    numerosExtraidos.value.push(n);
  }
}
</script>

<style lang="scss">
#app {
  font-family: Arial, Helvetica, sans-serif;
  max-width: 60rem;
  margin: 0 auto;
  font-size: 1.5rem;
}
</style>