<template>

  <div class="indexPage">
    <HeaderMenu></HeaderMenu>
    <SearchBlock></SearchBlock>
    <ResultBlock v-if="showResults"></ResultBlock>
  </div>
</template>

<script>
import SearchBlock from './searchBlock'
import ResultBlock from './results'
import HeaderMenu from './HeaderMenu'
import { mapGetters } from 'vuex'

export default {
  data () {
    return {

    }
  },
  components: {
    SearchBlock, ResultBlock, HeaderMenu
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
