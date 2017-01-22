export default [
  //  { path: '', name: '', component: resolve => require([''], resolve) }
  { path: '/404', name: 'notFound', component: resolve => require(['../views/notFound.vue'], resolve) },
  { path: '/index', name: 'index', component: resolve => require(['../views/index.vue'], resolve) },
  { path: '*', redirect: '/404' },
]
