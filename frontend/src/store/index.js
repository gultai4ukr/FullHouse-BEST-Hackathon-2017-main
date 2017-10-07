import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const store = new Vuex.Store({
  state: {
    searchQuery: '',
    keywordsResults: []
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
      const url = `https://konchytsv.pythonanywhere.com/search/events/?keywords=${query}`
      let result = ''

      Vue.http.get(url).then((res => {
        result = res.body
        commit('setKeywordsResults', result)
      })).catch(err => {
        console.log(err)
      })
    }
  }
})

export default store
