<template>
<div class="container">
  <div class="card">
    <div v-for="item in posts" :key="item.id">
                <div class="card rounded-3 card-shadow h-10 border">
                    <div class="card-body">
                        <small class="text-muted card-text">{{ item.slug }}</small>
                        <h5 class="mb-5 card-title">{{ item.title }}</h5>
                        <p class="card-text mb-5">{{ item.text }}</p>
                        <p class="card-text">
                            <small class="text-muted">{{ item.created_at }}</small>
                        </p>
                    </div>
                  <h6>
                  <router-link
                      class="link-style"
                   :to="{name: 'Postdetail', params:{id:item.id}}"
                   >
                      Read more ...
                  </router-link>
                  </h6>
                </div>


   </div>
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
      const token = this.$store.state.token
      console.log(token)
      console.log('logout')

      axios
      .get('http://127.0.0.1:8000/api/notes/')
      .then(response => {
        this.posts = response.data
            console.log(this.posts)
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