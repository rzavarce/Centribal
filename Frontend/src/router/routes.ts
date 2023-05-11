import { RouteRecordRaw } from 'vue-router';


import { LocalStorage } from 'quasar'
const ifAuthenticated = (to, from, next) => {

  if (LocalStorage.getItem('lockState')) {
    next('/LockScreen')
    return
  }

  if (LocalStorage.getItem('isAuthenticated')) {
    next()
    return
  }
  next('/')
}


const routes: RouteRecordRaw[] = [
{ path: '/', name:'login', component: () => import('pages/LoginPage.vue') },
{ path: '/PasswordReset/:user/:token/', component: () => import('pages/PasswordReset.vue') },
{ path: '/PasswordSetting/:user/', component: () => import('pages/PasswordSetting.vue') },
{ path: '/LockScreen/', name:'lockscreen', component: () => import('pages/LockScreen.vue'), },
{ path: '/Maintenance/',  component: () => import('pages/MaintenancePage.vue') },
{
  path: '/Dashboard',
  component: () => import('layouts/MainLayout.vue'),
  beforeEnter: ifAuthenticated,
  children: [
    { path: '/Dashboard/', name:'dashboard', component: () => import('pages/Dashboard.vue'), },
    { path: '/Users/', name:'users_list', component: () => import('pages/users/UsersList.vue'), },
    { path: '/Users/Add/', name:'users_add', component: () => import('pages/users/UsersAdd.vue'), },
    { path: '/Users/Edit/:id/', name:'users_edit', component: () => import('pages/users/UsersEdit.vue'), },
    { path: '/Products/', name:'products_list', component: () => import('pages/products/ProductsList.vue'), },
    { path: '/Products/Add/', name:'products_add', component: () => import('pages/products/ProductsAdd.vue'), },
    { path: '/Products/Edit/:id/', name:'products_edit', component: () => import('pages/products/ProductsEdit.vue'), },
    { path: '/Orders/', name:'orders_list', component: () => import('pages/orders/OrdersList.vue'), },
    { path: '/Orders/Add/', name:'orders_add', component: () => import('pages/orders/OrdersAdd.vue'), },
    { path: '/Orders/Edit/:id/', name:'orders_edit', component: () => import('pages/orders/OrdersEdit.vue'), },
    { path: '/Profile/', name:'profile', component: () => import('pages/UserProfile.vue') },
    { path: '/History/', name:'history', component: () => import('pages/HistoryPage.vue') },
    { path: '/MapSimple/', name:'map', component: () => import('pages/maps/MapPage.vue') },
    { path: '/MapCluster/', name:'map_cluster', component: () => import('pages/maps/MapCluster.vue') },
    { path: '/MapMoving/', name:'map_moving', component: () => import('pages/maps/MapMoving.vue') },
    { path: '/Others/', name:'others', component: () => import('pages/OthersPage.vue') },
  ],
},

  // Always leave this as last one,
  // but you can also remove it
{
  path: '/:catchAll(.*)*',
  component: () => import('pages/ErrorNotFound.vue'),
},

];

export default routes;
