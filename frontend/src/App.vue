<template>
  <div id="app">
      <router-view></router-view>
  </div>
</template>

<script>
import Vue from 'vue'
import IndexPage from './components/indexPage'

export default {
  name: 'App',
  components: {
    IndexPage
  }
}
</script>

<style>
@import url('https://fonts.googleapis.com/css?family=Montserrat');

html, body {
  background: linear-gradient(59deg, #08aeea, #2af598) no-repeat center center fixed; 
}
</style>
