import { createStore } from 'vuex'
export default createStore({
  state: {
    isLoading: false,
    isAuthenticated: false,
    token:'',
    user: {
      id:0,
      username:"",
    },

    newtransaction:{
      id:0,
      orderamount:0,
      torecieve:0,
      amountrecieved:0,
      totalamount:0,
      

    }
  },
  getters: {
  },
  mutations: {
    initializeStore(state){
      if(localStorage.getItem('token')){
        state.token = localStorage.getItem('token')
        state.isAuthenticated = true
        state.user.username = localStorage.getItem('username')
        state.user.id = localStorage.getItem('id')
      }else{
        state.token = ''
        state.isAuthenticated = false
        state.user.id = 0
        state.user.username = ''
      }


    },

    ClearTrans(state){
      console.log('0000000')
      state.newtransaction.id = 0
      state.newtransaction.amountrecieved = 0
      state.newtransaction.totalamount = 0
      state.newtransaction.torecieve = 0
      state.newtransaction.orderamount = 0
    },

    Setisloading(state, status){
      state.isLoading = status
    },

    setToken(state, token){
      state.token = token
      state.isAuthenticated = true
    },

    setUser(state, user){
      state.user = user
    },
      

    removeToken(state, token){
      state.token = ''
      state.isAuthenticated = false
    }

  },


  actions: {
  },
  modules: {
    
  }
})
