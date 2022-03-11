<template>
  <div class="container mt-4">

    <form @submit.prevent="updatePost">
     <input
         type="text"
         class="form-control"
         placeholder="Enter title"
         v-model="formData.title"
     >
    <br/>
    <input
         type="text"
         class="form-control"
         placeholder="Enter title"
         v-model="formData.slug"
     >
    <br/>
    <textarea
      rows="8"
      placeholder="enter body"
      class="form-control"
      v-model="formData.text"
    >
    </textarea>

    <button class="btn btn-success mt-4"> Update Post</button>
    </form>

        <div v-if="error"
       class="alert alert-warning alert-dismissible fade show mt-5"
       role="alert"
       >
    <strong>{{error}}</strong>
    </div>

  </div>
</template>

<script>
import axios from 'axios'
export default {

  name: "PostEdit",
    props: {
    id: {
      type:[Number, String],
      required:true
    }
  },
   data() {
    return {
      formData :{
        title:"",
        slug:"",
        text:"",
      },
      error:null
    }
  },
  methods: {


    updatePost(){
      const token = this.$store.state.token

      if(!this.formData.title || !this.formData.text ) {
          this.error = "Please add all fields"
          console.warn("no data")
        }
        else {
      axios.patch(`http://127.0.0.1:8000/api/notes/${this.id}/`,this.formData )

      .then(() => {
        this.$router.push('/')
         })
      .catch(error => console.log(error))
      }
    }
  },
  beforeRouteEnter(to, from, next) {

    if(to.params.id !== undefined) {
      axios.get(`http://127.0.0.1:8000/api/notes/${to.params.id}/` )
      .then((data) => {
        return next(vm=> (vm.formData.title=data.data.title, vm.formData.text=data.data.text, vm.formData.slug=data.data.slug ))
      })
    } else {
      return next
    }
  }
}
</script>

<style scoped>
</style>