$(document).ready(function() {
    $('#registrationForm').on('submit', function(event) {
        event.preventDefault();
        
        $.ajax({
            type: 'POST',
            url: '/register',
            data: $(this).serialize(),
            success: function(response) {
                alert('Registration successful!');
            },
            error: function(error) {
                alert('An error occurred. Please try again.');
            }
        });
    });
});
