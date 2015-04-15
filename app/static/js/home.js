(function(window){
	console.log("home.js Succesfully loaded in browser");

	$(document).ready(function(){
		//var usrObj={'username':'Steffanb','password':'pass','email':'email@domain.com'}
		//attachUser(usrObj)
		getUsers()
	});
	function getUsers(){
		$.ajax({
				url: "http://localhost:5000/getmanagers", 
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

	

}(this));