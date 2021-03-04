// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import VueRouter from 'vue-router';
import Vue from 'vue'
import App from './app';

import { Signin } from './app/components'

Vue.config.productionTip = false
Vue.use(VueRouter)
    /* eslint-disable no-new */

const routes = [
    { path: '/', component: App },
    { path: '/about', component: { template: '<div>sad</div>' } },
    { path: '/signin', component: Signin }
]

const router = new VueRouter({
    mode: 'history',
    routes
});

const app = new Vue({
    // el: '#app',
    // components: { App },
    router
    // template: '<App/>'
}).$mount('#app');