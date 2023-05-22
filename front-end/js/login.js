$(document).ready(function() {
	$('#login-form').submit(function(event) {
	  event.preventDefault();
  
	  // Get form values
	  var email = $('#email').val();
	  var password = $('#password').val();
  
	  // Create login request object
	  var loginRequest = {
		email: email,
		password: password
	  };
  
	  // Send login request
	  $.ajax({
		url: 'http://127.0.0.1:9090/login',
		type: 'POST',
		data: JSON.stringify(loginRequest),
		contentType: 'application/json',
		success: function(response) {
			if(response.message ==="Logged in successfully"){
				 window.location.href = 'jitsi-meet.html';
		  		console.log(response);
			}
			else{
				alert("Incorrect email or password, kindly recheck")
			}
		},
		error: function(xhr, status, error) {
		  // Handle login error
		  console.error(xhr.responseText);
		}
	  });
	});
  });



