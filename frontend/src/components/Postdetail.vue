<template>
 <div class="container mt-2">
    <table class="table">
     <thead> Post item</thead>
     <tbody>
      <tr>
       <td> id </td>
       <td> {{post.id}} </td>
      </tr>
       <tr>
       <td> title </td>
       <td> {{post.title}} </td>
      </tr>
       <tr>
       <td> slug </td>
       <td> {{post.slug}}  </td>
      </tr>
       <tr>
       <td> text </td>
       <td> {{post.text}}  </td>
      </tr>
        <tr>
       <td> is_public </td>
       <td> {{post.is_public}}  </td>
      </tr>
        <tr>
       <td> created_at </td>
       <td> {{post.created_at}} </td>
      </tr>
        <tr>
       <td> updated_at </td>
       <td> {{post.updated_at}} </td>
      </tr>
     </tbody>
    </table>



    <router-link :to="{name: 'Edit', params:{id:id}}"
    class="btn btn-success mt-3"
    > Update

    </router-link>
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
    data() {
    return {
      post:{}
    }
  },
  props: {
    id: {
      type:[Number, String],
      required:true
    }
  },


    methods: {
    deletePost() {
      axios
      .delete(`http://127.0.0.1:8000/api/notes/${this.id}/`)
          .then(() => {
            this.$router.push({
              name: 'Home'
            })
          })
          .catch(error => {
            console.log(error);
          });

    },
    getdata()
    {
      const token = this.$store.state.token
      axios
      .get(`http://127.0.0.1:8000/api/notes/${this.id}/` )
      .then(response => {
        this.post = response.data
      })

    }
  },

    created() {
    this.getdata()
  }
}
</script>

<style scoped>

</style>