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
  background: url(./icons/bg.png) no-repeat center center fixed;
  background-size: 100%;
}
</style>
