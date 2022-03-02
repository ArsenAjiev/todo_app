<template>
  <div class="container">
    <h1> Detail information </h1>
        <button
    class="btn btn-danger mx-3 mt-3"
    @click="deletePost"
    >

    Delete
    </button>


  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Postdetail",
    methods: {
    deletePost()
    {
      axios
      .get('http://127.0.0.1:8000/api/notes/11/')
      .then(response => {
        this.posts = response.data
            console.log(this.posts)
      })

    }
  }
}
</script>

<style scoped>

</style>