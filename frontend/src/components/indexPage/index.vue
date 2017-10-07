<template>
  <div class="indexPage">
    <!-- v-if="categories"-->
    <SearchBlock></SearchBlock>
    <Categories v-if=""></Categories>
  </div>
</template>

<script>
  //Imports
import SearchBlock from './searchBlock'
import Categories from './categories'

export default {
  data () {
    return {
      categories: false
    }
  },
  components: {
    SearchBlock, Categories
  },
  created () {
    this.categories = false;
  }
}
</script>

<style scoped>

</style>
