<template>
  <div class="indexPage">
    <SearchBlock></SearchBlock>
    <ResultBlock v-if="showResults"></ResultBlock>
  </div>
</template>

<script>
import SearchBlock from './searchBlock'
import ResultBlock from './results'
import { mapGetters } from 'vuex'

export default {
  data () {
    return {
 
    }
  },
  components: {
    SearchBlock, ResultBlock
  },
  computed: {
    ...mapGetters({
      showResults: 'keywordsResults'
    })
  }
}
</script>

<style scoped>

</style>
