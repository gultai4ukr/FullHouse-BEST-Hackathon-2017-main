<template>
  <div class="searchBlock">
    <input v-model="searchQuery"></input>
  </div>
</template>

<script>
export default {
  data () {
    return {
      searchQuery: ''
    }
  },
  watch: {
    searchQuery: function (val) {
      this.$store.commit('setQuery', val)
      console.log(this.$store.getters.query)
    }
  }
}
</script>

<style scoped>

</style>
