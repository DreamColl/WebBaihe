export default [
  //  { path: '', name: '', component: resolve => require([''], resolve) }
  { path: '/index', name: 'index', component: resolve => require(['../views/index.vue'], resolve) },
  { path: '/404', name: 'notFound', component: resolve => require(['../views/notFound.vue'], resolve) },
  { path: '/compatibility', name: 'compatibility', component: resolve => require(['../views/compatibility.vue'], resolve) }, // 兼容性提示
  { path: '/announcement', name: 'announcement', component: resolve => require(['../views/announcement.vue'], resolve) }, // 公共页
  { path: '/enter', name: 'enter', component: resolve => require(['../views/enter.vue'], resolve) }, // 报名页
  { path: '*', redirect: '/404' },
]
