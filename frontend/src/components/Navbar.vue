

<template>

<nav class="navbar navbar-expand-lg  navbar" style="background-color: #80d27d;">
  <div class="container">
    <router-link class="navbar-brand" style="color: #16361c" to="/"> Post </router-link>
    <div class="collapse navbar-collapse" id="navbarNav">
      <ul class="navbar-nav ms-auto">
        <li class="nav-item">
          <router-link class="btn btn-success" to="/"> Home </router-link>
        </li>
        <li class="nav-item">
           <router-link class="btn btn-success" to="/create"> Create Post </router-link>
        </li>
      </ul>
    </div>
  </div>
</nav>


</template>

<script>
export default {
  name: "Navbar-item"
}
</script>

<style scoped>
</style>