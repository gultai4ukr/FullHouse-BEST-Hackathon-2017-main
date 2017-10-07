<template>
  <div class="indexPage">
    <!-- v-if="categories"-->
    <SearchBlock></SearchBlock>
    <ResultBlock v-if="showResults"></ResultBlock>
  </div>
</template>

<script>
  //Imports
import SearchBlock from './searchBlock'
import ResultBlock from './results'
import { mapGetters } from 'vuex'

export default {
  data () {
    return {
    }
  },
  created () {
     // showResults: false
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
