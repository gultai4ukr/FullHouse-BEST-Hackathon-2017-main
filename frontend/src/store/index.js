import Vue from 'vue'
import Vuex from 'vuex'
//import VueResource from 'vue-resource'

//Vue.use(VueResource)
Vue.use(Vuex)

const store = new Vuex.Store({
  state: {
    searchQuery: ''
  },
  mutations: {
    setQuery (state, value) {
      console.log('Called setQuery')
      state.searchQuery = value
    }
  },
  getters: {
    query (state) {
      return state.searchQuery
    }
  },
  actions: {
    // search ({ commit }, query) {
    //   const url = `https://en.wikipedia.org/w/api.php?action=opensearch&search=${query}`
    //   let result = ''
      
    //   Vue.http.jsonp(url).then((res => {
    //     result = res.body
    //     commit('SET', result)
    //   })).catch(err => {
    //     console.log(err)
    //   })
    // }
  }
})

export default store
