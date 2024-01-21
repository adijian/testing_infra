<template>
  <h1>Hello {{data}}</h1>
  <input type="text" v-model="inputData" @keyup.enter="submit()">
  <button @click="submit()">Submit</button>
</template>

<script setup>
import { onMounted, ref } from 'vue'

const data = ref()
const inputData = ref()
const connection = new WebSocket("ws://localhost:8000/ws")

function submit() {
    console.log(`Sent: ${inputData.value}`) // Log the sent data
    connection.send(inputData.value)
    inputData.value = '' // Reset the input field after sending
}

onMounted(() => {
    connection.onmessage = function(e) {
        data.value = e.data
    }
})
</script>

<script>
export default {
  data() {
    return {
    }
  }
}
</script>
