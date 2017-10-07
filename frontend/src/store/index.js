import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const store = new Vuex.Store({
  state: {
    searchQuery: '',
    keywordsResults: [],
    showCategory: false,
    showResults: false,
    results: []
  },
  mutations: {
    setQuery (state, value) {
      state.searchQuery = value
    },
    setResults (state, value) {
      state.results = value
    },
    showResultsBlock (state) {
      state.showResults = !state.showResults
    },
    setKeywordsResults (state, value) {
      state.keywordsResults = value
    }
  },
  getters: {
    query (state) {
      return state.searchQuery
    },
    showResults (state) {
      return state.showResults
    },
    keywordsResults (state) {
      return state.keywordsResults
    }
  },
  actions: {
    searchByKeyword ({ commit }, query) {
      console.log('called API')
      const keys = '?FOURSQUARE_CLIENT_ID=ZPE3IBJSHLWPLC1TGFRQJNV4C3LPJ2FMQ2H3Y5UJ5K5A3FEA?FOURSQUARE_CLIENT_SECRET=CPYVSTMRCV32XVMA3MELMP5HQRQZ3WHQCR0G3BX5U0Q5HWNI'
      const url = `https://api.foursquare.com/v2/venues/`
      let result = ''

      Vue.http.get(url).then((res => {
        result = res.body
        console.log(result)
        //commit('setKeywordsResults', result)
      })).catch(err => {
        console.log(err)
      })
    }
  }
})

export default store
