<template>
  <div>
  <div @click="getParam('?category=music')">Music</div>
  <div @click="getParam('?category=sports')">Sport</div>
  <div v-for="item in this.$store.state.categoriesList">
    <div>{{ item.title }}</div>
    <div class="description">{{ item.description }}</div>
  </div>
  </div>
</template>

<script>
  //Imports
  import VueResource from 'vue-resource'
  import Vue from 'vue'

  Vue.use(VueResource)
  export default {
    data () {
      return {
        categories: []
      }
    },
    methods: {
      getParam(param) {
        this.$store.dispatch('searchCategory', param)
      }
    },
  }
</script>

<style scoped>
.description {
  border-color: red;
}
</style>
