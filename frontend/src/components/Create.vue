<template>

  <div class="container mt-4">
  <form @submit.prevent="createPost" >

    <input
    type="text"
    class="form-control"
    placeholder="Please enter tiltle"
    v-model="formData.title"
    />
    <input
    type="text"
    class="form-control"
    placeholder="Please enter slug"
    v-model="formData.slug"
    >

    <textarea
    rows="10"
    class="form-control"
    placeholder="Please enter body"
    v-model="formData.text"
    >
    </textarea>

    <button class="btn btn-success mt-4">
      Publish
    </button>

  </form>


    <div v-if="errore"
       class="alert alert-warning alert-dismissible fade show mt-5"
       role="alert"
       >
    <strong>{{errore}}</strong>
    </div>

 </div>
</template>

<script>
import axios from 'axios'
export default {
  data() {
    return {
      formData :{
        title:"",
        slug:"",
        text:"",
      },
      errore:null
    }
  },
  name: "Create-item",
  methods: {
    createPost() {
      console.warn("method work")
        if(!this.formData.title || !this.formData.text) {
          this.errore = "Please add all fields"
          console.warn("no data")
        }
        else {
          console.warn("data exist")
          console.log(this.formData)
          axios.post('http://127.0.0.1:8000/api/notes/', this.formData)
          .then(response => console.log(response))
          .then(() => {
            this.$router.push({
              name: 'Home'
            })
              })
        }
      }
  }
}
</script>

<style scoped>
</style>