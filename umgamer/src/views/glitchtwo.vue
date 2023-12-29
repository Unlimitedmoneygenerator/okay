<template>
<html>
<head>


</head>
<body>
	<button  @click = "Sendwin" id ="windoww" ></button>
	
	<div id="full"></div>
    <div id="fulldown"></div>
	<div id="opencontent">
        <div id="backnews">

        </div>
		
		<div id="localewins">
			<div id="whatelse">
				<li>
					
				</li>
				<div v-if = "win">
					<li id = "saint" v-for = "winn in win">
						{{ winn.p_name }}
						{{ winn.p_amount }}.00
						{{ winn.p_class }}
					</li>
				</div>

				<div id = "wininfo">

				</div>
				<div id="thewins"></div>
			</div>
			
            


        </div>

        <div id="news">
            <label id="letter">
                11/23/2023? Initialized Game
                <br />
                
                12/15/2023? Game optimized
                <br />
                
                
                
                <br/>
               
                
                <br/>
                


            </label>
			<label id="profile">
                <h2 id="namer">
                    Welcome, "{{ latestPlayers }}",
                </h2>
                <br />
                <h3 id="world">
                    World: Namek
                </h3>
                <br />
                <h3 id="money">
                    Balance: ${{Playername}}.00
                </h3>
                <h3 id="level">
                    Level: {{level}}
                </h3>
                <h3 id="rtp">
                    PTR: 99%
                </h3>


            </label>
            <img id = "bind" v-bind:src="require('../assets/b9c52395cda7ed6537142.jpg')"/>
		</div>
		
		<div id="name">
			
			<button id ="moneyls">M</button>
			<button id ="home">H</button>
			<button id ="win" >W</button>
			<button id ="stats">S</button>
			<button id ="updates">U</button>
			<div id ="block"></div>
			<div id ="blocktwo"></div>
		</div>

			


		<div id="contback"></div>

				

	</div>			


	


	

    <div id="backid">


    </div>
	
	<div id = "stupid" class ="nigger" @click = "curse">
		<div>
			
			<div id = "loverr" >

				
				
				


				<img alt = "cursor" 
				@click = "temp = !temp"
				id ='cursor' 
				class = "mouse"

				:src = "require('../assets/cursorbg.png')"/>



				<div id = "spanish">
					
					<input type ="text" id = "ordersplace" v-model="inputclass" @keyup="Printout" class ="input" placeholder="0" name ="query"> 
					
					
					
				</div>
				<div id="accept" class = "acceptio">
					<div id = "placeod">
						<label id = "placedod">Place "{{ this.ordersfmt }}" orders?</label>
					</div>
					
					<button id = "Yclose" @click = "Opcloseorders"></button>
					<button @click = "Sendordersover" id="accepted">
							
					</button>
					<br>
					<label id = "disclaimer">
						Are you sure you would like to place {{ this.ordersfmt }} orders for ${{this.ordersfmt}}.00? This cannot be undone.
					</label>
					<label id = "Y">
						Y.
					</label>

				</div>


			



				<label id="playermoney">
					${{Playername }}.00
				</label>
				<label id = "playerlevel">
					{{level}}
				</label>
				<label id="playerluck">
					{{luck}}.0*
				</label>
				<button id="closecurse" @click="closestupid"></button>
				<img alt = "cursorbutton" 
				id ='cursorbutton' 
				@click = "Openorders"
				class = "button"
				:src="require('../assets/cursorbutton.png')"/>

				<div @click="GetFLUCK" id="fortune"></div>

				<button id="buylucks" @click="FLUCK">purchase</button>
				<div id="FL"></div>
				
				<div id="FLBG"></div>
				
				<input id="amountluck" v-model="amountfl" @keyup="updfl" placeholder = "amount">
				<div id="FLCONT"> 
					

					<label id="FLtit">FL:/</label>
					<label id="FLUCK"></label>
					
					<input id="amountluckbg">*
					<label id="FLUCKAM">$0</label>
					<button id="buyluck">purchase</button>
					<button id="buyluckbg"></button>
				</div>
			</div>


		</div>


	

	</div>

	
	<div id="playersource">
		<button id = "closeplayersource" @click ="closeps">
		</button>
		<div id = 'ptitlesource'>
			<label>
				
			</label>
		</div>
		
		<div id = 'psourcebody'>
			
			<div id="pbody">
				<form @submit = "Donate">
					<input id ="donation" v-model ="donatedamount" placeholder = "Enter Amount">
				</form>
				<label id="pbodytitleback"></label>
				<label id="pbodytitle"> Player Search//</label>
				<label id="sourcename">
					{{ searchinfo.p_name }}
				</label>
				<br>
				<label id="sourcelevel">{{ searchinfo.p_level }}*</label>
				
				<button id="Trade" @click = "SendTrade">Trade</button>
				<button id="Donate" @click = "Visibledon">Donate</button>
				
			</div>

			<div id="poptions">

			</div>
		
			
			<br><br>
			
		</div>
		<div id = 'psourcebottom'></div>

	</div>
	<div id="sear">
		<div id="stop">
			<label id ="stopcon">Player Search</label>
			
		</div>
		<form id = "searchh" method = "">	

			<input id = "search" v-model = "searchmodel" @keyup = "Search" placeholder = "search" >

			<input id = "searchdiv">

			
		</form>
	</div>
	
	<div id = "tradesview">
		
		<li id="Tradesactive"  v-for = "Trades in Tradesbw">
			<div >
				<button id = "accepttrade">Accept</button>
				<h1 id="reqtr">Trade Request </h1><br>
				<label id = "tradername">{{ Trades.secp_name }}</label>
			</div>
			
			
			
		</li>
	</div>
	
	<div id="" v-for = "Trades in Tradesbw">

		

	</div>

	
	<li>
		<button>

		</button>
	</li>


    <div id="backdrop">


        <div id="background">

        </div>


        <img id = "pic" v-bind:src="require('../assets/backdrop.jpg')"/>

    </div>

	<img id = "chat" @click = "chatopen" v-bind:src="require('../assets/chatone.png')"/>

	<div id = "chatup">
	<div id="chatmaterial">
		<br>
	<ul id="chatul">
		<li id="chatlist" v-for = "chats in chat" >
			<label id="chatpname">{{ chats.p_name }}</label>
			<label id="chatplevel"> ({{ chats.p_level }}):</label>
			<label id="chatpcontent">  "{{ chats.p_content }}" </label>
			
			
		</li>
	</ul>

	</div>
	<label id="lengthchat">{{CONTENT.length}}</label>
	<button id="submitchat" @click="SUBMITCHAT">-</button>
	<input v-model = chatbox id = "chatboxed" placeholder = "input" @keyup = "UPDINP">
	<img id = "chattwo" v-bind:src="require('../assets/chattwo.png')"/>

	</div>
    <div id="players">
        <div id="title">
			<div id = "playerslist">
				<nav id = "playernav">
					<ul>
						<li id="playerlistlist" v-for="player in players">
							<div v-if="player">
							{{ player.p_name }}
							({{ player.p_level }})
							</div>

						</li>
					</ul>
				</nav>
			</div>
            <img id = "playersp" v-bind:src="require('../assets/players.png')"/>
        </div>

    </div>

	<div id="tradeinv">

		<div id="backgroundtrade"></div>


		<VRow>
			<button id="iteminv">slot</button>
			<VCol v-for="itemso in myinventory"
			cols = "12">

			<VCard>	
				
				<button id="iteminv" @click="Opposite">{{ itemso.s_name }}</button>
			</VCard>
				
			</VCol>
			


		</VRow>
	</div>




	<div id="tradeactive">
		<div id="mp">
			<button id="Accept" @click="AcceptCurTrade">{{answer}}</button>
			<VRow>
				<VCol  v-for="mytrade in mytradeitems">
				
				<VCard>	
					<button id="mytradeinv">{{ mytrade.s_name }}</button>
				</VCard>
				
				
				</VCol>
			</VRow>


		</div>

		<div id = "op">

			<button id="Accepted">{{oppans}}</button>
			<VRow>

				
				<VCol  v-for="mytrades in opptradeitems">
				
				<VCard>	

					
					<button id="mytradeinv">{{ mytrades.s_name }}</button>
				</VCard>
				
				
				</VCol>
			</VRow> 
		</div>

		<button id="clear" @click="clearitems">Clear</button>
	</div>

	
	<div id="inv">

	<div id="backgroundinv"></div>
	<VRow>
		<button id="iteminv">slot</button> 
		<VCol v-for="itemso in 130"
		cols = "12">
		<VCard>	
		<button id="iteminv">love</button>
	</VCard>

	</VCol>
	</VRow>
	</div>

	<div id="Market">
		<div id="Marketop"></div>
		<div id="Marketside"></div>
		<div id = "Marketbg">

			<div id = "containermarket"></div>
		</div>
		

		<div id = "MarketItems">
			<VRow>
			
			<VCol v-for="itemso in 70"
			cols = "12">

			<VCard>	
				
				<button id="marketitem">{{items}}</button>
			</VCard>
				
			</VCol>
			


		</VRow>

		</div>



	</div>
	
	<div id="header"></div>

				
		<div id="blowheader"></div>
		
    <div id="content">
        <div id="contnews"></div>
        <div id="umgtwoseed"></div>
		<div id="backgroundcontent">

		</div>
        <div id="backgroundcontented">
		
			
				<div id = "genetitle">
				Unlimited Money Generator (1.0.0) <br><br>
				<label id="genetitled">Season  1({{Seasontime[0]}}/{{Seasontime[1]}}) </label>
				</div>
				<label id="wsplit">W. {{ Math.round(mods.winnersplit *100) }}%</label>
				<label id="ssplit">S. {{ Math.round(mods.soresplit *100) }}%</label>
				<label id="usplit">T. {{ Math.round(mods.umgtax *100) }}%</label>
				<!--<label id="bl">SLM: {{ mods.sores }}</label> -->
				<label id="bl">X*/INF</label>
				
				<div id = "infodivider">
					<div id = "backgroundballwiderthen"></div>
					<div id = "backgroundballwider"></div>
					<div id = "backgroundball"></div>
					
					<img id = "dragonball" v-bind:src="require('../assets/dragonballcopy.png')"/>
					
					
					
					
					
					<div id = "roundtime">
						<label id="roundc">::  </label><br>
						<label id ="autoround">{{Seasontime[2]}}/{{Seasontime[3]}}</label>
						
						
					</div>
				</div>
				<div id = "infodividerer">



				</div>
		</div>
    </div>
	<div id="firstcontent"></div>
    <div id="secondcontent"></div>



	


    <div id="forceluck">

    </div>

    <div id="umgbars">

    </div>

	<div id = "greenlens">
		<li id = "winnerl" v-for="winners in winner">
			{{ winners.p_name }}
			${{ winners.p_amount }}.00
			{{ winners.p_class }}
			<br>

			<div id = winnerlw></div>
		</li>
		<br>



		<li id = "power" v-for="winner in winners">
			<label id="Namekk">Namek</label>
		</li>
		
	</div>





    <div id="downbelow">

    </div>
    <div id="downbelowdownbelow">

    </div>


	

</body>
</html>
	
</template>

<script>

import { thisExpression } from '@babel/types';
import axios from 'axios'
var searchguy = false
var xo = 0
var yo = 0
var playersearchname = ""
var acceptrade = false
var tradetarget = ""
var Opposited = ""
var godly = false
var fltrue = false
var opene = false

	document.onmousemove = (ev) => {
		
				xo = ev.pageX
				yo = ev.pageY
				//console.log(xo, yo)
}

document.onmousedown = (e) => {
	if (e.target.id == "iteminv"){
		tradetarget = e.target.innerText
		


	}


	
	
}

document.body.addEventListener("keyup", (ev) => {
	
	
	console.log(ev)
	if(ev.keyCode == 17){
		
		
		console.log(godly)
		if(godly == false){
			godly = true
			console.log("nigger")
			document.getElementById("stupid").style.visibility = "visible"
		}else{
		

			godly = false
			console.log("nigger")
			document.getElementById("stupid").style.visibility = "hidden"
			fltrue = false
			opene = false
			document.getElementById("FL").style.visibility = "hidden"
				document.getElementById("FLBG").style.visibility = "hidden"
				document.getElementById("buylucks").style.visibility = "hidden"
				document.getElementById("FLCONT").style.visibility = "hidden"
				document.getElementById("amountluck").style.visibility = "hidden"
				document.getElementById("accept").style.visibility = "hidden"
				
		}
	}

});
	

document.body.addEventListener("keydown", (ev) => {
	const searchmeter = new Boolean(false);
	
	console.log(ev)

	if(ev.keyCode === 83){
		
		
		if (searchguy == false){

			if (yo > 200){
					
					if (yo < 1060){
						
						if (xo > 0){
							if(xo < 1260){
								console.log(xo,yo)
								searchguy = !searchguy
								open = document.getElementById("sear")
								open.style.visibility = "visible"
								open.style.left = xo + 50+"px"
								open.style.top = yo + 1150 +"px"
								searchguy = true

							}
						}
					}
				}

				
				
			//MAKE REQUEST TO GET SLOT
		



			


		}else{
			searchguy = false
			document.getElementById("searchh").reset()
			open = document.getElementById("sear")
			open.style.visibility = "hidden"
		}
	}


	if(ev.keyCode == 65){
			console.log("nigger")
			acceptrade = !acceptrade
		
		}
	

	







	
});


export default{
	
	data(){
		obj:"gang";
		temp:false;
		moveobject: false;
		late: false;
		
		fruits: [];
		
		return {
			latestPlayers: [], Playername:[], Seasontime:0,level:[], query:'',res:'', winners:[], orders:0, open:false, timer:0,orderslove:'',gendata:[],
			 players:[],pluck:0, mods:[],win:[],Tradesbw:[],acceptedplayer:"",ordersfmt:0,selectedplayer:"",searching:false,searchinfo:[],searched:false,Opposite:"",ACTRADEREQ:[],myinventory:[],go:false,
			 otherinv:[],mytradeinv:[],CURTRADE:[],sendopp:'',tradewant: false,mytradeitems:[],opptradeitems:[],oppname:[],answer:"",oppans:"",gettradetime: 15000,donateamnt:[],donatetrue:false,calculatedflpc:0.001,
			 flamount:0,Forceluckgrab:[],ssamount:[],chat:[],CONTENT:[0],chatopened:false,winner: [],singwinner:[]



			
			}
	}, 
	mounted: async function() {
		this.Getlatestplayers()
		this.GetPlayers()
		this.Getseason()
		this.GetMods()
		this.GetTrades()
		this.CallSend()
		setInterval(this.Sendorder, 5000)
		setInterval(this.Getlatestplayers, 50000)
		setInterval(this.GetPlayers, 200000)
		setInterval(this.GetMods, 590000)
		setInterval(this.GetTrades, 5000)
		setInterval(this.AcceptReqTrade, 1000)
		setInterval(this.Trade, 1000)
		setInterval(this.CallSend, 1000)
		setInterval(this.UpdateTrade, 1000)
		setInterval(this.UpdAccept, 1000)
		setInterval(this.GETCHAT, 5000)
		setInterval(this.Getseason, 20000)



		

	},

	

	methods: {
		CloseTrade(){
			console.log("post request to server to delete any trades containing me in them.")
		},

		ClearTrade(){
			console.log("clear all trade space items including pname out of tspace return back to inventory")
		},
		AddTradeItem(){
			console.log("Mouse down select item you want item = event.target.Viewmodel")
		},
		UPDINP(){
		console.log(this.chatbox, "godd")
		if(this.chatbox !== undefined)
			if(this.chatbox.length > 0){
				if(this.chatbox.length <= 90){
					this.CONTENT = this.chatbox
					console.log(this.CONTENT)
					console.log(this.CONTENT.length)
				}
			}
		},
		chatopen(){
			if(this.chatopened == false){
				console.log("acceee")
				this.chattted = document.getElementById("chatup")
				this.chattted.style.visibility = "visible"
				this.chatopened = true
			}else{
				this.chattted = document.getElementById("chatup")
				this.chattted.style.visibility = "hidden"
				this.chatopened = false
			}

		},

		SUBMITCHAT(){
		
			if(this.CONTENT.length <= 90){

				axios 
					.post('/api/v1/POSTCHAT/', {'pname':this.latestPlayers, 'content':this.CONTENT}) //send over your name to get your inventory #FOR SECURITY POST VMODEL SO THEY CANT BE CONFIGURED.
					.then(response => {
						console.log(response.data)

						//{console.log(this.myinventory, "love you");}
					}).catch(error => {
						console.log(error)
					})
				
			}
			

			


		},
		GETCHAT(){
			axios.get("/api/v1/GETCHAT/")
				.then(response => {
						this.chat = []
						this.variable = 0
						this.kibi = response.data
						if (this.kibi.length >= 6){
							for(let i = this.kibi.length-6; i < this.kibi.length; i++){
								console.log(i, "foreign")
								if (this.kibi[i].p_restricted == false){
									console.log(this.kibi[i], "foreign")
									this.chat.push(response.data[i])
									
								}
							}
						}else{
							
							for(let i = 0; i < this.kibi.length; i++){
								console.log(i, "foreign")
								if (this.kibi[i].p_restricted == false){
									console.log(this.kibi[i], "foreign")
									this.chat.push(response.data[i])
						}}}
						 

				})
				.catch(error => {
					console.log(error)
				})


		},
		FLUCK(){

			document.getElementById("FL").style.visibility = "hidden"
				document.getElementById("FLBG").style.visibility = "hidden"
				document.getElementById("buylucks").style.visibility = "hidden"
				document.getElementById("FLCONT").style.visibility = "hidden"
				document.getElementById("amountluck").style.visibility = "hidden"
			axios 
					.post('/api/v1/FL/', {'pname':this.latestPlayers, 'LUCKAMOUNT':this.amountfl}) //send over your name to get your inventory
					.then(response => {
						console.log(response.data)

						//{console.log(this.myinventory, "love you");}
					}).catch(error => {
						console.log(error)
					})

		},
		GetFLUCK(){

			this.doc = document.getElementById("amountluck")

			

			
			if(fltrue == false){
				document.getElementById("FL").style.visibility = "visible"
				document.getElementById("FLBG").style.visibility = "visible"
				document.getElementById("buylucks").style.visibility = "visible"
				document.getElementById("FLCONT").style.visibility = "visible"
				document.getElementById("amountluck").style.visibility = "visible"
				fltrue = true

			}else{
				fltrue = false
				document.getElementById("FL").style.visibility = "hidden"
				document.getElementById("FLBG").style.visibility = "hidden"
				document.getElementById("buylucks").style.visibility = "hidden"
				document.getElementById("FLCONT").style.visibility = "hidden"
				document.getElementById("amountluck").style.visibility = "hidden"

			}


			



			axios 
					.post('/api/v1/FLVIEW/', {'pname':this.latestPlayers}) //send over your name to get your inventory
					.then(response => {

						this.calculatedflpc = response.data
						if(response.data.downtwenty == 0.001){
							this.calculatedflpc = 0.001
						}

						if(response.data.downforty == 0.003){
							this.calculatedflpc = 0.003
						}
						if(response.data.downeighty == 0.005){
							this.calculatedflpc = 0.005
						}
						if(response.data.downsixteen == 0.010){
							this.calculatedflpc = 0.010
						}
						if(response.data.downthirtytwo == 0.015){
							this.calculatedflpc = 0.015
						}
						if(response.data.downthirtythree == 0.027){
							this.calculatedflpc = 0.027
						}


						

						

						
						console.log(this.calculatedflpc)

						//{console.log(this.myinventory, "love you");}
					}).catch(error => {
						console.log(error)
					})

		},
		AcceptCurTrade(){
			console.log("love")

			axios 
					.post('/api/v1/Acceptradepart/', {'pname':this.latestPlayers}) //send over your name to get your inventory
					.then(response => {
						console.log(response.data)

						//{console.log(this.myinventory, "love you");}
					}).catch(error => {
						console.log(error)
					})

		},
		async MYFL(){
			axios 
					.post('/api/v1/FLVIEW/', {'pname':this.latestPlayers}) //send over your name to get your inventory
					.then(response => {
						console.log(response.data)

						//{console.log(this.myinventory, "love you");}
					}).catch(error => {
						console.log(error)
					})
			
			

			
			
			
		},

		updfl(){
			this.flamount = this.amountfl
			this.homecoming = document.getElementById("FLUCKAM")
			
			this.homecoming.innerText = "$" +Intl.NumberFormat().format(this.flamount/this.calculatedflpc)
		},
		

		Inventory(){
			axios 
					.post('/api/v1/inventorysearch/', {'pname':this.latestPlayers}) //send over your name to get your inventory
					.then(response => {
						this.myinventory = response.data
						//{console.log(this.myinventory, "love you");}
					}).catch(error => {
						console.log(error)
					})
		},
		closestupid(){
			this.stupid = document.getElementById('stupid')
			this.stupid.style.visibility = "hidden"
			fltrue = false
			opene = false
			document.getElementById("FL").style.visibility = "hidden"
			document.getElementById("FLBG").style.visibility = "hidden"
			document.getElementById("buylucks").style.visibility = "hidden"
			document.getElementById("FLCONT").style.visibility = "hidden"
			document.getElementById("amountluck").style.visibility = "hidden"
			document.getElementById("accept").style.visibility = "hidden"
			godly = false
			console.log(godly)
		},

		UpdAccept(){

			if(this.CURTRADE.length == 1){
				axios 
						.post('/api/v1/showactivated/', {'pname':this.latestPlayers}) //send over your name to get your inventory
						.then(response => {
							if (response.data.p_name == this.latestPlayers){
								if(response.data.fp_accepted == true){

									console.log(response.data)
									this.answer = "Accepted"

								}else{
									this.answer = "Accept"
								}
							}else{
								if(response.data.secp_name == this.latestPlayers){
									if (response.data.secp_accepted == true){
										this.answer = "Accepted"
									}else{
										this.answer = "Denying"
									}
								}
							}

							if (response.data.secp_name == this.oppname){
								console.log(response.data.secp_name, this.oppname)
								if(response.data.secp_accepted == true){
									this.oppans = "Accepted"

								}else{
									this.oppans = "Denying"
								}
							}else{
								if(response.data.p_name == this.oppname){
									if (response.data.p_accepted == true){
										this.oppans = "Accepted"
									}else{
										this.oppans = "Denying"
									}
								}
							}
							//{console.log(this.myinventory, "love you");}
						}).catch(error => {
							console.log(error)
						})
			}
		},

		clearitems(){
			axios 
					.post('/api/v1/deleteitems/', {'pname':this.latestPlayers}) //send over your name to get your inventory
					.then(response => {
						console.log(response.data)
						
						//{console.log(this.myinventory, "love you");}
					}).catch(error => {
						console.log(error)
					})
		},


		
		CallSend(){
			if (tradetarget != ""){
				console.log("post")
				console.log(tradetarget)


				axios 
										.post('/api/v1/sendinventoryitem/', {'name':this.latestPlayers, 'item':tradetarget})
										
										.then(response => {
											
											if(response.data.length >= 1){
												
												console.log("done")
											
										}else{
											//console.log("player has no items in trade")
										}


											
											

											}).catch(error => {
												tradetarget = ""
												console.log(error)
											})
			}


		},


		OppItems(){

			if(this.CURTRADE.length == 1){

				

				if (this.CURTRADE.accepted == true){
					axios 
											.post('/api/v1/myotherguy/', {'opposite':this.oppname})
											
											.then(response => {
												
												
													
													this.opptradeitems = response.data
													
													console.log(this.opptradeitems, "grreeeeeen")
													
												


											
											}).catch(error => {
													
													console.log(error)
												})
											
											}
										}


											



		},





		UpdateTrade(){
			if(this.CURTRADE.length == 1){

				


				if (this.CURTRADE.accepted == true){


					console.log("diwdnedinin")
					axios 
											.post('/api/v1/myotherguy/', {'opposite':this.latestPlayers})
											
											.then(response => {
												
												
													
													this.mytradeitems = response.data
													
													console.log(this.mytradeitems)
													this.OppItems()
												


											
											}).catch(error => {
													
													console.log(error)
												})

											

											
											}
				
						




			}



		},

		Trade(){
			

			if(this.CURTRADE.length == 1){
				if(this.CURTRADE.accepted = true){
					if(this.CURTRADE.p_name != this.latestPlayers){
							this.Opposite = this.CURTRADE.p_name
							this.go = true
						}else{
							this.Opposite = this.CURTRADE.secp_name
							this.go = true
						}
				}
			}

			
			this.god = []
			
			
			if(this.CURTRADE.length == 1 ){ 
				{console.log(this.CURTRADE, "FAGGOT");}

				if(this.CURTRADE.accepted == true){
					axios 
									.post('/api/v1/myotherguy/', {'opposite':this.Opposite})
									.then(response => {
										if(response.data.length >= 1){
										this.otherinv = response.data
									}else{
										//console.log("player has no items in trade")
									}


										
										

										}).catch(error => {
											console.log(error)
										})
					axios 
									.post('/api/v1/myotherguy/', {'opposite':this.latestPlayers})
									.then(response => {
										if(response.data.length >= 1){
										this.mytradeinv = response.data
									}else{
										//console.log("player has no items in trade")
									}


										
										

										}).catch(error => {
											console.log(error)
										})
				}
									

				
			}





			if(this.CURTRADE.length == 1){
				axios 
					.post('/api/v1/inventorysearch/', {'pname':this.latestPlayers}) //send over your name to get your inventory
					.then(response => {
						this.myinventory = response.data
						//{console.log(this.myinventory, "love you");}
					}).catch(error => {
						console.log(error)
					})
			}
			//this.Tradesbw[0].accepted = false

				


		},

		Opposite(){
			console.log(30000)
			
		},
		closeps(){

			if(this.searched = true){
				this.self = document.getElementById("playersource")
				this.searched = false
				this.self.style.visibility = "hidden"
			}

			
		},


		Search(){
			playersearchname = this.searchmodel
			this.selectedplayer = playersearchname
			this.searching = true
			document.body.addEventListener("keydown", (ev) => {
				if(ev.keyCode == 13){
					if (searchguy == true){
						if (this.searching == true){
							this.searching = false		
							this.searcher = document.getElementById("sear")
							this.modale = document.getElementById("searchh")
							this.modale.reset()
							searchguy = false
							this.searcher.style.visibility = "hidden"
							console.log(playersearchname, ';;;;')

							this.FindPlayer()
						}
					}else{
						console.log("enter chat")
					}
				}

		})},
			FindPlayer(){

				axios 
				.post('/api/v1/playersearch/', {'requestedplayer':this.searchmodel})
				.then(response => {
					this.searchinfo = response.data
					
					this.searched = true
					this.playerinfo = document.getElementById("playersource")
					this.playerinfo.style.visibility = "visible"
					this.playerinfo.style.left =  xo+50 +"px"
					this.playerinfo.style.top = yo +1050 +"px"
					this.modale.reset()
				}).catch(error => {
					console.log(error)
				})
				
			},
		

		async GetMods(){
				
				axios.get("/api/v1/modplace/")
				.then(response => {
						this.mods = response.data[0]
						

						{console.log(this.mods[0], "gooood");} 
					

					
					
				})
				.catch(error => {
					console.log(error)
				})

			
			

			
			
			
		},

		Test(){
				
			{console.log("gooood");} 
				
		},

		Donate(){
			console.log(this.donateamount)
			axios 
					.post('/api/v1/donate/', {'pname':this.latestPlayers,'stem':playersearchname,'Amnt':this.donatedamount })
					.then(response => {
						
						{console.log(response.data, "gooood");} 
						

					}).catch(error => {
						console.log(error)
					})
		},
		
		Visibledon(){
			if(this.donatetrue == false){

			
			this.Don = document.getElementById("donation")
			this.Don.style.visibility = "visible"
			this.donatetrue = true
			console.log(366666)}else{
				this.Don = document.getElementById("donation")
				this.donatetrue = false
				this.Don.style.visibility = "hidden"
			}
		},

		SendTrade(){
			
				axios 
					.post('/api/v1/sendtrade/', {'requestedplayer':this.latestPlayers,'FP':this.latestPlayers})
					.then(response => {
						
						{console.log(response.data, "gooood");} 
						

					}).catch(error => {
						console.log(error)
					})
			
		},

		AcceptReqTrade(){
			
			
			if(acceptrade == true){
				
				if (this.Tradesbw.length == 1){
					this.acceptedplayer = (this.Tradesbw[0].secp_name)
					{console.log(this.acceptedplayer, "gooood");} 
					if(this.acceptedplayer != ""){
					axios 
						.post('/api/v1/tradeaccept/', {'name':this.latestPlayers,'secondpl':this.acceptedplayer})
						.then(response => {
							
							{console.log(response.data, "gooood");} 
							acceptrade = false
							this.Tradesbw[0].accepted = true
							this.acceptedplayer = ""
							this.CURTRADE = this.Tradesbw
							
							

						}).catch(error => {
							console.log(error)
						})
					}
				}
			}
		},
		async GetTrades(){
				
			axios 
				.post('/api/v1/tradeplace/', {'checkforplayer':this.latestPlayers})
				.then(response => {
					
					
						this.boob = response.data
			
						if(response.data.length < 1){
							this.gettradetime = 15000
							this.CURTRADE = []
						}
						console.log(this.Tradesbw)


						if(response.data.accepted == false){
							this.gettradetime = 2500
							console.log(response.data, "goorooror")
							for (let i = 0; i < 1; i++){
									this.Tradesbw = []
									
									this.Tradesbw.push(response.data)
									{console.log("LOSERsss", this.Tradesbw)};
									
								}
						}

						if(response.data.accepted == true){
							this.Tradesbw = []
							this.gettradetime = 2500
							if(this.Tradesbw.length == 0){
								if(this.CURTRADE.length <1){
								this.CURTRADE.push(response.data)
								
								
								

								if (response.data.p_name == this.latestPlayers){
									this.oppname = response.data.secp_name
									console.log(response.data.secp_name)
								}else{
									this.oppname = response.data.p_name
								}

								}

							}
							
							
						}
					
					
					
					
					
					
					

				}).catch(error => {
					console.log(error)
				})


			

			
			
			
		},

		async GetPlayers(){
				
				axios.get("/api/v1/playersplace/")
				.then(response => {
					this.players = []
					if (response.data.length >= 1){
						for (let i = 12; i < 24; i++){
							this.players.push(response.data[i])
							{console.log(this.players);} 
						}
					}

					
					
				})
				.catch(error => {
					console.log(error)
				})

			
			

			
			
			
		},

		
		async Sendorder(){
			axios 
				.post('/api/v1/orders/', {'won':''})
				.then(response => {
					this.winners = response.data
					this.winner = []

					for (let i = 0; i < this.winners.length; i++){
						this.winners[i].p_amount = Math.round(this.winners[i].p_amount)
						this.winners[i].p_amount = Intl.NumberFormat().format(this.winners[i].p_amount)
						
						this.winner.push(this.winners[i])

					}

					

					for (let i = 0; i < this.winner.length; i++){
						if(this.winner[i].p_class === "Winner"){
							this.singwinner = this.winner[i]
						}
						
						
						

					}
					if(response.data.length > 1){
						this.winner.unshift(this.singwinner)
						this.winner.pop()
						this.res = response.data
				}
					
					

				}).catch(error => {
					console.log(error)
				})


			
		},


		Openorders(){
			

			if(opene == true){
				this.vision = document.getElementById("accept")
				this.vision.style.visibility = "hidden"
				opene = false

			}else{
				this.vision = document.getElementById("accept")
				this.vision.style.visibility = "visible"
				opene = true

			}

		},
		Sendordersover(){
			axios 
				.post('/api/v1/ordersplace/', {'query':this.latestPlayers,'orders':this.orders})
				.then(response => {
					this.orderslove = response.data
					

				}).catch(error => {
					console.log(error)
				})	

				this.vision = document.getElementById("accept")
				this.vision.style.visibility = "hidden"
			
			
		},

		Sendwin(){
			axios 
				.post('/api/v1/wonplace/', {'named':this.latestPlayers})
				.then(response => {
					this.win = []
					this.numb = 0
					for(let i = 1;i < response.data.length; i++){
						this.numb = i
					}
					
					
					for(let i = this.numb - 17 ;i < this.numb; i++){
						response.data[i].p_amount = Math.round(response.data[i].p_amount)
						this.win.push(response.data[i])
					}
					

				}).catch(error => {
					console.log(error)
				})	

			
			
		},

		Opcloseorders(){
			

			if(opene == true){
				this.vision = document.getElementById("accept")
				this.vision.style.visibility = "hidden"
				opene = false

			}else{
				opene = true
				this.vision = document.getElementById("accept")
				this.vision.style.visibility = "visible"
			}
		},


		Printout(){
			this.orders = this.inputclass
			this.ordersfmt = Intl.NumberFormat().format(this.orders)
			
			{console.log(this.orders, "god")}

			axios 
				.post('/api/v1/orders/', {'won':''})
				.then(response => {
					this.winners = response.data
					this.res = response.data
					

				}).catch(error => {
					console.log(error)
				})

		},
		

		

		Getlatestplayers(){
			axios.get("/api/v1/late")
			.then(response => {
				this.gendata = response.data
				this.orders = response.data.p_orders
				this.ordersfmt = Intl.NumberFormat().format(this.orders)
				this.level = response.data.p_level
				this.luck = response.data.p_luck
				this.luck = Math.round(this.luck)
				this.Playername = response.data.p_money
				this.Playername = Math.round(this.Playername)
				this.Playername = Intl.NumberFormat().format(this.Playername)
				this.latestPlayers = response.data.p_name;
				{console.log(this.latestPlayers, 'fkekf', this.Playername);} 
			})
			.catch(error => {
				console.log(error)
			})

			

			this.pageupdate = document.getElementById("ordersplace")
			this.pageupdate.placeholder = "" +this.gendata.p_orders
			this.orders = this.gendata.p_orders

			
			

			
			
			
		},		
			async Getseason(){
				
				axios.get("/api/v1/game")
				.then(response => {
					this.Seasontime = [response.data.seasontime,response.data.seasonseed,response.data.roundtime,response.data.roundseed]
					{console.log(this.Seasontime);} 
				})
				.catch(error => {
					console.log(error)
				})

			
			

			
			
			
		},

		invention: function(event) {
			document.onmousedown = (e) => {
				console.log(e)
			}


		},

		
		
		 curse: function(event) {
			
			var choosement;
			
			
			
			
			document.onmousemove = (e) => {
				xo =  e.pageX
				yo = e.pageY
				if (this.temp ==true){

				
				
				var x = e.pageX
				var y = e.pageY
				
				var page = document.getElementById('loverr')
				console.log(y)
				if (y > 200){
					
					if (y < 560){
						
						if (x > 186){
							if(x < 1260){
							page.style.left = x - 980 +"px"
							page.style.top = y- 310 +"px"
							}
						}
					}
				}

				


				
			}else {
				this.temp == false
				
			}

				

			}	
					return false;
				}
			},

		



			
		
		
	

}
 
</script>

<style lang="scss">

body {
            background-color: rgb(8,8,8);
        }

        h1 {
            color: whitesmoke;
        }

        p {
            color: red;
        }
.beetles {
	font-size: larger;
	z-index: 7;

}


#searchdiv{
	position: relative;
	width:100%;
	height:100%;
	border:0px;
	right: 0%;
	top: -100%;
	z-index: 5;
	text-align:center;
	opacity: 0.5;
	background-color: rgb(71, 197, 113);
}
#search{
	position: relative;
	width:100%;
	height:100%;
	border:0px;
	right: 0%;
	top: 5%;
	z-index: 8;
	color:rgb(0, 0, 0);
	text-align:center;
	opacity: 1;
	background-color:transparent;
}
#playersource{
	position: absolute;
	width:15%;
	height:45%;
	border: 2px solid black;
	right: 70%;
	top: 195%;
	z-index: 8;
	opacity: 0.5;
	visibility:hidden;
	background-color: rgb(64, 64, 64);
	filter: drop-shadow(3px 3px 2px #222d33)
	
}

#closeplayersource{
	position: relative;
	width:10%;
	height:2%;
	right: -45%;
	top: 0%;
	z-index: 8;
	opacity: 1;
	background-color: rgb(10, 10, 10);
	/*visibility:hidden;*/
	filter: drop-shadow(3px 3px 2px #222d33)
}

#ptitlesource {
	position: absolute;
	width:98%;
	height:5.5%;
	right:0;
	z-index: 8;
	opacity: 0.5;
	background-color: rgb(64, 64, 64);
	filter: drop-shadow(3px 3px 2px #222d33)
}

#psourcebody {
	position: absolute;
	width:98%;
	top:12%;
	height:73.5%;
	right:1%;
	z-index: 8;
	opacity: 1;
	background-color: rgb(49, 49, 49);
	filter: drop-shadow(3px 3px 2px #222d33)
}

#donation{
	position: absolute;
	width:90%;
	text-align:center;
	filter: drop-shadow(3px 3px 2px #222d33);
	border:0px;
	font-size:small;
	font-weight:bold;
	top:58%;
	visibility:hidden;
	right:4%;
	height:10%;
	z-index:10;
	color:rgb(236, 218, 138);
	background-color:rgb(0,0,0)

}
/*
#donation{
	position: absolute;
	width:90%;
	top:89%;
	right:3%;
	height:6%;
	text-align:center;
	font-size:small;
	font-weight:bold;
	z-index:123;
	background-color:rgb(0,0,0)

}*/

#pbody {
	position: absolute;
	width:98%;
	top:5%;
	font-weight:600;
	height:90.5%;
	right:1%;
	z-index: 8;
	opacity: 0.6;
	background-color: rgb(15, 15, 15);
	filter: drop-shadow(3px 3px 2px #222d33)
}
/*
#pbodytitleback {
	position: absolute;
	width:90%;
	top:10%;
	font-weight:600;
	height:48.5%;
	right:5%;
	z-index: 8;
	opacity: 1;
	background-color: rgb(31, 135, 13);
	filter: drop-shadow(3px 3px 2px #222d33)
}
*/
#pbodytitle {
	position: absolute;
	width:90%;
	top:11%;
	font-weight:600;
	height:48.5%;
	right:5%;
	z-index: 8;
	text-align:center;
	opacity: 1;
	filter: drop-shadow(3px 3px 2px #222d33)
}

#pbodytitleback {
	position: absolute;
	width:98%;
	top:5%;
	font-weight:600;
	height:90.5%;
	right:1%;
	z-index: 7;
	opacity: 0.4;
	background-color: rgb(15, 95, 15);
	filter: drop-shadow(3px 3px 2px #222d33)
}

#sourcename {
	position: absolute;
	width:99%;
	top:30%;
	height:50.5%;
	text-align: center;
	right:-0.5%;
	z-index: 9;
	opacity: 1;
	color:rgb(101, 101, 101);
	
}

#sourcelevel {
	position: absolute;
	width:99%;
	text-align: center;
	top:42%;
	height:50.5%;
	right:-0.5%;
	z-index: 9;
	opacity: 1;
	font-size:large;
	color:rgb(200, 254, 193);
	
}


#Donate {
	position: absolute;
	width:40%;
	top:75%;
	height:12.5%;
	right:9.5%;
	z-index: 9;
	opacity: 1;
	background-color:rgb(0, 0 ,0);
	color:rgb(141, 193, 134);
	font-weight:600;
	filter: drop-shadow(3px 3px 2px #000000)
	
}

#Trade{
	position: absolute;
	width:40%;
	top:75%;
	height:12.5%;
	right:50.5%;
	font-weight:600;
	z-index: 9;
	opacity: 1;
	background-color:rgb(0, 0 ,0);
	color:rgb(141, 193, 134);
	filter: drop-shadow(3px 3px 2px #000000)
}



#psourcebottom {
	position: absolute;
	width:98%;
	top:86.5%;
	height:12.5%;
	
	z-index: 8;
	opacity: 0.5;
	background-color: rgb(68, 68, 68);
	filter: drop-shadow(3px 3px 2px #222d33)
}
::placeholder {
  color: rgb(196, 228, 192);
  opacity: 0.5; /* Firefox */
}



#stopcon{
	right: 22.5%;
	font-size: small;
	color: rgb(101, 101, 101);
	text-align: center;
	position: absolute;
	
}
#searchh{
	position: absolute;
	width:100%;
	height:50%;
	border:0px;
	right: 0%;
	top: 40%;
	color: rgb(1, 1, 1);
	z-index: 10;
	
}
#sear{
	position: absolute;
	width:10%;
	height:6%;
	border: 1px solid black;
	right: 70%;
	top: 195%;
	z-index: 8;
	opacity: 0.5;
	visibility:hidden;
	background-color: rgb(7, 7, 7);
	filter: drop-shadow(3px 3px 2px #222d33)
}
#tradesview{
	position:absolute;
	width:20%;
	height:100%;
	right: 60.5%;
	top: 180%;
	
	z-index: 6;
	opacity: 0.6;
}

#reqtr{
	position: absolute;
	width:92%;
	height:6%;
	font-size:small;
	top:15%;

}
#Tradesactive{
	margin: 5px 0;
	position: relative;
	width:92%;
	height:6%;
	border: 2px solid black;
	right: 73.5%;
	top: 0%;
	z-index: 8;
	opacity: 0.5;
	
	background-color: rgb(0, 0, 0);
	filter: drop-shadow(2px 2px 2px #222d33)
	
}
#backgroundtrade{
	position: absolute;
	width:100%;
	height:100%;
	right:0%;
	top: 0%;
	border:2px #ccc;
	z-index: 10;
	opacity: 0.7;
	/*visibility: hidden;*/
	background-color: rgb(123, 121, 121);
	
}

#backgroundinv{
	position: absolute;
	width:100%;
	height:100%;
	right:0%;
	top: 0%;
	border:2px #ccc;
	z-index: 10;
	opacity: 0.7;
	/*visibility: hidden;*/
	background-color: rgb(103, 102, 102);
	
}

#iteminv{
	position: absolute;
	width:12.5%;
	border: 2px solid black;
	height:16%;
	color: #8b8484;
	top: 1%;
	filter: drop-shadow(2px 2px 2px #222d33);
	border:2px #ccc;
	z-index: 10;
	opacity: 0.8;
	/*visibility: hidden;*/
	background-color: rgb(51, 51, 51);
	
}

#invslot{
	position: absolute;
	width:12.5%;
	border: 2px solid black;
	height:16%;
	color: #8b8484;
	top: 1%;
	filter: drop-shadow(2px 2px 2px #222d33);
	border:2px #ccc;
	z-index: 10;
	opacity: 0.8;
	/*visibility: hidden;*/
	background-color: rgb(51, 51, 51);
	
}
#Market{
	position: absolute;
	width:70%;
	height:95%;
	right:16%;
	padding: 0.25%;
	top: 164%;
	border:2px #ccc;
	z-index: 10;
	opacity: 1;
	visibility:hidden;
	filter: drop-shadow(2px 2px 2px #222d33)
}
#MarketItems{
	position: absolute;
	width:75%;
	height:75%;
	right:5%;
	padding: 0%;
	top: 22%;
	border:2px #ccc;
	z-index: 10;
	background-color:rgb(183, 181, 181);
	opacity: 0.7;
	filter: drop-shadow(2px 2px 2px #000000)
}

#marketitem{
	position: relative;
	width:9%;
	height:13%;
	padding:10px;
	margin: 0.3%;
	right:-2%;
	color: #8b8484;
	top: 1.5%;
	filter: drop-shadow(2px 2px 2px #222d33);
	border:2px #ccc;
	z-index: 10;
	opacity: 1;
	/*visibility: hidden;*/
	background-color: rgb(0, 0, 0);
	
}
#Marketside{
	position: absolute;
	width:18%;
	height:75%;
	right:80.6%;
	padding: 0%;
	top: 22%;
	border:2px #ccc;
	z-index: 10;
	background-color:rgb(9, 28, 43);
	opacity: 0.3;
	filter: drop-shadow(2px 2px 2px #222d33)
}
#Marketop{
	position: absolute;
	width:98.1%;
	height:19.1%;
	right:1%;
	padding: 0%;
	top: 1.7%;
	border:2px #ccc;
	z-index: 10;
	background-color:rgb(9, 28, 43);
	opacity: 0.3;
	filter: drop-shadow(2px 2px 2px #222d33)
}
#Marketbg{
	position: relative;
	width:100%;
	height:100%;
	right:0%;
	padding: 0%;
	top: 0%;
	border:2px #ccc;
	z-index: 10;
	background-color:rgb(9, 28, 43);
	opacity: 0.3;
	filter: drop-shadow(2px 2px 2px #222d33)
}

#containermarket{
	position: absolute;
	width:99%;
	height:98%;
	right:.5%;
	padding: 3%;
	top: 1%;
	border:2px #ccc;
	z-index: 10;
	background-color:rgb(0, 0, 0);
	opacity: 1;
	filter: drop-shadow(2px 2px 2px #222d33)
}

#tradeinv{
	position: absolute;
	width:50%;
	height:80%;
	right:35.5%;
	padding: 0.25%;
	top: 170%;
	border:2px #ccc;
	z-index: 10;
	opacity: 1;
	visibility: hidden;
	filter: drop-shadow(2px 2px 2px #222d33)
}

#Accept{
	top:45%;
	right:35%;
	width:30%;
	font-family: 'Arial Narrow';
	color: #8b8484;
	position: absolute;
	background-color: #000000;
}

#clear{
	top:105%;
	right:35%;
	width:30%;
	height: 14%;
	opacity: 1;
	font-family: 'Arial Narrow';
	font-weight: bold;
	color: #8b8484;
	position: absolute;
	background-color: rgb(12, 80, 38)}


#Accepted{
	top:45%;
	right:35%;
	width:30%;
	font-family: 'Arial Narrow';
	color: #8b8484;
	position: absolute;
	background-color: #000000;
	
}


#inv{
	position: absolute;
	width:50%;
	height:80%;
	right:35.5%;
	padding: 0.25%;
	top: 170%;
	border:2px #ccc;
	z-index: 10;
	opacity: 1;
	visibility: hidden;
	filter: drop-shadow(2px 2px 2px #222d33)
}

#mp{
	position: absolute;
	width:100%;
	padding: 5%;
	height:50%;
	right:0.45%;
	top: 0%;
	border:2px #ccc;
	z-index: 10;
	opacity: 1;
	/*visibility: hidden;*/
	
	filter: drop-shadow(2px 2px 2px #222d33)
}

#op{
	position: absolute;
	width:100%;
	padding: 5%;
	height:50%;
	right:0.45%;
	top: 50%;
	border:2px #ccc;
	z-index: 10;
	opacity: 1;
	/*visibility: hidden;*/
	
	filter: drop-shadow(2px 2px 2px #222d33)
}
#tradeactive{
	position: absolute;
	width:16.5%;
	height:30%;
	right:18.45%;
	top: 171%;
	border:2px #ccc;
	z-index: 10;
	opacity: 0.5;
	visibility: hidden;
	background-color: rgb(25, 25, 25);
	filter: drop-shadow(2px 2px 2px #222d33)
}

#iteminv{
	position: relative;
	width:6%;
	color:rgb(96, 96, 96);
	height:8%;
	margin: 0.5%;
	right:0%;
	top:3%;
	border:2px #ccc;
	text-align: center;
	z-index: 11;
	opacity: 1;
	/*visibility: hidden;*/
	background-color: rgb(32, 32, 32);
	filter: drop-shadow(2px 2px 2px #121111)
}

#tradeinitems{
	position: relative;
	width:100%;
	height:100%;
	right:0.5%;
	top: 0%;
	z-index: 10;
	opacity: 0.5;
	background-color: rgb(23, 23, 23);
	filter: drop-shadow(2px 2px 2px #222d33)
}
#tradername{

	position:absolute;
	width:20%;
	height:17%;
	right: 45%;
	top: 70%;
}
/*
#Tradesactive{
	
	position: absolute;
	width:20.5%;
	height:23%;
	border: 2px solid black;
	right: 73.5%;
	top: 180%;
	z-index: 8;
	opacity: 0.6;
	background-color: rgb(75, 150, 75);
	filter: drop-shadow(2px 2px 2px #222d33)
	/*bright green bar up top with level  consent form and signature send to inventory.
}*/


#accepttrade{
	position: absolute;
	width:20%;
	height:17%;
	border: 2px solid black;
	right: 5%;
	top: 75%;
	z-index: 10;
	opacity: 0.6;
	background-color: rgb(75, 150, 75);
	filter: drop-shadow(2px 2px 2px #222d33)
	/*bright green bar up top with level  consent form and signature send to inventory.*/
}

#genetitled{
	position: absolute;
	width: 100%;
	height: 5%;
	top:190%;
	right: .5%;
	text-align: center;
	opacity: 0.8;
	z-index: 10;
	font-size: small;
	
	font-weight: bold;
	color:rgb(0, 150, 100);
	filter: drop-shadow(2px 2px 2px rgb(0, 0, 0));
	background-color: #030304;
}
#genetitle{
	position: absolute;
	width: 100%;
	height: 5%;
	right: 0%;
	text-align: center;
	opacity: 0.8;
	z-index: 10;
	font-size: small;
	font-weight: 500;
	color:rgb(0, 150, 100);
	filter: drop-shadow(2px 2px 2px rgb(0, 0, 0));
	background-color: #030304;
}
#infodividerer{
	position: absolute;
	width: 40%;
	height: 20%;
	right: 30.25%;
	border: 1px solid rgb(48, 48, 48);
	z-index: 6;
	top:70%;
	opacity: 0.2;
	filter: drop-shadow(2px 2px 2px rgb(0, 0, 0));
	background-color:black;
}
#infodivider{
	position: absolute;
	width: 98%;
	height: 20%;
	right: 1%;
	z-index: 7;
	top:72%;
	color: rgb(0, 180, 100);
	filter: drop-shadow(0px 0px 0px rgb(0, 0, 0));
}
#placeod{
	position: absolute;
	width: 75%;
	height: 20%;
	top:-23%;
	right: 12.5%;
	z-index: 7;
	color: black;
	opacity: 1;
	background-color: #030304;
}
#placedod{
	position: absolute;
	width: 75%;
	height: 20%;
	top:20%;
	right: 12.5%;
	font-family: Arial;
	z-index: 7;
	text-align: center;
	color: green;
	opacity: 1;
}
#accept{
	position: absolute;
	width: 35%;
	height: 35%;
	top:25%;
	right: 60%;
	z-index: 7;
	color: green;
	opacity: 0.6;
	visibility:hidden;
	background-color: #030304;
}
#disclaimer{
	position: absolute;
	width: 100%;
	right:0%;
	text-align: center;
	font-family: Arial;
	top:15%;
	font-size: medium;
}

#Yclose{
	position: absolute;
	width: 5%;
	height: 2.5%;
	top:5%;
	right: 47.5%;
	z-index: 7;
	color: rgb(5, 255, 255);
	text-align: right;
	background-color: #323735;
	opacity: 0.7;
}
#Y{
	position: absolute;
	width: 30%;
	height: 17%;
	top:77%;
	right: 5%;
	z-index: 7;
	color: black;
	text-align: right;
	background-color: #8b8484;
	opacity: 0.9;
}

/*#Y{
	position: absolute;
	width: 30%;
	height: 17%;
	top:78%;
	right: -6%;
	z-index: 7;
	color: black;
	opacity: 1;
}*/
#accepted{
	position: absolute;
	width: 30%;
	height: 17%;
	top:77%;
	right: 5%;
	z-index: 8;
	color: green;
	opacity: 0.6;
}
#ordersplace{
	position: absolute;
	width: 50%;
	right: 20%;
	background-color: transparent;
	color: green;
	
}
#spanish{
	position: absolute;
	width:5%;
	right: 48%;
	top:67%;
	z-index: 7;
	height: 10%;
}
#playerlevel{
	position: absolute;
	top:83.5%;
	right:43.25%;
	color:green;
	z-index: 8;
	filter: drop-shadow(2px 2px 2px rgb(0, 0, 0));
	font-size: 100%;
	text-align: center;
	padding-top: 0%;
}

#playermoney{
	position: absolute;
	top:77.5%;
	right: 53.50%;
	color:green;
	letter-spacing: 0.2px;
	z-index: 8;
	font-size:16px;
	filter: drop-shadow(2px 1px 1px rgb(0, 0, 0));
}

#playerorders{
	position: absolute;
	top:72.5%;
	right:50.5%;
	color:green;
	z-index: 8;
}


#playerluck{
	position: absolute;
	top:71.50%;
	right:31.25%;
	color:green;
	font-size: large;
	z-index: 8;
	filter: drop-shadow(2px 1px 1px rgb(0, 0, 0));
}

#greenlens{
	position: absolute;
	z-index:7;
	top:172%;
	right: 35%;
	width: 30%;
	height: 90%;

}

#winnerl{
	filter: drop-shadow(2px 1px 1px rgb(0, 0, 0));
	color: rgb(0, 200, 120);
	z-index:7;
	font-family: Arial;
	font-size: large;
	text-align: center;
	

}

#Namekk{
	top:-7.5%;
	text-align: center;
	position: relative;
	
}
#power{
	filter: drop-shadow(2px 1px 1px rgb(0, 0, 0));
	color: rgb(0, 200, 120);
	z-index:7;
	font-size: xx-large;
	position: absolute;
	height: 6%;
	top:-6.5%;
	font-family: Arial;
	text-align: center;
	
	right: -5%;
	opacity: 0.1;
	width: 50%;
	background-color: #030304;
	

}


#winnerlw{
	opacity: 0.2;
	position: absolute;
	color: rgb(0, 200, 120);
	height: 105%;
	width: 100%;
	top:0%;
	z-index:1;
	font-size: large;
	background-color: #030304;

}
#butter {
	position: absolute;
	z-index: 7;
	font-size: large;
}

#loverr{
	position: absolute;
	top:40%;
	width:100%;
	height:100%;
	z-index: 7;
}
#box {
	position: inherit;
	right:10%;
	width:100%;
	opacity:1;
	height:100%;
}


#stupid{
	position: absolute;
	width:56%;
	height:63%;
	border: 0px solid gray;
	right: 10%;
	top: 170%;
	z-index: 8;
	opacity: 1;
	visibility:hidden;
	filter: drop-shadow(2px 2px 2px #222d33)
	/*bright green bar up top with level  consent form and signature send to inventory.*/
}

#amountluck{
	position:absolute;
	top:39%;
	border:2px solid gray;
	width:15.5%;
	right:37.5%;
	z-index:10;
	opacity:0.3;
	visibility:hidden;
	text-align:center;
	color:rgb(206, 206, 206);
	background-color:rgb(145, 145, 145);
}

#amountluckbg{
	position:absolute;
	top:0%;
	
}

#buyluck{
	position:absolute;
	top:72%;
	border:2px solid gray;
	width:72.5%;
	right:15%;
	z-index:10;
	opacity:0.5;
	color:rgb(255, 255, 255);
	background-color:rgb(173, 168, 168);
}

#buylucks{
	position:absolute;
	top:47%;
	width:16%;
	color:transparent;
	z-index:11;
	right:37.25%;
	opacity:1;
}

#fortune{
	position:absolute;
	top:10%;
	width:16%;
	height:8%;
	z-index:11;
	right:37.25%;
	opacity:1;
}

#buyluckbg{
	position:absolute;
	top:72%;
	width:72.5%;
	right:15%;
	opacity:0.5;
	z-index:10;
	color:rgb(206, 206, 206);
	background-color:rgb(102, 102, 102);
}


#header {
	position: absolute;
	width: 100%;
	height: 8.5%;
	padding: 10px;
	border: 0px solid gray;
	right: 0px;
	top: 0px;
	z-index: 3;
	background-color: black;
	opacity: 0.35;
	filter: drop-shadow(2px 2px 2px #030304)
	/*bright green bar up top with level  consent form and signature send to inventory.*/
}

#downbelow {
	position: absolute;
	width: 100%;
	height: 35%;
	padding: 10px;
	border: 0px solid gray;
	right: 0px;
	top: 267%;
	z-index: 1;
	opacity: 0.035;
	background-color: rgb(70,160,160);
	/*bright green bar up top with level  consent form and signature send to inventory.*/
}

#full {
	position: absolute;
	width: 100%;
	height: 200%;
	padding: 10px;
	border: 0px solid gray;
	right: 0px;
	top: 0%;
	z-index: 1;
	opacity: 0.05;
	background-color: rgb(0,80,95);
	filter: drop-shadow(2px 2px 2px #222d33)
	/*bright green bar up top with level  consent form and signature send to inventory.*/
}
#playerslist{
	position: absolute;
	top:290.5%;
	right: -10%;
	border:4px solid black;
	font-family: Arial;
	width:115%;
	height: 1250%;
	opacity: 0.8;
	filter: drop-shadow(4px 4px 4px #222d33);
	background-color: #050505;
	z-index:1;

}
#playernav {
	position: absolute;
	width:100%;
	height:100%;
	right:-17.5%;
	top:1%;
	z-index:1;
}
#playersp {
	position: absolute;
	width:92%;
	height:198%;
	right:8%;
}

#playerlistlist{
	position: relative;
	right: -3%;
	width: 120%;
	font-size: small;
	color: rgb(100, 191, 107);
	
	height: 100%;
	opacity: 1;
	font-weight:520;
	filter: drop-shadow(2px 2px 2px #222d33);
	top:0%;
}
#cursor {
	position: absolute;
	width:100%;
	height:100%;
	border: 0px solid gray;
	right: 0%;
	top: 0%;
	z-index: 7;
	opacity: 1;
	filter: drop-shadow(2px 2px 2px #222d33)
	/*bright green bar up top with level  consent form and signature send to inventory.*/
}

#closecurse {
	position: absolute;
	width:7%;
	height:2.5%;
	border: 0px solid gray;
	right: 41.30%;
	top: 91.75%;
	z-index: 7;
	opacity: 1;
	filter: drop-shadow(2px 2px 2px #222d33)
	/*bright green bar up top with level  consent form and signature send to inventory.*/
}

#FLUCK{
	position:absolute;
	top:20%;
	font-family:"Arial Narrow";
	color:rgb(255, 238, 218);
	
}

#FLUCKAM{
	position:absolute;
	right:0%;
	text-align:center;
	width:100%;
	top:20%;
	font-family:"Arial Narrow";
	color:rgb(255, 238, 218);
	
}
#FLtit{
	position:absolute;
	font-weight:600;
	width:100%;
	right:0%;
	text-align:center;
	font-family:"Arial Narrow";
	color:rgb(255, 238, 218);
	
}
#FL{
	position:absolute;
	width:20.5%;
	border:1px solid orange;
	background-color:rgb(223, 93, 0);	
	height:32.5%;
	visibility:hidden;
	right:34.75%;
	top:23.5%;
	z-index:9;
	opacity:0.3;
	
}

#FLCONT{
	position:absolute;
	width:20.5%;
	height:32.5%;
	right:34.75%;
	top:23.5%;
	z-index:9;
	visibility:hidden;
	opacity:1;

	
}

#FLBG{
	position:absolute;
	width:19.5%;
	visibility:hidden;
	background-color:rgb(78, 38, 12);	
	height:31.25%;
	right:35.30%;
	top:24%;
	z-index:10;
	opacity:0.3;

}

#cursorbutton {
	position: absolute;
	width:6.50%;
	height:11.5%;
	border: 0px solid gray;
	right: 41.55%;
	top: 68.75%;
	z-index: 7;
	opacity: 1;
	filter: drop-shadow(2px 2px 2px #222d33)
	/*bright green bar up top with level  consent form and signature send to inventory.*/
}

#bind {
	position: absolute;
	width:100%;
	height:100%;
	right:0%;

}


body {
	overflow-x: hidden;
	/* Hide scrollbars */
}

#backnews {
	position: absolute;
	width: 95%;
	height: 89%;
	border: 1px solid black;
	right: 2.5%;
	top: 5%;
	z-index: 4;
	opacity: 0.6;
	background-color: RGB(12,12,12);
	filter: drop-shadow(4px 2px 2px #222d33)
}

#localewins {
	position: absolute;
	width: 75%;
	height: 85%;
	right: 13%;
	top: 8%;
	z-index: 5;
	visibility:hidden;
	opacity: 0.8;
	background-color: white;
	filter: drop-shadow(2px 2px 3px #222d33)
	/*bright green bar up top with level  consent form and signature send to inventory.*/
}
#wininfo {
	position: absolute;
	width: 28%;
	height: 95%;
	right: 36.7%;
	top: 2.5%;
	z-index: 9;
	opacity: 1;
	background-color: black;
}
#whatelse {
	position: absolute;
	width: 90%;
	height: 75%;
	right: 5%;
	top: 10%;
	z-index: 9;
	opacity: 1;
	background-color: grey;
}
#thewins {
	position: absolute;
	width: 32.5%;
	height: 90%;
	right: 2.5%;
	top: 5%;
	z-index: 9;
	opacity: 1;
	background-color: black;
}

#news {
	position: absolute;
	width: 75%;
	height: 85%;
	right: 13%;
	top: 8%;
	z-index: 5;
	visibility:visible;
	opacity: 0.8;
	background-color: black;
	filter: drop-shadow(2px 2px 3px #222d33)
	/*bright green bar up top with level  consent form and signature send to inventory.*/
}

#opencontent {
	position: absolute;
	width: 95%;
	height: 75%;

	
	
	
	
	
	right: 3%;
	
	top: 9.5%;
	z-index: 5;
	
	
	/*filter: drop-shadow(2px 2px 2px #000000)
	bright green bar up top with level  consent form and signature send to inventory.*/
}
#letter {
	position: absolute;
	width: 100%;

	height: 100%;
	text-align: center;
	right: -14%;
	top: 34%;
	z-index: 4;
	opacity: 1;
	
	color:green;
	filter: drop-shadow(4px 2px 2px #222d33)
	/*bright green bar up top with level  consent form and signature send to inventory.*/
}
#profile {
	position: absolute;
	width: 100%;
	height: 100%;
	right: 0%;
	top: 10%;
	z-index: 4;
	opacity: 1;
	color: green;
	filter: drop-shadow(4px 2px 2px #222d33);
	/*bright green bar up top with level  consent form and signature send to inventory.*/
}

#namer {
	position: absolute;
	width: 100%;
	height: 100%;
	top:-5%;
	right:-7%;
	z-index: 4;
	opacity: 1;
	color: green;
	filter: drop-shadow(4px 2px 2px #222d33);
	font-size:96%
	/*bright green bar up top with level  consent form and signature send to inventory.*/
}


#world {
		position: absolute;
		width: 100%;
		height: 100%;
		right: -18.5%;
		top: 11.5%;
		z-index: 4;
		opacity: 1;
		color: green;
		filter: drop-shadow(4px 2px 2px #222d33);
		font-size:91%;
	}

#money {
	position: absolute;
	width: 100%;
	height: 100%;
	right: -15.5%;
	top: 19.5%;
	z-index: 4;
	opacity: 1;
	color: green;
	filter: drop-shadow(4px 2px 2px #222d33);
	font-size:91%;
}

#level {
	position: absolute;
	width: 100%;
	height: 100%;
	right: -15%;
	top: 28.5%;
	z-index: 4;
	opacity: 1;
	color: green;
	filter: drop-shadow(4px 2px 2px #222d33);
	font-size: 91%
}

#rtp {
	position: absolute;
	width: 100%;
	height: 100%;
	right: -16.5%;
	top: 37.5%;
	z-index: 4;
	opacity: 1;
	color: green;
	filter: drop-shadow(4px 2px 2px #222d33);
	font-size: 91%
}


#contback {
	position: absolute;
	width: 101%;
	height: 102.5%;
	
	right: -.75%;
	top: 0.5%;
	padding:5px;
	z-index: 4;
	opacity: 0.5;
	background-color: black;
	filter: drop-shadow(2px 2px 2px #000000)
	
}

#name {
	position: absolute;
	width: 20%;

	height: 7%;
	border: 0px solid black;
	right: 41%;
	top: 83.5%;
	z-index: 5;
	opacity: 0.3;
	background-color: black;
	filter: drop-shadow(2px 2px 2px #222d33)
	/*bright green bar up top with level  consent form and signature send to inventory.*/
}

#home{
	position:absolute;
	width:10%;
	top:10%;
	right:45%;
	opacity:0.8;
	height:80%;
	font-weight:1000;
	border:1px solid green;
	color: rgb(100, 190, 50);
	background-color:rgb(44, 122, 66);
}

#win{
	position:absolute;
	width:10%;
	top:10%;
	right:56%;
	height:80%;
	opacity:0.8;
	z-index:15;
	font-weight:600;
	border:1px solid green;
	color: rgb(100, 190, 50);
	background-color:rgb(44, 122, 66);
}
#saint{
	position:relative;
	z-index:10;
	color:green;
}
#windoww{
	position:absolute;
	width:2%;
	top:72.4%;
	right:52.8%;
	height:4.5%;
	font-weight:800;
	z-index:90;
	background-color:transparent;
	border:0px;
}
#moneyls{
	position:absolute;
	width:10%;
	top:10%;
	right:34%;
	height:80%;
	font-weight:600;
	opacity:0.8;
	border:1px solid green;
	color: rgb(100, 190, 50);
	background-color:rgb(44, 122, 66);
}
#stats{
	position:absolute;
	width:20%;
	top:10%;
	right:67.5%;
	height:80%;
	font-weight:600;
	opacity:0.6;
	border:1px solid green;
	color: rgb(100, 190, 50);
	background-color:rgb(44, 122, 66);
}

#updates{
	position:absolute;
	width:20%;
	top:10%;
	right:12.5%;
	opacity:0.6;
	height:80%;
	font-weight:600;
	border:1px solid green;
	color: rgb(100, 190, 50);
	background-color:rgb(44, 122, 66);
}

#block{
	position:absolute;
	width:10%;
	top:10%;
	right:1.3%;
	opacity:0.4;
	height:80%;
	font-weight:600;
	color: black;
	background-color:rgb(52, 62, 52);
}

#blocktwo{
	position:absolute;
	width:10%;
	top:10%;
	right:88.7%;
	opacity:0.4;
	height:80%;
	font-weight:600;
	color: black;
	background-color:rgb(52, 62, 52);
}
/*
#seasonload {
	position: absolute;
	width: 95%;
	height: 75%;
	border: 4px solid black;
	right: 2.5%;
	top: 9.5%;
	z-index: 5;
	opacity: 1x;
	background-color: darkslategray;
	filter: drop-shadow(4px 2px 2px #222d33)
	/*bright green bar up top with level  consent form and signature send to inventory.
}
*/
#blowheader {
	position: absolute;
	width: 100%;
	height: 65%;
	padding: 10px;
	border: 0px solid gray;
	opacity: 0.6;
	right: 0%;
	top: 88.5%;
	z-index: 2;
	background-color: black;
	filter: drop-shadow(2px 2px 2px #000000)
}

#firstcontent {
	position: absolute;
	width: 25%;
	height: 55%;
	padding: 10px;
	border: 0px solid gray;
	opacity: 0.5;
	right: 5.75%;
	top: 93.5%;
	z-index: 5;
	background-color: black;
	
}

#secondcontent {
	position: absolute;
	width: 25%;
	height: 55%;
	padding: 10px;
	border: 0px solid gray;
	opacity: 0.5;
	right: 71.25%;
	top: 93.5%;
	z-index: 2;
	background-color: black;
	
}


#content {
	position: absolute;
	width: 35%;
	height: 56%;
	padding: 10px;
	border: 0px solid gray;
	right: 34%;
	top: 93.5%;
	z-index:5;
	
}
#seasontime{
	position: absolute;
	top: 58.5%;
	right: 0%;
}
#roundc{
	position: relative;
	top: -2000.5%;
	right: 450%;
	font-weight: bold;
	z-index: 2;
	color: rgb(100,160,100);
}
#roundtime{
	position: absolute;
	top: 25.5%;
	right: 41%;
	
	z-index: 2;
	color: rgb(100,160,100);
}

#autoround{
	letter-spacing: 42%;
	font-family:'Arial';
	position: absolute;
	font-size: small;
	text-align: center;
	right:82.5%;
	top:100%;

}
#backgroundballwiderthen{
	z-index: 1;
	position: absolute;
	top: -296%;
	height: 265%;
	width: 90%;
	right: 5%;
	opacity: 0.2;
	z-index: 1;
	background-color: rgb(0, 0, 0);
}
#backgroundballwider{
	z-index: 1;
	position: absolute;
	top: -300%;
	height: 269.5%;
	width: 35%;
	right: 33%;
	opacity: 0.3;
	background-color: rgb(0, 80, 20);
}
#backgroundball{
	z-index: 1;
	position: absolute;
	top: -310.5%;
	height: 290%;
	width: 32.5%;
	right: 34.25%;
	opacity: 0.3;
	background-color: rgb(10, 10, 10);
}
#bl{
	position: absolute;
	top: 57.5%;
	height: 9%;
	width: 32.5%;
	opacity: 0.9;
	right: 15.5%;
	z-index: 13;
	font-size: large;
	color: rgb(2, 200, 20);
	font-weight: bolder;
}
#usplit{
	position: absolute;
	top: 40.5%;
	height: 9%;
	width: 22.5%;
	right: 38.50%;
	opacity: 0.9;
	z-index: 13;
	font-size: large;
	color: rgb(2, 200, 20);
	font-weight: bolder;
}

#ssplit{
	position: absolute;
	top: 28.5%;
	height: 9%;
	width: 32.5%;
	opacity: 0.9;
	right: 17.25%;
	z-index: 13;
	font-size: large;
	color: rgb(2, 200, 20);
	font-weight: bolder;
}

#wsplit{
	position: absolute;
	top: 20.5%;
	height: 9%;
	width: 32.5%;
	right: 30.25%;
	opacity: 0.9;
	z-index: 13;
	font-size: large;
	color: rgb(2, 200, 20);
	font-weight: bolder;
}
#dragonball{
	z-index: 6;
	position: absolute;
	top: -300.5%;
	height: 415%;
	width: 30%;
	opacity: 0.5;
	right: 35.5%;
	filter: drop-shadow(1px 1px 1px #222d33);
	
	color: rgb(100,160,100);
}

#backgroundcontent {
	position: absolute;
	width: 96.5%;
	height: 96.5%;
	padding: 10px;
	border: 0px solid gray;
	right: 0;
	top: 0;
	background-color: black;
	opacity: 0.1;
	z-index: 6;
	filter: drop-shadow(2px 2px 2px #222d33)
	
}

#backgroundcontented {
	position: absolute;
	width: 96.5%;
	height: 96.5%;
	padding: 10px;
	border: 3px solid black;
	right: 0;
	top: 0;
	opacity: 0.8;
	z-index: 7;
	
}


#pic {
	position: absolute;
	border: 0px solid gray;
	width: 99%;
	height: 99%;
	right: 0%;
	top:-0.5%;
	background-color: black;
	z-index: 6;
	filter: blur(0.01rem); /* 0.01 no blur 0.1 blur*/
	opacity: 1;
}

#chat {
	position: absolute;
	border: 0px solid gray;
	width: 8%;
	height: 14%;
	right: 91.5%;
	top:251%;
	z-index: 10; 
	opacity: 0.9;
}

#chatup{
	visibility:hidden;
}

#chattwo {
	position: absolute;
	border: 0px solid gray;
	width: 45%;
	height: 102%;
	right: 63.5%;
	top:165%;
	z-index: 6; 
	opacity: 1;
}

#chatul{
	text-wrap: wrap;
	list-style:none;
}
#chatmaterial{
	position: absolute;
	border: 0px solid gray;
	width: 17%;
	height: 46%;
	font-family:'Arial Narrow';
	right: 77.5%;
	top:188%;
	color:rgb(255, 255, 255);
	z-index: 9; 
	text-wrap: wrap;
	text-align:center;
	opacity: 1;
}
#chatpname{
	filter:drop-shadow(2px, 2px, 2px rgb(0,0,0));
	color:rgb(111, 111, 111);
	
}
#chatpcontent{
	text-wrap: wrap;
	font-weight:500;
	font-size:5px;
	filter:drop-shadow(2px, 2px, 2px rgb(0,0,0));
	font-size:large;
	font-family:'Arial';
	color:rgb(23, 85, 23)
	
}
#chatplevel{
	filter:drop-shadow(2px, 2px, 2px rgb(0,0,0));
	font-size:large;
	
	color:rgb(23, 23, 23)
	
}
#chatlist{
	color:rgb(255, 255, 255);
	font-weight:600;
	right:-2%;
	
	position:relative;
	font-family:'Arial Narrow';
	text-align:left;
	opacity:0.9;
	word-wrap: break-word;
}
#chatboxed {
	position: absolute;
	border: 0px solid gray;
	width: 8%;
	height: 4%;
	font-family:'Arial Narrow';
	right: 83.25%;
	top:247%;
	color:rgb(255, 255, 255);
	z-index: 9; 
	text-align:center;
	opacity: 0.3;
	background-color:rgb(8, 8, 8);
}


#lengthchat {
	position: absolute;
	border: 0px solid gray;
	width: 4%;
	height: 8%;
	font-family:'Arial Narrow';
	right: 84%;
	top:252.5%;
	color:rgb(255, 255, 255);
	z-index: 9; 
	text-align:center;
	opacity: 0.3;
	font-size:large;
}


#submitchat {
	position: absolute;
	border: 0px solid gray;
	width: 2%;
	height: 4%;
	font-family:'Arial Narrow';
	right: 80.85%;
	top:247%;
	color:rgb(193, 214, 214);
	z-index: 9; 
	text-align:center;
	opacity: 0.5;
	background-color:rgb(11, 105, 39);
}


#fulldown {
	position: absolute;
	width: 100%;
	height: 108%;
	padding: 10px;
	border: 0px solid gray;
	right: 0px;
	top: 157%;
	z-index: 1;
	opacity: 0.06;
	background-color: rgb(100,255,215);
	filter: drop-shadow(2px 2px 2px #222d33)
	/*bright green bar up top with level  consent form and signature send to inventory.*/
}


#backdrop {
	position: absolute;
	width: 97.5%;
	height: 103%;
	border: 0px solid gray;
	right: 1.9%;
	top: 160.75%;
	z-index: 5;
	opacity: 1;
	filter: drop-shadow(4px 4px 4px #030304);
}

#backid {
	position: absolute;
	z-index: 5;
	opacity: 1;
	padding:10px;
	top:0%;
	right:0%;
	width:100%;
	height:100%;
}

#background {
	position: absolute;
	width: 100%;
	height: 102%;
	padding: 10px;
	border: 0px solid gray;
	right: -.5%;
	top: -2%;
	z-index: 6;
	filter: drop-shadow(0px 4px 4px #222d33);
	background-color: rgb(5, 5, 5);
	opacity: 0.4;
}


#umgbars {
	position: absolute;
	width: 3.5%;
	height: 75%;
	padding: 10px;
	border: 0px solid gray;
	right: 102.35%;
	top: 70.5%;
	background-color: green;
	/*background-color: rgb(55, 189, 100); background-color: rgb(5, 5, 5);*/
	opacity: 1;
	z-index: 5;
	/*filter: drop-shadowwhen come back add season progress bar plus timer.
 add audio disable trades, disable friends, donate button, trading, marketplace.
up top at header, support, profile(bio, profile pic),funds,logout,player data like money and name,home
    create guilds. ranked guilds highest level guild gets cash prize. also daily reward for betting.
    everytime people win for loop make it drag to bottom of screen top. light green text.
    rank by player, rank by guild. season guilds. then reset. invite to guild. create guild. dont tell people what glitches are used for. let them figure it out lol.
    show season guild rankings at the top, news and updates at the top. rules at the top. top season players.
(0px 4px 4px #222d33);*/
}


#forceluck {
	position: absolute;
	width: 10.5%;
	height: 3%;
	padding: 10px;
	border: 0px solid gray;
	right: 12.35%;
	top: 185.5%;
	/*background-color: rgb(200,200,200);*/
	opacity: 1;
	filter: brightness(1.10);
	z-index: 9;
	/*filter: drop-shadow(0px 4px 4px #222d33);*/
}

#players {
	position: absolute;
	width: 12%;
	height: 0.5%;
	padding: 10px;
	border: 0px solid gray;
	right: 5.35%;
	top: 168.5%;
	/*background-color: rgb(200,200,200);*/
	opacity: 0.5;
	filter: brightness(1.10);
	z-index: 7;
	/*filter: drop-shadow(0px 4px 4px #222d33);*/
}

#titled {
	position: absolute;
	width: 15%;
	height: 1%;
	padding: 10px;
	border: 0px solid gray;
	right: 42.50%;
	top: 134.4%;
	background-color: rgb(0,0,0);
	opacity: 0.7;
	filter: brightness(1.10);
	z-index: 9;
	/*filter: drop-shadow(0px 4px 4px #222d33);*/
}

#gene {
	position: relative;
	width: 15%;
	height: 1.5%;
	padding: 10px;
	border: 0px solid gray;
	right: -10%;
	top: -5%;
	opacity: 1;
	filter: brightness(1.10);
	z-index: 9;
	text-align: center;
	color: palegreen;
	filter: brightness(1.5);
}




























		


</style>
