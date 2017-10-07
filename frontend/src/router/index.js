import Vue from 'vue'
import Router from 'vue-router'
import Categories from '../components/indexPage/categories'
import IndexPage from '../components/indexPage/index'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/categories',
      component: Categories
    }, {
      path: '',
      component: IndexPage
    }
  ]
})
