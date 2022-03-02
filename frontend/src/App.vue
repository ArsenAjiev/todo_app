<template>

  <div class="container mt-5">

    <ul class="nav">
      <li><a href="/"> Home </a> | </li>
      <li v-if="loggedIn"><router-link :to="{ name: 'Create' }"> Create </router-link> | </li>
      <li v-if="loggedIn"><router-link :to="{ name: 'Edit' }"> Edit </router-link> | </li>
      <li v-if="!loggedIn"><router-link to="/login">Log In</router-link> | </li>
      <li v-if="!loggedIn"><router-link :to="{ name: 'Signup' }">Sign up</router-link> | </li>
      <li v-if="loggedIn"><a v-on:click="logout" href="#"> Logout </a> | </li>
    </ul>


  </div>

  <router-view/>
</template>


<script>
import axios from "axios";

export default {
    computed: {
    loggedIn() {
      return this.$store.getters.loggedIn
    }
  },


  name: 'App',
  methods: {
    logout()
    {
      const token = this.$store.state.token
      console.log(token)
      console.log('logout')
      localStorage.clear()
      this.$router.push({name: 'Login'})
    },
  },



  beforeCreate() {
    this.$store.commit('initializeStore')

    const token = this.$store.state.token

    if (token) {
      axios.defaults.headers.common['Authorization'] = "Token " + token
    } else {
      axios.defaults.headers.common['Authorization'] = ''
    }
  }

}


</script>

