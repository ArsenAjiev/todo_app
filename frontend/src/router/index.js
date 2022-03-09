import { createRouter, createWebHistory } from 'vue-router'
import Login from "@/views/Login";
import Signup from "@/views/Signup";
import Home from "@/components/Home";
import Create from "@/components/Create";
import Edit from "@/components/Edit";
import Postdetail from "@/components/Postdetail";

const routes = [
    {
    path: '/',
    name: 'Home',
    component: Home
    },
    {
    path: '/signup',
    name: 'Signup',
    component: Signup
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/create',
    name: 'Create',
    component: Create
  },
  {
    path: '/edit/:id',
    name: 'Edit',
    component: Edit
  },
  {
    path: '/postdetail/:id',
    name: 'Postdetail',
    component:Postdetail,
    props:true

},

]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
