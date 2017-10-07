<template>
  <div class="resultsBlock">
    <div v-for="result in results">
      <div class="resultBlock">
        <div class="title">{{ result.title | cutBrackets }}</div>
        <div class="description" v-html="result.description"></div>
        <div class="time">{{ result.time }}</div>
        <div class="location">{{ result.city_name }} {{ result.country_name }}</div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  data () {
    return {
      
    }
  },
  computed: {
    ...mapGetters({
      results: 'keywordsResults'
    })
  },
  filters: {
    cutBrackets: function (value) {
      if (value.match(/"/i)) return value.replace('"', '')
      return value
    },
    cutDescriptions: function (value) {
      return value.substring(0, 100)
    }
  }
}
</script>

<style scoped>
.title {
  font-weight: 700;
  text-align: left;
  color: #1da2d3;
  margin: 1%;
  font-size: 1.5rem;
}

.description {
  text-overflow: ellipsis;
  white-space: wrap;
  overflow: hidden;
}

.resultsBlock {
  position: relative;
  columns: 4;
  column-gap: 0;
}

.resultBlock {
  font-family: Montserrat;
  margin: 3%;
  border: 1px solid #8CA0B7;
  background-color: #F5F7F9;
  -webkit-box-shadow: 0px 4px 15px -1px rgba(140,160,183,1);
  -moz-box-shadow: 0px 4px 15px -1px rgba(140,160,183,1);
  box-shadow: 0px 4px 15px -1px rgba(140,160,183,1);
  display: inline-block;
  width: 100%;
  vertical-align: top;
}
</style>
