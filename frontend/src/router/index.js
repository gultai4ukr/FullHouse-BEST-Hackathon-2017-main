import Vue from 'vue'
import Router from 'vue-router'
import indexCategory from '../components/categoryIndex/indexCategory'
import IndexPage from '../components/indexPage/index'
import otherCatgories from '../components/categoryIndex/otherCategory'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/categories',
      component: indexCategory
    }, {
      path: '/',
      component: IndexPage
    }, {
      path: '/categories/:id',
      component: otherCatgories
    }
  ]
})
