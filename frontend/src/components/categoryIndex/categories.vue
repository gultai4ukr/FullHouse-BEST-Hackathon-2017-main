<template>
  <div>
    <div @click="getParam('?category=music')">Music</div>
    <div @click="getParam('?category=sports')">Sport</div>
    <div @click="getParam('?category=comedy')">Comedy</div>
    <div @click="getParam('?category=family_fun_kids')">familyFun</div>
    <div @click="getParam('?category=books')">Books</div>
    <div @click="getParam('?category=attractions')">attractions</div>
    <div @click="getParam('?category=technology')">technology</div>
    <div @click="getParam('?category=business')">business</div>
    <div @click="getParam('?category=community')">community</div>
    <div v-for="item in this.$store.state.categoriesList">
    <div>{{ item.title }}</div>
    <div class="description" v-html=" item.description "></div>
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
    created: function () {
      console.log(this.$route.param)
    }
  }
</script>

<style scoped>
.description {
  border-color: red;
}
</style>
