import {createRouter, createWebHistory} from "vue-router";
import Home from "@/components/Home";
import Post_Detail from "@/components/Post_Detail";



const routes = [
    {
        path: '/',
        name: "home",
        component: Home

    },

         {
        path: '/details/:id',
        name: "details",
        component:Post_Detail,
        props:true

    },



]

const router = createRouter({
    history:createWebHistory(),
    routes,
})

export default router;