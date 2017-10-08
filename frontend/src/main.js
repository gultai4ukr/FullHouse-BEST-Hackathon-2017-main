import Vue from 'vue'
import App from './App'
import Vuex from 'vuex'
import store from './store'
import VueResource from 'vue-resource'
import 'vue-awesome/icons'

import Icon from 'vue-awesome/components/Icon'
Vue.component('icon', Icon)

Vue.use(Vuex)
Vue.use(VueResource)
import router from './router'

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  render: h => h(App)
})
