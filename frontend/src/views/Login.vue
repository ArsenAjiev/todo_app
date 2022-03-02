<template>
<div class="container">
  <h1> login </h1>
    <form @submit.prevent="submitForm">
    <input type="text" name="username" v-model="username">
    <input type="password" name="password" v-model="password">
    <button type="submit"> Log in </button>

  </form>
</div>
</template>

<script>
import axios from "axios";

export default {
  name: "Login",
  data() {
    return {
      username: '',
      password: ''
    }
  },
  methods: {
    submitForm(e) {
      const formData = {
        username: this.username,
        password: this.password
      }
      axios
          .post('/api/auth/token/login', formData)
          .then(response => {
            console.log(response)
            const token = response.data.auth_token

            this.$store.commit('setToken', token)

            axios.defaults.headers.common['Authorization'] = "Token " + token

            localStorage.setItem("token", token)
            this.$router.push({name: 'Home'})
          })
          .catch(error => {
            console.log(error)
          })
      }

  }
}



</script>

<style scoped>

</style>