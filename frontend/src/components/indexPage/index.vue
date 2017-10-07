<template>
  <div class="indexPage">
    <SearchBlock></SearchBlock>
  </div>
</template>

<script>
import SearchBlock from './searchBlock'

export default {
  data () {
    return {
      smth: ''
    }
  },
  components: {
    SearchBlock
  }
}
</script>

<style scoped>

</style>
