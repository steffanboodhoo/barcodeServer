(function(window){
	console.log("home.js Succesfully loaded in browser");

	$(document).ready(function(){
		//var usrObj={'username':'Steffanb','password':'pass','email':'email@domain.com'}
		//attachUser(usrObj)
		getUsers()
	});
	function getUsers(){
		_get('https://steff-bood-sw-eng.herokuapp.com/getmanagers',null,function(data){
			console.log(data)
		});
	}
	function attachUser(usrObj){
		var usrDiv = $("<div/>",{class:'list-group list-group-horizontal'})
		$("<div/>",{class:'list-group-item'}).append("<b>Username</b>: "+usrObj.username).appendTo(usrDiv)
		$("<div/>",{class:'list-group-item'}).append("<b>Password</b>: "+usrObj.password).appendTo(usrDiv)
		$("<div/>",{class:'list-group-item'}).append("<b>Email</b>: "+usrObj.email).appendTo(usrDiv)
		$('#userlist_Cont').append(usrDiv).hide().fadeIn(2000)
	}

	function _post (loc, param, success_callback, error_callback){    

      $.ajax({
        type    :   'post',
        url     :   loc,
        data    :   param,
        success :   function(response){
          if (typeof success_callback === 'function')
            success_callback(response);
        },
        error :   function(response){
          if (typeof error_callback === 'function')
            error_callback(response);
          else
            console.log(response.responseText);
        }
      });
    }

    function _get(loc, success_callback,error_callback){          

      $.ajax({
        type  :   'get',
        url   :   loc,        
        success :   function(response){
          if (typeof success_callback === 'function'){
            success_callback(response);
          }
        },
        error :   function(response){
          if (typeof error_callback === 'function'){
            error_callback(response);
          }else{
            console.log(response);
          }
        }
      });
    }

}(this));