<template>
    <button id="sacar-numero" @click="sacarNumero">Sacar número</button>

    <div class="numeros-seleccionados">
        <span v-for="(n, i) in reversedNumeros" :key="i" class="bola">
        {{ n }}
        </span>
    </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { defineEmits } from 'vue'

const emit = defineEmits(['nuevo-numero'])
const numeros = ref([])

// Computed para mostrar los números en orden inverso (último a la izquierda)
const reversedNumeros = computed(() => [...numeros.value].reverse())

function sacarNumero() {
    if (numeros.value.length >= 90) return

    let nuevo
    do {
        nuevo = Math.floor(Math.random() * 90) + 1
    } while (numeros.value.includes(nuevo))

    numeros.value.push(nuevo)
    emit('nuevo-numero', nuevo)
}
</script>

<style lang="scss" scoped>
$color-bg: #f0c040;

#sacar-numero {
    cursor: pointer;
}

.numeros-seleccionados {
    display: flex;
    flex-wrap: wrap;
    gap: 1rem;
    margin: 2rem 0;

    span {
        border: 1px solid black;
        padding: 10px;
        border-radius: 30px;
        width: 30px;
        text-align: center;

        &:first-of-type {
        background-color: $color-bg;
        font-weight: bold;
        }
    }
}
</style>
