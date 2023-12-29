<template>
  <v-app>
    <v-main>
      <NavBar></NavBar>
      
      <router-view/>
    </v-main>
  </v-app>
</template>

<script>
import axios from 'axios';
import NavBar from './views/NavBar';

import store from './store/index'

export default {
  name: 'App',

  components:{
    NavBar
  },

  beforeCreate(){
    this.$store.commit('initializeStore')
    console.log(this.$store.state.isAuthenticated)
    if(this.$store.state.token){
      axios.defaults.headers.common['Authorization'] = 'Token ' + this.$store.state.token
    }else{
      axios.defaults.headers.common['Authorization'] = ''
    }
  },

  data: () => ({
    //
  }),
}
</script>



