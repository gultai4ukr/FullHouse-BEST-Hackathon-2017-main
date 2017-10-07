<template>
  <div class="main">
    <div @queryChange="getQuery($event)">
      {{ queryResult }}
    </div>
  </div>
</template>

<script>
import Vue from 'vue'

export default {
  data () {
    return {
      queryResult: ''
    }
  },
  created() {
    test.$on("queryChange", function(val) {
      console.log(val)
    })
  }
}

// Main.$on('queryChange', function (newQuery) {
//   this.queryResult = newQuery
// })

//export default Main
</script>

<style scoped>

</style>
