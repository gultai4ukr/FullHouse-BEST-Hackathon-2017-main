<template>
  <div id="app">
    <FilterBlock></FilterBlock>
  </div>
</template>

<script>
import Vue from 'vue'
import FilterBlock from './components/Filter.vue'
//import MainBlock from './components/Main.vue'

export default {
  name: 'App',
  components: {
    FilterBlock
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
