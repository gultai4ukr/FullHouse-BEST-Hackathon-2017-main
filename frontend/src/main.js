import Vue from 'vue'
import App from './App'
import Vuex from 'vuex'
import store from './store'

Vue.use(Vuex)
//Vue.use(VueResource)
import router from './router'

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  render: h => h(App)
})
