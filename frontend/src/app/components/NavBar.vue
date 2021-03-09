<template>
    <div class="navbar-root">
      <nav class="navbar navbar-expand-md navbar-light bg-light">
        <a class="navbar-brand" href="/">kanban</a>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav mr-auto">
            <li class="nav-item">
            </li>

            
            <li v-if="token != 0"  class="nav-item">              
              <a class="nav-link" href="accounts/logout/" v-on:click="logout">Sign Out</a>
            </li>
          
              <li v-if="token == null" class="nav-item">
                <a class="nav-link" href="accounts/signup/">Sign Up</a>  
              </li>
              <li v-if="token == null" class="nav-item">
                <a class="nav-link" href="accounts/login/">Sign In </a>  
              </li>
          </ul>
        </div>
      </nav>

    </div>
    
</template>

<script>
import { getCookie } from './utils';

export default {
    name: "NavBar",
    data: function() {
        return {
            text: "text",
            token: getCookie('csrftoken') || null

        }
    },

    methods: {
      logout: function() {
        localStorage.removeItem('token')
        document.cookie = ""
      }
    }
}
</script>
