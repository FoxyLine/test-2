<template>
    <div id="form-signup">
        <div class="form-signup__container">
            <h2 class="form-header">Sign up</h2>
            <form class='form'>
                <p v-if="form_err">{{ form_err }}</p>
                <div class="input">
                    <p>username</p>
                    <p v-if="username_err">{{ username_err }}</p>
                    <input v-model="username" type="text"/>
                </div>
                <div class="input">
                    <p>password</p>
                    <p v-if="password_err">{{ password_err }}</p>
                    <input v-model="password" type="password"/>
                </div>              
                <div type="submit" v-on:click="submit" class="submit btn" >sign up</div>
            </form>
        </div>
    </div>
</template>
<script>
import { getCookie, signin } from './utils';

export default {
    name: 'Signin',
    data: function(){
        return {
            username: "",
            password: "",

            username_err: "",
            password_err: "",

            form_err: ""
        }
    },

    methods: {
        submit: function() {
            this.form_err = ""

            let csrfmiddlewaretoken = 'eHppBlCHrEESybVoUmbd7ia0L3Gaf4ahoMjV37GqZFbZUsWbUCBcOhEwtvN6Ivq5'//getCookie('csrftoken');
            let body = {
                username: this.username,
                password: this.password,
                csrfmiddlewaretoken
            }

            let response = signin(body)

            response.then(
                result => {
                    console.log('assd');
                    if (result.token){
                        localStorage.setItem('token', result.token)
                        this.$router.push('/')
                    } else {
                        this.username_err = String(result.username || "")
                        this.password_err = String(result.password || "")   
                    }

                    if (result.non_field_errors){
                        this.form_err = "Невозможно войти с предоставленными учетными данными"
                    }

                }
            )            
            
        }
    }
}
</script>

<style src="../../style.css"/>