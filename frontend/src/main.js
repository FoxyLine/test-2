// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import VueRouter from 'vue-router';
import Vue from 'vue'
import Router from './app/router';

// import App from './app';

// import { Signin, KanbanBoard } from './app/components'

Vue.config.productionTip = false




const app = new Vue({
    // el: '#app',
    // components: { App },
    router: Router
        // template: '<App/>'
}).$mount('#app');