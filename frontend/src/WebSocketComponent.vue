<template>
  <div>
    <input v-model="message" @keyup.enter="sendMessage">
    <button @click="sendMessage">Send</button>
    <ul>
      <li v-for="msg in messages" :key="msg">{{ msg }}</li>
    </ul>
  </div>
</template>

<script>
export default {
  data() {
    return {
      message: '',
      messages: [],
      socket: null,
    };
  },
  mounted() {
    this.socket = new WebSocket('ws://localhost:3000');
    this.socket.onmessage = (event) => {
      this.messages.push(event.data);
    };
    this.message = "TESTST"
    // while (this.socket.readyState == 0) {
    //   this.message = "test"
    // }
    // this.socket.send(this.message);
  },
  methods: {
    sendMessage() {
      console.log(this.socket)
      this.socket.send(this.message);
      this.message = '';
      // if (this.message.trim() !== '') {
      //   this.socket.send(this.message);
      //   this.message = '';
      // }
    },
  },
};
</script>