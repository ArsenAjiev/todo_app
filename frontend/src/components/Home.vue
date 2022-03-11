<template>
<div class="container">
  <br>
      <div  v-if="posts.length" class="row row-cols-3 g-5">
           <div class="col" v-for="item in posts" :key="item.id">
                <div class="card rounded-3 card-shadow h-100 border">
                      <div class="card-body" >
                          <h5 class="mb-5 card-title">Title: {{ item.title }}</h5>

                          <p class="card-text mb-5">Text: {{ item.text }}</p>
                          <p class="card-text">
                              <small class="text-muted">Date created: {{ item.created_at }}</small>
                          </p>
                      </div>
                           <h6>
                          <router-link
                                  class="btn btn-success mt-3"
                           :to="{name: 'Postdetail', params:{id:item.id}}"
                           >
                           Read more ...
                          </router-link>
                          </h6>
                </div>
            </div>
    </div>
   <div  v-else class="row row-cols-9 g-5">
     <h1 class="no_data"> No data </h1>
   </div>
</div>
</template>

<script>
import axios from "axios";
export default {
    name: "Postlist",
    data() {
    return {
      posts: []
    };
  },
    methods: {
    getdata()
    {
      axios
      .get('http://127.0.0.1:8000/api/notes/')
      .then(response => {
        this.posts = response.data
            // console.log(this.posts)
      })

    }
  },
  created() {
    this.getdata()
  }
}
</script>

<style scoped>


.no_data {
   display: flex;
   justify-content: center;
   /*background: #537c50;*/
   color: #1b5aa1;
   font-weight: bolder;
   font-size: 7rem;
   text-shadow: 2px 2px 4px rgba(0,0,0, .45);
  text-align: center;
  margin-top: 5rem;

;

 }


</style>