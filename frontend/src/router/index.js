import { createRouter, createWebHistory } from 'vue-router'
import Login from "@/views/Login";
import Signup from "@/views/Signup";

const routes = [
  {
    path: '/sign-up',
    name: 'Signup',
    component: Signup
  },
  {
    path: '/log-in',
    name: 'Login',
    component: Login
  },

]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
