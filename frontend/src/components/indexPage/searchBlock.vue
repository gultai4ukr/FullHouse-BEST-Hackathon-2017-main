<template>
  <div class="searchBlock">
    <input v-model="searchQuery" />
  </div>
</template>

<script>
let initParam = {
  queryParam: ''
}

export default {
  data () {
    return {
      searchQuery: '',
    }
  },
  watch: {
    searchQuery: function (val) {
      this.$store.commit('setQuery', val)
      /*initParam.queryParam = this.$store.getters.query;
      this.$http.get('').then(res => {
        console.log(res);
      }).catch(e => console.log(e))*/
    }
  }
}
</script>

<style scoped>

</style>
