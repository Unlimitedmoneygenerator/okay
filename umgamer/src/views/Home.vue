<template>

<html>
<head>
	
  
</head>
<body>


<div id = 'contented'>
	
	<div id = 'content'></div>
	<img id = "imgtwo" v-bind:src="require('../assets/lordgod.png')"/>
	<img id = "img" v-bind:src="require('../assets/lordgod.png')"/>
	

</div>

<div id = 'select'>
	
	<div id ='selectbg'></div>
	<label id = "title">Unlimited Money Generator</label><br>
	<label id = "amount">{{umcount}} UM</label>
	<label>Minimum order amount is as little as 1 order(1$), players must take into account the fee.</label>
	<label id="info">Any preorders will recieve a special reward. Any preorders will be allowed to play before all other users, no exceptions, all preorders obtain max data level. Preorder minimum, is one dollar plus the fee. Order any amount you like below.</label>
	<input id = "input" v-model = "ordamnt" placeholder="Order amount" @keyup="RunUm">
	<label id="note">*note, each order placed costs 1 dollar, so if you dont have at least 1 "UM", you wont be able to play.</label>
	<button id ="STRIPEBUTT" @click="STRIPE">STRIPE</button>
	<button id ="CRYPTO" @click="CRYPTO">CRYPTO</button>
	<button id="paynow" v-if="unedited > 1" @click ="PAYNOW">Pay Now</button>

</div>

	

<div id="keys" v-if = "$store.state.isAuthenticated">
	
	<div id="keysback"></div>
	
	<div id ="keyview"></div>
	
	<div id ="keyviews">
		<label ID ="Name">{{$store.state.user.username}}</label>
		
		<label id = "keytitlebg"></label>
		<label id = "keytitle">Keys</label>
		<div id="keyarea">
			
			
			<div id="keyareabg"></div>
			<ul id="ul">
				
				<li	id = "keylist" v-for ="items in KEYS">
					s
					
					
					<label id="Specialkeybg"></label>
					<label id="Specialkeyis" v-if = 'items.p_timer == 0 '>{{items.p_keyseed}}</label>
					<label id="Specialkey" v-if = 'items.p_timer > 0 '>***</label>
					<button id="View">{{ Math.floor(items.p_timer /(3600*24))}}</button>

					
				</li>
				<button id="Activatekeys" @click = 'ACTKEYS'>Activate Keys</button>
				<button id="BackButton" class="button is-success" @click="back">Back</button>
				
			
			</ul>
			
			
			
		</div>
		
	</div>
	
</div>

<div id="login" class="loginstate">
	<div id="divider" v-if="$store.state.isAuthenticated">
		
	</div>

	
	<button v-if = "$store.state.isAuthenticated" id="keybutton"  class="button is-success" @click = "openk">Keys</button>
	<button v-if = "$store.state.isAuthenticated" id="buttonlogout" @click = "Logout" class="button is-success">Logout</button>
	<button v-if = "$store.state.isAuthenticated" id="buttonpurh" @click = "GOPAY" class="button is-success">Transactions</button>
	<div id="logback"></div>
	
	<form id ="form" v-if = "!$store.state.isAuthenticated" @submit.prevent="submitformlog">
		<label id="formtitle">{{method}}:</label>
		
		<div id="login">
			
			<input id = 'user' placeholder="Username" v-model="logusername">
			
			
			<input id = 'pass' placeholder="Password" v-model="logpassword">

			<button id="loginbut">
				Login
			</button>
		</div>

		<div id="newuser">
			<button id="forgotpw" type="button" @click="fgpw">
			Forgot PW
			</button>
			<button id="register" type="button" @click = "fgreg">
			/Register
			</button>
		</div>

	</form>

	<form id ="formregister" v-if = "!$store.state.isAuthenticated" @submit.prevent="submitForm">
		<label id="formtitle">register:</label>
		
		<div id="login">
			
			<input id = 'reguser' placeholder="Username" v-model="username">
			<input id = 'regpass' placeholder="Password" v-model="password">
			<input id = 'secondpass' placeholder="Confirm Password" v-model="passwordtwo">>
			<input id = 'email' placeholder="Email" v-model="email">>>

			<button id="loginbut">
				Register
			</button>
		</div>
		

		<div id="newuser">
			<button id="forgotpw" type="button" @click="fgpw">
			Forgot PW
			</button>
			<button id="register"  type="button" @click = "fglogin">
			/Login
			</button>
		</div>

	</form>

	

	<div id ="formforgot" v-if = "!$store.state.isAuthenticated">
		<label id="formtitle">forgot user/pass:</label>
		
		<div id="login">
			
			<input id = 'reguserforgot' placeholder="Enter Username">
			
			
			<input id = 'regemailforgot' placeholder="Enter Email">
			<label id="or">or</label>
			<button id="loginbut">
				Reset
			</button>
		</div>

		<div id="newuser">
			<button id="forgotpw" type="button" @click = 'fglogin'>
			Login
			</button>
			<button id="register"  type="button" @click = 'fgreg'>
			/Register
			</button>
		</div>

	</div>

	<h1 id="formcred" v-if = "!$store.state.isAuthenticated">*Credentials:</h1>
	
</div>


<div id="qrcode">
	<div id="qrcodebg">

		<div id="contentqr">
			
			<img id = "qrcodeimage" src="">
			<label id="btcaddress" >{{ this.CURaddress }}</label>
			
		</div>

		<div id="divofpurchase">
			<label id="Payment">Payment Details</label>
			<div id="back"></div>
			<button id="backbutton" @click="closeinvoices" class="button is-success">Close</button>
			<label id="Status">Payment Status: {{ currenttrans.payment_status }}</label>
			<label id="PaymentAmt">Payment Amount: {{ currenttrans.pay_amount }}</label>
			<label id="AmountRec">Amount Received: {{ currenttrans.amount_received }}</label>
			<label id="UserName">User: {{ currenttrans.username}}</label>



		</div>
	</div>
</div>
</body>
</html>
	
</template>

<script>
var openedlogin = false
document.body.addEventListener("keydown", (ev) => {
	
	if (ev.keyCode == 16){
		console.log(event)
			if (openedlogin == false){
					openedlogin = true
					document.getElementById("login").style.opacity = 0.7
					document.getElementById("contented").style.zIndex = 8
					document.getElementById("select").style.zIndex = 8
		
			}else{
				document.getElementById("select").style.zIndex = 10
				document.getElementById("contented").style.zIndex = 10
				document.getElementById("login").style.zIndex = 9
					openedlogin = false
					document.getElementById("login").style.opacity = 0
					}

			if(document.getElementById("qrcode").style.visibility == "visible"){
				document.getElementById("qrcode").style.visibility = "hidden"
			}

			if(document.getElementById("keys").style.visibility == "visible"){
				document.getElementById("keys").style.visibility = "hidden"
			}
			
	}
	
})
import store from '@/store'
import axios from 'axios'



//register method, login method,//stripe,keys method





//use umglitch for umgame and creating accounts db then transfer it to umglitch
// bitcoin,,email send to confirm user.. //understand keys method way to decode on umglitch. 
//upload server.

//stripe but just add a fee. .87 +30 1.17 31.17


//umglitch database port to server. umglitch login, fix login page, fix all hyperlinks, player profile cant go below. cannot donate to your
//self, 

//umgroup
//account on hold
//panel approve decline transactions
//show transaction status in user profile.
//transfer btc from our wallet to theirs for specific amount.
//import to csv list if approved, take money out of their umg account append to csv list if trans approved and well, import the address and the amount, to 
//now payments.
//send money to umglitch.
// keep money in umg

//12 days




// add keys method to umglitch,
//login method
//fix first page.
//disable trades and inventory
//optimization method
//when you win it stays on screen till you close.
//chat go up chat go down
//player wins /sore losers model fix(include luck).
//LEVELUP BAR
//min data level to see winner luck, put in game
//IMPORT ROUND TYPE object into game, IF RANDOM DONT GIVE MAX TIME so its harder for users.
//music
//support
//figure out databases.
//when seed is random, the minimum amount is 5 minutes
//LEADERBOARD
//test out cursor
//ERRORS TICKET
//CREATE SYSTEM, WORKERS CAN APPROVE AND DECLINE TRANSACTIONS AUTOMATED, BASED OFF A RISK SYSTEM, IF PLAYER SORE LOSER WINS/WINNERS
// < CASHOUT, RED FLAG BRING OVER TO WORKERS FOR THEM TO REVIEW.
//FIX CHAT UP next phase imput chat cooldown
//show name at top
// /everyone must post winning 1/10 x10000 +


//12 days

















//make sure only one trade can be sent at a time. modifies min to see winner luck, trade counter, max 1 per player. on umgglitch frontend,
//add mods section later on update(x2 speed, no FL, no L)
//finish trade even though alr ready for launch in state.//
//make it so you can click player names and view their level and shit.
// umglitch schedule, optimization winner luck see, fix maybe background layer (world)g experiment with try and make it better,

//glitches save for later




import {toast} from 'bulma'


export default{
	data(){
	return{
		
		method:'login',Keys:[],sampkey:[""],username:'',password:'',passwordtwo:'',email:'',errors:[],logusername:'',logpassword:''
		,getkeys:[],postuser:[],pub_key:'',stripe:null,token:[],usernamer:[],umcount:0,mode:"stripe",test:0,currenttrans:[],
		CURaddress:"", char:(`https://chart.googleapis.com/chart?chs=250x250&cht=qr&chl=` + this.CURaddress),unedited:0,KEYS:[],
		donor:""
		
	}
	
	
	},

	async mounted(){
		document.getElementById("login").style.opacity = 0
		document.getElementById("contented").style.zIndex = 10
		this.PayWin()
		setInterval(1000, this.lovetou())
		setInterval(1000, this.GETDONOR())
		setInterval(4000, this.GETMYTRANS())
		await this.getPubKey()
		
		//await this.GetData()
		
		
		//setInterval(1000, this.Purchase())
	},



	methods:{
		lovetou(){
			console.log("peace")
		},

		GETDONOR(){
			const fromData = {
					username: this.username,
					
				}

				axios
					.post('/api/v1/Donate/', fromData).then(response =>{
						this.donor = response.data.KEY
						
					}).catch(error => {
						if(error.response){
							console.log(error.response.data)
						}
					})
		},
		openk(){
			document.getElementById("login").style.opacity = 0
			openedlogin = false
			document.getElementById("keys").style.visibility = "visible"

			const data = {
					username:this.$store.state.user.username,
				}
			axios.post('api/v1/GETMYKEYS/',data)
			.then(response =>{
				console.log(response.data)
				this.KEYS = response.data
				
			})
			.catch(error =>{
				console.log('Error:', error)
			})


			

		},
		async GETMYTRANS(){
			const data = {
					username:this.$store.state.user.username,
				}
			axios.post('api/v1/mydata/',data)
			.then(response =>{

				this.currenttrans = response.data
				this.CURaddress = response.data.address
				this.char = response.data.p_qrcode
				
				
				console.log(response.data)
				const image = document.getElementById("qrcodeimage")
				image.src = this.char


				
			})
			.catch(error =>{
				console.log('Error:', error)
			})
		},
		async GOPAY(){
			this.GETMYTRANS()
			document.getElementById("qrcode").style.visibility = "visible"
			document.getElementById("keys").style.visibility = "hidden"
			document.getElementById("login").style.opacity = 0
			openedlogin = false

		
		},
		async PAYNOW(){

			if(!store.state.isAuthenticated){
				console.log("you arent logged in")
			}else{



				if(this.mode == 'crypto'){
					if(this.ordamnt > 50){
						this.$store.commit('ClearTrans')
						const options = {

						method: 'POST',
						url:'https://api.nowpayments.io/v1/payment',
						headers: {
							'content-type': 'application/json',
							'x-api-key': this.donor,
						},

						data: {
							'price_amount': this.ordamnt,
							'price_currency': "usd",
							'pay_currency':"btc",
							'ipn_callback_url': 'https://nowpayments.io',
							'order_id': 'keyseed',
							'order_description': 'A key seed with the amount of'+ this.umcount
						}



						};

						try{
						const response = await axios.request(options)
						console.log(response.data)
						//delete all invoices right here with a function
						const data = {


								'username':this.$store.state.user.username,
								'price_amount':response.data.price_amount,
								'address':response.data.pay_address,
								'pay_amount':response.data.pay_amount,
								'amount_received':response.data.amount_received,
								'payment_id':response.data.payment_id,
								'payment_status':response.data.payment_status
							}

						axios.post('api/v1/invoice/', data)
						.then(response =>{

							console.log(response)	

							
						})						
						.catch(error =>{
							console.log('Error:', error)
							document.getElementById("qrcode").style.visibility = "visible"
							this.GETMYTRANS()

						})


						}catch(error){
						console.log(error)

						}
					}
				}else{
					this.Purchase()
				}
			}
		},
		PayWin(){
			if (this.mode == "stripe"){
				document.getElementById('STRIPEBUTT').style.border = "1px solid green"
				document.getElementById('CRYPTO').style.border = "0px solid green"
			}else{
				document.getElementById('CRYPTO').style.border = "1px solid green"
				document.getElementById('STRIPEBUTT').style.border = "0px solid green"
			}
			
		},
		
		CRYPTO(){
			this.mode = 'crypto'
			document.getElementById('CRYPTO').style.border = "1px solid green"
			document.getElementById('STRIPEBUTT').style.border = "0px solid green"
			if (this.ordamnt <= 100){
				this.ordamnt = Math.round(this.ordamnt)
				this.test = this.ordamnt * 0.005
				this.umcount = this.ordamnt -this.test
				this.unedited = Math.round(this.umcount)
				//this.umcount = Math.round(this.umcount)
				this.umcount = Intl.NumberFormat().format(this.umcount)
				}else{
					this.ordamnt = Math.round(this.ordamnt)
					this.test = this.ordamnt * 0.005
					this.umcount = this.ordamnt -this.test
					this.umcount = Math.round(this.umcount)
					this.unedited = Math.round(this.umcount)
					this.umcount = Intl.NumberFormat().format(this.umcount)
					console.log(this.umcount)
				}
		},
		STRIPE(){
			this.mode = 'stripe'
			document.getElementById('CRYPTO').style.border = "0px solid green"
			document.getElementById('STRIPEBUTT').style.border = "1px solid green"
			if (this.ordamnt <= 100){
				this.ordamnt = Math.round(this.ordamnt)
				this.test = this.ordamnt * 0.029
				this.umcount = this.ordamnt -this.test
				this.umcount =this.umcount - 0.3
				this.unedited = Math.round(this.umcount)
				//this.umcount = Math.round(this.umcount)
				this.umcount = Intl.NumberFormat().format(this.umcount)
				}else{
					this.ordamnt = Math.round(this.ordamnt)
					this.test = this.ordamnt * 0.029
					this.umcount = this.ordamnt -this.test
					this.umcount =this.umcount - 0.3
					this.umcount = Math.round(this.umcount)
					this.unedited = Math.round(this.umcount)
					this.umcount = Intl.NumberFormat().format(this.umcount)
				}


		},
		RunUm(){
			if (this.mode == "stripe"){
				if (this.ordamnt <= 100){
				this.ordamnt = Math.round(this.ordamnt)
				this.test = this.ordamnt * 0.029
				this.umcount = this.ordamnt -this.test
				this.umcount =this.umcount - 0.3
				this.unedited = Math.round(this.umcount)
				//this.umcount = Math.round(this.umcount)
				this.umcount = Intl.NumberFormat().format(this.umcount)
				}else{
					this.ordamnt = Math.round(this.ordamnt)
					this.test = this.ordamnt * 0.029
					this.umcount = this.ordamnt -this.test
					this.umcount =this.umcount - 0.3
					this.unedited = Math.round(this.umcount)
					this.umcount = Math.round(this.umcount)
					this.umcount = Intl.NumberFormat().format(this.umcount)
				}
			}else{

				if (this.ordamnt <= 100){
				this.ordamnt = Math.round(this.ordamnt)
				this.test = this.ordamnt * 0.005
				this.umcount = this.ordamnt -this.test
				this.unedited = Math.round(this.umcount)
				//this.umcount = Math.round(this.umcount)
				this.umcount = Intl.NumberFormat().format(this.umcount)
				}else{
					this.ordamnt = Math.round(this.ordamnt)
					this.test = this.ordamnt * 0.005
					this.umcount = this.ordamnt -this.test
					this.unedited = Math.round(this.umcount)
					this.umcount = Math.round(this.umcount)
					this.umcount = Intl.NumberFormat().format(this.umcount)
					console.log(this.umcount)
				}

			}
			
			

		},

		closeinvoices(){
			document.getElementById("qrcode").style.visibility = "hidden"
			openedlogin = true
			document.getElementById("login").style.opacity = 0.7
			document.getElementById("login").style.zIndex = 10
			document.getElementById("contented").style.zIndex = 8
			document.getElementById("select").style.zIndex = 8

		},

		back(){
			document.getElementById("login").style.opacity = 0.7
			document.getElementById("keys").style.visibility = "hidden"
			document.getElementById("login").style.visibility = "visible"
			document.getElementById("login").style.zIndex = 10
			document.getElementById("contented").style.zIndex = 8
			openedlogin = true

		},
		async Logout(){

				axios
					.post('/api/v1/token/logout/')
					.then(response =>{
						
						
						console.log('Logged Out')
					
					}).catch(error => {
						if(error.response){
							console.log(error.response.data)
						}
					})
				axios.defaults.headers.common['Authorization'] = ''
				localStorage.removeItem('token')
				localStorage.removeItem('token')
				this.$store.commit('removeToken')
				localStorage.removeItem('username')
				localStorage.removeItem('id')
				document.getElementById("keys").style.visibility = "hidden"
				document.getElementById("login").style.opacity = 0.7
				document.getElementById("login").style.visibility = "visible"


					
				
		},

		async gohead(){

				axios
					.get('/api/v1/users/me').then(response =>{
						
						this.username = response.data.username
						console.log(this.username, "loveyou")


						this.$store.commit('setUser', {'id':response.data.id, 'username':response.data.username})

						localStorage.setItem('username', response.data.username)
						localStorage.setItem('id', response.data.id)

						console.log(this.$store.state.user)
						
						document.getElementById("form").style.visibility = "hidden"
						document.getElementById("formcred").style.visibility = "hidden"

					}).catch(error => {
						if(error.response){
							console.log(error.response.data)
						}
				})
		},


		async GetData(){
				const options = {

				method: 'POST',
				url:'https://api.nowpayments.io/v1/payment',
				headers: {
					'content-type': 'application/json',
					'x-api-key': '0X69GM1-0YQMQM3-GH4TPKG-YP685FF',
				},

				data: {
					'price_amount': 3999.5,
					'price_currency': "usd",
					'pay_currency':"btc",
					'ipn_callback_url': 'https://nowpayments.io',
					'order_id': 'RGDBP-21314',
					'order_description': 'Apple Macbook Pro 2019 x 1'
  					
  					
  					
  					
				}

				
			
			};

			try{
				const response = await axios.request(options)
				console.log(response.data)
			}catch(error){
				console.log(error)
				

				
			}
		},

		
		
		async Purchase(){
			const data = {
					username:this.$store.state.user.username,
					keyamount:this.ordamnt
					



				}
			axios.post('api/v1/stripe/create_checkout_session/',data)
			.then(response =>{


				console.log(response)

				return this.stripe.redirectToCheckout({sessionId: response.data.sessionId})
			})
			.catch(error =>{
				console.log('Error:', error)
			})
		},
		async getPubKey(){

			await axios
				.get('/api/v1/stripe/get_stripe_pub_key/')
				.then(response => {
					console.log(response.data)
					this.pub_key = response.data
					this.stripe =Stripe(
					response.data.pub_key
					)
				})
				.catch(error =>{
					console.log(error)
				})

		},
		fgpw(){
			document.getElementById("formregister").style.visibility = "hidden"
			document.getElementById("form").style.visibility = "hidden"
			document.getElementById("formforgot").style.visibility = "visible"
		},
		fgreg(){
			document.getElementById("formregister").style.visibility = "visible"
			document.getElementById("form").style.visibility = "hidden"
			document.getElementById("formforgot").style.visibility = "hidden"
		},
		fglogin(){
			document.getElementById("formregister").style.visibility = "hidden"
			document.getElementById("form").style.visibility = "visible"
			document.getElementById("formforgot").style.visibility = "hidden"
		},
		submitForm(){
			if (!this.errors.length){
				const fromData = {
					username: this.username,
					password: this.password,
					email: this.email
				}

				axios
					.post('/api/v1/users/', fromData).then(response =>{
						toast(
							{
								message:"account was created please log in",
								type: 'is-success',
								dismissable: true,
								pauseOnHover:true,
								duration:7000,
								position:'bottom right',
								
							}
						)
					}).catch(error => {
						if(error.response){
							console.log(error.response.data)
						}
					})
			}
		},

		 goheadS(){


			 
			 console.log(this.$store.state.token, axios.defaults.headers.common['Authorization'])
			 axios
			
					.get('/api/v1/users/me')
					.then(response =>{

						this.$store.commit('setUser', {'id':response.data.id, 'username':response.data.username})

						localStorage.setItem('username', response.data.username)
						localStorage.setItem('id', response.data.id)

						console.log(this.$store.state.username)
					})
					.catch(error =>{
						console.log(error)
					})
		},
		async submitformlog(){
			axios.defaults.headers.common['Authorization'] = ''
			localStorage.removeItem('token')
				const fromData = {
					username: this.logusername,
					password: this.logpassword,
					
					
				}

				axios
					.post('/api/v1/token/login/', fromData).then(response =>{
						const token = response.data.auth_token

						this.$store.commit('setToken', token)
						
						axios.defaults.headers.common['Authorization'] = 'Token '+token

						localStorage.setItem('token', token)
						
						console.log(response.data)
						this.gohead()
						//document.getElementById("form").style.visibility = "hidden"
						//document.getElementById("formcred").style.visibility = "hidden"

					}).catch(error => {
						if(error.response){
							console.log(error.response.data)
						}
				})
				
				
					
					
			}
		},
		
	




}

</script>

<style lang="scss">
body {
            background-color: rgb(111, 228, 152);
        }

h1 {
            color: whitesmoke;
        }

p {
            color: red;
        }


#login{
	position:absolute;
	height: 88%;
	width: 98%;
	right: 1%;
	background-color: black;
	top: 11%;
	opacity: 0.7;
	z-index: 9;
	
	
}

#qrcodeimage{
	position:absolute;
	height: 60%;
	width: 40%;
	right: 57.5%;
	background-color: rgb(32, 32, 32);
	top: 18.5%;
	border: 10px solid black;
	opacity: 1;
	z-index: 10;
}
#divofpurchase{
	position:absolute;
	height: 90%;
	width: 50%;
	right: 4.25%;
	background-color: rgb(22, 22, 22);
	top: 5%;
	border: 5px solid black;
	opacity: 1;
	z-index: 10;
}
#back{
	position:absolute;
	height: 50%;
	width: 95%;
	right: 2.5%;
	text-align: center;
	font-size: 14px;
	font-family: 'Arial Narrow';
	font-weight: bold;
	background-color: rgb(0, 0, 0);
	top: 10.5%;
	opacity: 1;
	z-index: 10;
}

#backbutton{
	position:absolute;
	height: 10%;
	width: 45%;
	right: 25.5%;
	text-align: center;
	font-size: 14px;
	font-family: 'Arial Narrow';
	font-weight: bold;
	background-color: rgb(22, 52, 17);
	top: 85.5%;
	opacity: 1;
	z-index: 10;
}
#PaymentAmt{
	position:absolute;
	height: 50%;
	width: 95%;
	right: 2.5%;
	text-align: center;
	font-size: 14px;
	font-family: 'Arial Narrow';
	font-weight: bold;
	top: 15.5%;
	opacity: 1;
	z-index: 10;
}
#AmountRec{
	position:absolute;
	height: 50%;
	width: 95%;
	right: 2.5%;
	text-align: center;
	font-size: 14px;
	font-family: 'Arial Narrow';
	font-weight: bold;
	top: 20.5%;
	opacity: 1;
	z-index: 10;
}

#UserName{
	position:absolute;
	height: 50%;
	width: 95%;
	right: 2.5%;
	text-align: center;
	font-size: 14px;
	font-family: 'Arial Narrow';
	font-weight: bold;
	top: 25.5%;
	opacity: 1;
	z-index: 10;
}
#Status{
	position:absolute;
	height: 50%;
	width: 95%;
	right: 2.5%;
	text-align: center;
	font-size: 14px;
	font-family: 'Arial Narrow';
	font-weight: bold;
	top: 10.5%;
	opacity: 1;
	z-index: 10;
}
#Payment{
	position:absolute;
	height: 5%;
	width: 95%;
	right: 2.5%;
	text-align: center;
	font-size: 14px;
	font-family: 'Arial Narrow';
	font-weight: bold;
	background-color: rgb(0, 0, 0);
	top: 2.5%;
	opacity: 1;
	z-index: 10;
}
#contentqr{
	position:absolute;
	height: 95%;
	width: 95%;
	right: 2.5%;
	background-color: rgb(32, 32, 32);
	top: 2.5%;
	border: 10px solid black;
	opacity: 1;
	z-index: 10;
}
#btcaddress{
	position:absolute;
	height: 5%;
	width: 44%;
	right: 55.25%;
	background-color: rgb(14, 14, 14);
	top: 80%;
	color: #209c19;
	opacity: 0.7;
	font-size: 14px;
	text-align: center;
	z-index: 10;
}
#qrcodebg{
	position:absolute;
	height: 80%;
	width: 50%;
	right: 25%;
	background-color: rgb(44, 132, 48);
	top: 10%;
	border: 10px solid black;
	opacity: 0.7;
	z-index: 10;
}
#qrcode{
	position:absolute;
	height: 88%;
	width: 99%;
	right: 0.5%;
	background-color: rgb(0, 0, 0);
	top: 11%;
	opacity: 0.8;
	z-index: 10;
	visibility: hidden;
}
#title{
	width:100%;
	position: absolute;
	right: 0%;
	font-size: large;
	z-index: 10;
	color: green;
	font-family: 'Arial Narrow';
	text-align: center;
}

#paynow{
	font-family: 'Arial Narrow';
	width: 50%;
	right: 25%;
	top: 102.5%;
	font-weight: 600;
	color:green;
	font-size: large;
	position: absolute;
	text-align: center;
	background-color: #000000;
}
#CRYPTO{
	font-family: 'Arial Narrow';
	width: 100%;
	right: 0%;
	top: 95%;
	color:green;
	font-size: large;
	position: absolute;
	text-align: center;
	background-color: #000000;
}

#note{
	font-family: 'Arial Narrow';
	width: 100%;
	right: 0%;
	top: 79%;
	font-size: 15px;
	color:green;
	// /border: 1px solid rgb(40, 162, 38);
	position: absolute;
	text-align: center;
	background-color: #000000;
}
#STRIPEBUTT{
	font-family: 'Arial Narrow';
	width: 100%;
	right: 0%;
	top: 89%;
	color:green;
	// /border: 1px solid rgb(40, 162, 38);
	font-size: large;
	position: absolute;
	text-align: center;
	background-color: #000000;
}
#info{
	font-family: 'Arial Narrow';
	width: 100%;
	right: 0%;
	top:20%;
	color:green;
	font-size: large;
	position: absolute;
	text-align: center;
}

#amount{
	font-family: 'Arial Narrow';
	width: 100%;
	right: 0%;
	color:green;
	
	top:47.5%;
	font-size: 72px;
	position: absolute;
	text-align: center;
}
#divider{
	position:absolute;
	height: 100%;
	width: 25%;
	right: 38.5%;
	background-color: rgb(13, 12, 12);
	top: 0%;
	opacity: 0.70;
	z-index: 10;

	filter: drop-shadow(6px,6px,2px rgb(0,0,0));
}


#keybutton{
	position:absolute;
	height: 7.5%;
	width: 12.5%;
	right: 45%;
	background-color: rgb(10, 78, 28);
	top: 37.5%;
	opacity: 1;
	z-index: 10;
}

#buttonpurh{
	position:absolute;
	height: 7.5%;
	width: 12.5%;
	right: 45%;
	background-color: rgb(10, 78, 28);
	top: 55%;
	opacity: 1;
	z-index: 10;
}
#buttonlogout{
	position:absolute;
	height: 7.5%;
	width: 12.5%;
	right: 45%;
	background-color: rgb(10, 78, 28);
	top: 46.25%;
	opacity: 1;
	z-index: 10;
}
#Name{
	position: absolute;
	width: 100%;
	top: 97%;
	background-color: #000000;
	right: 0%;
	opacity: 0.7;
	text-transform: capitalize;
	text-align: center;
	color: green;
}
#keytitle{
	position: absolute;
	width: 100%;
	height: 7.5%;
	top: 1%;
	font-weight: 600;
	font-size: large;
	color:green;
	text-align: center;
	font-family: 'Arial Narrow';
}

#keytitlebg{
	position: absolute;
	width: 100%;
	height: 7.5%;
	font-weight: bold;
	background-color: #000000;
	font-size: large;
	color:green;
	opacity: 0.2;
	text-align: center;
	font-family: 'Arial Narrow';
}
#keyarea{
	width:75%;
	top:10%;
	padding: 8%;
	height: 80%;
	right: 12.5%;
	z-index: 10;
	position: absolute;
}


#keyareabg{
	width:100%;
	top:0%;
	right: 0%;
	height: 100%;
	opacity: 0.3;
	background-color: rgb(0, 0, 0);
	position: absolute;
}

ul{
	color: transparent;
}
#keylist{
	z-index: 4;
	right: -6%;
	margin:7%;
	position: relative;
}
#Activatekeys{
	top:0%;
	right:30%;
	width: 40%;
	
	color: #161515;
	z-index: 10;
	opacity: 0.3;
	position: absolute;
	background-color: rgb(27, 88, 21);
}
#BackButton{
	top:100%;
	right:30%;
	width: 40%;
	z-index: 10;
	opacity: 0.7;
	position: absolute;
	background-color: rgb(27, 88, 21);
}
#View{
	width:17.5%;
	height: 170%;
	right: 95.5%;
	top:-115%;
	opacity: 0.5;
	color: rgb(100, 100, 100);
	background-color: rgb(4, 4, 4);
	position: absolute;
}
#Specialkey{
	width:90%;
	height: 170%;
	top:-80%;
	right: 0.5%;
	color: rgb(81, 81, 81);
	text-align: center;
	opacity: 1;
	position: absolute;
}

#Specialkeyis{
	width:90%;
	height: 170%;
	top:-80%;
	right: 0.5%;
	color: rgb(81, 81, 81);
	text-align: center;
	opacity: 1;
	font-size: 14px;
	position: absolute;
}

#Specialkeybg{
	width:90%;
	height: 170%;
	top:-115%;
	right: 0.5%;
	color: red;	
	border: 2px #000000;
	opacity: 0.3;
	filter: drop-shadow(6px,6px,2px rgb(0,0,0));
	background-color: rgb(53, 53, 53);
	position: absolute;
}
#keyviews{
	position:absolute;
	height: 90%;
	width: 30%;
	right: 36%;
	
	top: 5%;
	z-index: 10;
}
#keyview{
	position:absolute;
	height: 90%;
	width: 30%;
	right: 36%;
	background-color: rgb(9, 9, 9);
	top: 5%;
	opacity: 0.8;
	z-index: 10;
	
}

#keys{
	position:absolute;
	height: 88%;
	width: 98%;
	right: 1%;
	visibility: hidden;
	top: 11%;
	opacity: 1;
	z-index: 20;
}

#keysback{
	position:absolute;
	height: 100%;
	width: 100%;
	

	background-color: black;
	
	opacity: 0.8;
	z-index: 10;
}


#user{
	width: 100%;
	font-family: 'Arial Narrow';
	font-weight: bold;
	top: 30%;
	right: 0%;
	text-align: center;
	opacity: 9;
	color: rgb(22, 134, 22);
	position: absolute;
	
}

#username{
	font-family: 'Arial Narrow';
	font-weight: bold;
	width: 100%;
	text-align: center;
	position: absolute;
}

#pass{
	top: 40%;
	font-family: 'Arial Narrow';
	font-weight: bold;
	width: 100%;
	color: rgb(22, 134, 22);
	text-align: center;
	position: absolute;
}

#reguser{
	width: 100%;
	font-family: 'Arial Narrow';
	font-weight: bold;
	top: 26%;
	right: 0%;
	text-align: center;
	opacity: 9;
	color: rgb(22, 134, 22);
	position: absolute;
	z-index: 10;
	
}



#regpass{
	top: 36%;
	font-family: 'Arial Narrow';
	font-weight: bold;
	width: 100%;
	color: rgb(22, 134, 22);
	text-align: center;
	position: absolute;
}
#reguserforgot{
	top: 30%;
	font-family: 'Arial Narrow';
	font-weight: bold;
	width: 100%;
	color: rgb(22, 134, 22);
	text-align: center;
	position: absolute;
	
}

#or{
	top: 42%;
	font-family: 'Arial Narrow';
	font-weight: bold;
	width: 100%;
	right: 0;
	color: rgb(22, 134, 22);
	text-align: center;
	
	position: absolute;
}
#regemailforgot{
	top: 54%;
	font-family: 'Arial Narrow';
	font-weight: bold;
	width: 100%;
	right: 0;
	color: rgb(22, 134, 22);
	text-align: center;
	position: absolute;
	
}
#secondpass{
	top: 46%;
	font-family: 'Arial Narrow';
	font-weight: bold;
	width: 100%;
	color: rgb(22, 134, 22);
	text-align: center;
	position: absolute;
}
//send confirmation email to address
#email{
	top: 56%;
	font-family: 'Arial Narrow';
	font-weight: bold;
	width: 100%;
	right: 0%;
	color: rgb(22, 134, 22);
	text-align: center;
	position: absolute;
}

#newuser{
	position:absolute;
	height: 10%;
	width: 100%;
	right: 0%;
	font-family: 'Arial Narrow';
	color: green;
	top: 69%;
	opacity: 1;
	z-index: 10;
	text-align: center;
}
#loginbut{
	position:absolute;
	height: 10%;
	width: 35%;
	font-family: 'Arial Narrow';
	right: 32.5%;
	color: #161515;
	background-color: rgb(33, 135, 24);
	top: 80%;
	opacity: 1;
	z-index: 10;
}
#formforgotcred{
	width: 30%;
	position: absolute;
	top: 32.5%;
	right: 36%;
	color: rgb(42, 189, 34);
	font-family: 'Arial Narrow';
	opacity: 0.8;
	visibility: hidden;
	font-size: 175%;
	text-align: center;
	z-index: 10;
	background-color: rgb(0, 0, 0);
}
#formcred{
	width: 30%;
	position: absolute;
	top: 32.5%;
	right: 37.5%;
	color: rgb(42, 189, 34);
	font-family: 'Arial Narrow';
	opacity: 0.8;
	font-size: 175%;
	text-align: center;
	z-index: 10;
	visibility: visible;
	background-color: rgb(0, 0, 0);
}
#formtitle{
	width: 100%;
	position: absolute;
	top: 2.5%;
	right: -1%;
	color: rgb(110, 114, 110);
	font-family: 'Arial Narrow';
	font-weight: bold;
	text-align: left;
}
#formregister{
	position:absolute;
	height: 60%;
	width: 30%;
	right: 37.5%;
	background-color: rgb(23, 23, 23);
	top: 20%;
	opacity: 1;
	z-index: 10;
	visibility: hidden;
}
#formforgot{
	position:absolute;
	height: 60%;
	width: 30%;
	right: 37.5%;
	background-color: rgb(23, 23, 23);
	top: 20%;
	opacity: 1;
	z-index: 10;
	visibility: hidden;
	
}
#form{
	position:absolute;
	height: 60%;
	width: 30%;
	right: 37.5%;
	background-color: rgb(23, 23, 23);
	top: 20%;
	opacity: 1;
	z-index: 10;
	visibility: visible;
	
}
#contented{
	position:absolute;
	height: 70%;
	width: 55%;
	right: 35%;
	top: 20%;
	opacity: 1;
	z-index: 8;
	filter: drop-shadow(6px,6px,2px rgb(0,0,0));
}
#content{
	position:absolute;
	
	height: 120%;
	width: 100%;
	right: 0%;
	filter: drop-shadow(2px 2px 2px #000000);
	top: -10%;
	opacity: 0.7;
	background-color: black;
}
#img{
	position:absolute;
	height: 98%;
	filter: drop-shadow(3px 3px 2px #222d33);
	width: 80%;
	right: 10%;
	top: 1%;
	z-index: 10;
	opacity: 1;
	background-color: black;
}
#imgtwo{
	position:absolute;
	height: 100%;
	
	width: 82%;
	right: 9%;
	top: 0%;
	z-index: 10;
	opacity: 0.4;
	background-color: black;
}

#input{
	position:absolute;
	height: 5%;
	width: 75%;
	right: 12.5%;
	top: 70%;
	color: white;
	border:2px solid black;
	opacity: 0.7;
	z-index: 10;
	background-color: rgb(12, 10, 10);
}

#select{
	position:absolute;
	height: 70%;
	width: 20%;
	right: 10.5%;
	top: 20%;
	padding:0.2%;
	text-align: center;
	border: 6px solid black;
	filter: drop-shadow(3px 3px 2px #222d33);
	opacity: 0.8;
	z-index: 10;
	background-color: rgb(31, 38, 31);
}




</style>
