<template>
    <div class="container mt-5">
  <nav class="navbar navbar-expand-lg navbar-light bg-light" >
    <a class="navbar-brand p-lg-3" href="/">Home</a>

    <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav me-auto ">
<li v-if="loggedIn">
          <router-link class="nav-link active" aria-current="page" :to="{ name: 'Create' }"> Create </router-link>
       </li>
        </ul>

        <span class="navbar-text">
        <ul class="navbar-nav me-auto ">
        <li v-if="!loggedIn">
          <router-link class="nav-link active" aria-current="page" to="/login">Log In</router-link>
       </li>
        <li v-if="!loggedIn">
          <router-link class="nav-link active" aria-current="page" :to="{ name: 'Signup' }"> Sign up </router-link>
       </li>
       <li  v-if="loggedIn"> <a class="nav-link active" aria-current="page" v-on:click="logout" href="#"> Logout </a>  </li>
       </ul>
          </span>
    </div>
    </nav>
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

<style scoped>






</style>