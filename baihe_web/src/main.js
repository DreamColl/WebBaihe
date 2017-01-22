// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import routes from './config/routes'
import VueRouter from 'vue-router'

/* eslint-disable no-new */

Vue.use(VueRouter)

const router = new VueRouter({ routes })

router.beforeEach((to, from, next) => {
  next()
})

new Vue({
  el: '#app',
  router,
  render: h => h(App)
})
