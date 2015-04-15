(function(window){
	console.log("home.js Succesfully loaded in browser");

	$(document).ready(function(){
		//var usrObj={'username':'Steffanb','password':'pass','email':'email@domain.com'}
		//attachUser(usrObj)
		getUsers();
		setup();
	});
	function setup(){
		console.log('setting up')
		$('#addUsrBtn').click(function(){
			console.log('click')
			getInput()
		})
	}
	function getUsers(){
		$.ajax({
				url: "https://steff-bood-sw-eng.herokuapp.com/getmanagers", 
				success: function(response){
							var users = JSON.parse(response)
							console.log( users)
							console.log([1,2,3,4])
							users.forEach(function(curr){
								attachUser(curr)
							})
    					}
    		});
		//_get('http://localhost:5000/getmanagers',null,null,null);

	}
	function attachUser(usrObj){
		var usrDiv = $("<div/>",{class:'list-group list-group-horizontal'})
		$("<div/>",{class:'list-group-item'}).append("<b>Username</b>: "+usrObj.username).appendTo(usrDiv)
		$("<div/>",{class:'list-group-item'}).append("<b>Password</b>: "+usrObj.password).appendTo(usrDiv)
		$("<div/>",{class:'list-group-item'}).append("<b>Email</b>: "+usrObj.email).appendTo(usrDiv)
		$('#userlist_Cont').append(usrDiv).hide().fadeIn(1000)
	}

	function getInput(){
		var username = $('#username').val();
		var password = $('#password').val();
		var email = $('#email_address').val();

		var user = {
			"username" : username,
			"password"	: password,
			"email" : email
		};
		if(user===""||password===""||email===""){
			console.log('returned')
			return;
		}

		console.log(user);
		var usrJson = JSON.stringify(user);
		// clearing the input fields
		$('#username').val('');
		$('#password').val('');
		$('#email_address').val('');

		$.ajax({
				data:usrJson,
				type:'post',
				url: "https://steff-bood-sw-eng.herokuapp.com/newmanager", 
				success: function(response){
							attachUser(user);
							console.log(response)
    					}
    		});
	}

	

}(this));