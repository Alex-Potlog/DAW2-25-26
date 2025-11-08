<template>
  <td :class="{ empty: isEmpty, marcado: isMarked }">
    {{ isEmpty ? '' : value }}
  </td>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  value: {
    type: [Number, null],
    default: null,
  },
  numerosExtraidos: {
    type: Array,
    default: () => [],
  },
})

const isEmpty = computed(() => props.value === null)
const isMarked = computed(
  () => props.value !== null && props.numerosExtraidos.includes(props.value),
)
</script>

<style lang="scss" scoped>
td {
  border: 2px solid #333;
  width: 60px;
  height: 60px;
  text-align: center;
  font-weight: bold;
  font-size: 1.5rem;
  background-color: #fff;
  color: #333;
  transition: all 0.2s ease-in-out;

  &:hover {
    background-color: #f0c040;
    transform: scale(1.1);
    cursor: pointer;
  }

  &.empty {
    background-color: #000;
    color: #000;

    &:hover {
      background-color: #000;
      transform: none;
    }
  }

  &.marcado {
    background-color: #007900;
    color: #fff;
  }
}
</style>
