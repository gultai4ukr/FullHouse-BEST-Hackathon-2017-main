<template>
  <div class="filter">
    <input v-model="query" placeholder="query" />
  </div>
</template>

<script>
export default {
  data () {
    return {
      query: ''
    }
  },
  watch: {
    query: function (val) {
      this.$store.commit('setQuery', val)
      console.log(this.$store.getters.query)
    }
  }
}
</script>

<style scoped>

</style>
