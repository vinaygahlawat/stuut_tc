<!--<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
</script>
-->
<template>
  <div class="container">
    <header>
      <div class="wrapper">
        <h1>Stuut</h1>
        <nav>
          <RouterLink to="/">Home</RouterLink>
          <RouterLink to="/about">About</RouterLink>
        </nav>
      </div>
    </header>

    <div class="content">
      <RouterView />
    </div>
    <div>
      <h1>Stock Search</h1>
      <input v-model="symbol" @keydown.enter="searchStock" placeholder="Search for stock" />
      <button @click="searchStock">Search</button>
      <h2>Closing Price: {{ this.info }}</h2>
    </div>
  </div>

</template>

<script>
  export default {
    data() {
      return {
        info: [],
        symbol: "",
      };
    },
    mounted() {
      this.searchStock();
    },
    methods: {
      searchStock() {
        console.log(this.symbol);
        fetch(`http://127.0.0.1:5000//api/ticker/${this.symbol}`)
          .then((response) => response.json())
          .then((data) => {
            this.info = data["previousClose"];
            console.log(this.info);
          });
      },
    },
  };
</script>

<style scoped>
.container {
  display: flex;
  flex-direction: column;
  align-items: center;
}

header {
  line-height: 1.5;
  max-height: 100vh;
  width: 100%;
  text-align: center;
  display: flex;
  justify-content: center;
  width: 100%;
  top: 0;
  margin-top: 10px;
  margin-bottom: 20px;
}

h1 {
  font-size: 2rem;
}

nav {
  width: 100%;
  font-size: 12px;
  text-align: center;
  margin-top: 2rem;
  margin-bottom: 2rem;
}

nav a.router-link-exact-active {
  color: var(--color-text);
}

nav a.router-link-exact-active:hover {
  background-color: transparent;
}

nav a {
  display: inline-block;
  padding: 0 1rem;
  border-left: 1px solid var(--color-border);
}

nav a:first-of-type {
  border: 0;
}

.content {
  width: 100%;
  display: flex;
  justify-content: center;
  align-self: flex-start;
}
</style>
