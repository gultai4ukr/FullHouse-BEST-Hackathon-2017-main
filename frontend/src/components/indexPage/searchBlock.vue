<template>
  <div class="searchBlock">
    <input v-model="searchQuery" class="searchBox" placeholder="Type anything. Literally." @keyup.enter="search"/>
       <button class="button-go">
         <img src="../../icons/go.svg" class="icon-go">
         Go
      </button>
  </div>
</template>

<script>
export default {
  data () {
    return {
      searchQuery: ''
    }
  },
  methods: {
    search: function () {
      this.$store.commit('showResultsBlock')
      this.$store.commit('setQuery', this.searchQuery)
      console.log(this.$store.getters.query)
    }
  }
}
</script>

<style scoped>
.searchBlock {
  margin: 15% auto;
  display: block;
  width: 40%;
  border-radius: 100px;
  background-color: #f6f9fd;
  box-shadow: 0 18px 44px 2px rgba(0, 0, 0, 0.27);
  padding-left: 1.5%;
  padding-right: 1.5%;
  font-family: Montserrat;
  font-size: 24px;
  text-align: left;
  border: none;
  color: #9b9b9b;
  z-index: 110;
}

.searchBox {
  width: 70%;
  outline: none;
  border: none;
  margin: 2%;
  padding: 2%;
  font-size: 1.1rem;
  background-color: #f6f9fd;
}

textarea:focus, input:focus{
  outline: none;
}

.searchBox input {
  display: inline-block;
  vertical-align: middle;
}

.button-go {
  height: 100%;
  width: 20%;
  position: relative;
  color: #fff;
  font-size: 1.3rem;
  border-radius: 100px;
  background-color: #189dcd;
  border: none;
  padding-top: 1.5%;
  padding-bottom: 2%;
  outline: none;
  cursor: pointer;
  transition: .5s;
}
.button-go:hover {
  background-color: #1d85aa;
}

.icon-go {
  object-fit: contain;
  vertical-align: middle;
}
</style>
