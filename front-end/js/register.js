$(document).ready(function() {
    // Handle form submission
    $('#register-form').submit(function(event) {
        event.preventDefault(); // Prevent the form from submitting normally

        // Get the form data
        var formData = {
            name: $('#name').val(),
            email: $('#email').val(),
            password: $('#password').val()
        };

        // Send an AJAX request to the /register endpoint
        $.ajax({
            type: 'POST',
            url: 'http://127.0.0.1:9090/register',
            data: JSON.stringify(formData),
            contentType: 'application/json',
            success: function(response) {
                alert("Registered!! yes!")
                // Handle the success response
                console.log(response);
                // You can perform any desired actions here
            },
            error: function(error) {
                // Handle the error response
                console.error(error);
                // You can display an error message or perform any desired actions here
            }
        });
    });
});
