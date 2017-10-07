<template>
  <div class="resultsBlock">
    <div v-for="result in filteredResults">
      <div class="resultBlock">
        
        <img v-bind:src="result.img" />
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
      filteredResults: ''
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
    }
  },
  watch: {
    results: function (val) {
      this.filterImages(val)
    }
  },
  methods: {
    filterImages: function (objects) {
      for (let i = 0; i < objects.length; i++) {
        objects[i].img = "https://image.jimcdn.com/app/cms/image/transf/none/path/s38008646b8c4413d/image/ib1787d70c86e8c6b/version/1494078317/image.png"
        //else objects[i].img = objects[i].image.medium.url
        objects[i].description = objects[i].description.substring(0, 100)
      }
      this.filteredResults = objects
    }
  }
}
</script>

<style scoped>
.title {
  font-weight: 500;
  text-align: left;
  color: #1da2d3;
  margin: 1%;
  font-size: 1.3rem;
  margin: 15px;
}

.description {
  text-overflow: ellipsis;
  white-space: wrap;
  overflow: hidden;
  padding: 10px;
}

.resultsBlock {
  columns: 4;
  column-gap: 1;
  background-color: #fff;
  text-align: center;
}

.resultBlock {
  font-family: Montserrat;
  margin: 5% auto;
  border: none;
  background-color: #F5F7F9;
  -webkit-box-shadow: 0px 4px 15px -1px rgba(140,160,183,1);
  -moz-box-shadow: 0px 4px 15px -1px rgba(140,160,183,1);
  box-shadow: 0px 4px 15px -1px rgba(140,160,183,1);
  display: inline-block;
  width: 90%;
  vertical-align: top;
}

.resultBlock img {
  width: 100%;
}
</style>
