import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const store = new Vuex.Store({
  state: {
    searchQuery: '',
    keywordsResults: [],
    hotelsResults: [],
    showCategory: false,
    showResults: false,
    results: [],
    categoriesList: []
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
    },
    setCategories (state, value) {
      state.categoriesList = value
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
    },

    showCategories (state) {
      return state.categoriesList
    }
  },
  actions: {
    searchByKeyword ({ commit }, query) {
      const url = `http://konchytsv.pythonanywhere.com/search/events/?keyword=`
      let result = ''

      Vue.http.get(url + query).then((res => {
        result = res.body
        for (let i = 0; i < result.length; i++) {
          const imgURL = getImage(query)
          result[i].img = imgURL
        }
        commit('setKeywordsResults', result)
      })).catch(err => {
        console.log(err)
      })
    },
    searchCategory: function ({commit}, query) {
      //REQUEST
      const url = `http://konchytsv.pythonanywhere.com/search/events/${query}`
      let categoriesList = '';
      Vue.http.get(url).then((res => {
        categoriesList = res.body;
        commit('setCategories', categoriesList)
      })).catch(err => {
        console.log(err)
      })
    }
  }
})

export default store

function getImage (cat) {
  return `http://loremflickr.com/320/${getRandomInt(210, 258)}/${cat}`
}

function getRandomInt (min, max) {
  return Math.floor(Math.random() * (max - min)) + min
}