<script setup>
import { ref } from 'vue'
import { getHello } from '@/services/helloService'
import HelloResult from '@/components/HelloResult.vue'

// Estado de la vista
const name = ref('')
const message = ref('')
const error = ref('')
const loading = ref(false)

// Acción: se ejecuta al enviar el formulario
async function saludar() {
    loading.value = true
    error.value = ''
    message.value = ''
    try {
        message.value = await getHello(name.value)
    } catch (e) {
        error.value = 'No se ha podido contactar con el backend. ¿Está arrancado?'
        console.error(e)
    } finally {
        loading.value = false
    }
}
</script>

<template>
    <section class="hello">
        <h1>Hello World</h1>
        <form class="hello__form" @submit.prevent="saludar">
            <label for="name">Tu nombre (opcional)</label>
            <input id="name" v-model="name" type="text" placeholder="Ana" />
            <button type="submit" :disabled="loading">
            {{ loading ? 'Cargando…' : 'Saludar' }}
            </button>
        </form>

        <HelloResult :message="message" :error="error" />
    </section>
</template>

<style scoped>
:focus-visible {
    outline: 2px solid var(--color-primary);
    outline-offset: 3px;
}
    .hello__form {
        display: flex;
        flex-direction: column;
        gap: var(--space-s);
        max-width: 320px;
    }
    body {
    font-family: var(--font-family);
    font-size: var(--font-size-body);
    color: var(--color-on-surface);
    background-color: var(--color-surface);
}

h1 {
    font-size: var(--font-size-title);
    font-weight: 700;
}

button {
    font-family: var(--font-family);
    font-size: var(--font-size-body);
    font-weight: 500;
}
    input {
        padding: var(--space-s) var(--space-m);
        border: 1px solid var(--color-on-surface);
        border-radius: var(--radius-m);
        font: inherit;
    }

    button {
        padding: var(--space-s) var(--space-l);
        border: none;
        border-radius: var(--radius-m);
        background: var(--color-primary);
        color: var(--color-on-primary);
        font: inherit;
        cursor: pointer;
    }
    button:disabled {
        opacity: 0.6;
        cursor: wait;
    }
</style>