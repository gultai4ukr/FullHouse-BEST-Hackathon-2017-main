<template>
  <div class="indexPage">
    <!-- v-if="categories"-->
    <SearchBlock></SearchBlock>
    <Categories v-if=""></Categories>
    <ResultBlock v-if="showResults"></ResultBlock>
  </div>
</template>

<script>
  //Imports
import SearchBlock from './searchBlock'
import Categories from './categories'
import ResultBlock from './results'
import { mapGetters } from 'vuex'

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
     // showResults: false
    }
  },
  components: {
    SearchBlock, ResultBlock
  },
  computed: {
    ...mapGetters({
      showResults: 'showResults'
    })
  }
}
</script>

<style scoped>

</style>
