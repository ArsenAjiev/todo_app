<template>
  <div class="container mt-5">
    <h1 class="notes"> Notes </h1>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
      <a class="navbar-brand p-lg-3" href="/">Home</a>

      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav me-auto ">
          <li v-if="loggedIn">
            <router-link class="nav-link active" aria-current="page" :to="{ name: 'Create' }"> Create</router-link>
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
       <li v-if="loggedIn"> <a class="nav-link active" aria-current="page" v-on:click="logout"
                               href="#"> Logout </a>  </li>
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
    logout() {
      const token = this.$store.state.token
      axios
          .post('/api/auth/token/logout', token)
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

<style lang="scss" scoped>

.notes {
  display: flex;
  justify-content: center;
  font-weight: bolder;
  font-size: 5rem;
  color: #0a731e;
  text-decoration: none;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, .45);
  transition: .35s color ease-in-out, .35s opacity ease-out, .35s text-shadow ease-in-out;
}


</style>