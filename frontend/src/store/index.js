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
      const url = `http://konchytsv.pythonanywhere.com/search/events/?keyword=`
      let result = ''

      Vue.http.get(url + query).then((res => {
        result = res.body.response.venues
        commit('setKeywordsResults', result)
      })).catch(err => {
        console.log(err)
      })
    }
  }
})

export default store
