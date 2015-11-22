//Showing fields when drop down

$('#user-role').on('click', function() {
	switch ($('#user-role').val()) {
  case 'volunteer':
    $('#donator-form').hide();
    $('#collector-form').hide();
    $('#volunteer-form').fadeIn();
    $('#submit-form').fadeIn();
    break;
  case 'donator':
    $('#collector-form').hide();
    $('#volunteer-form').hide();
    $('#donator-form').fadeIn();
    $('#submit-form').fadeIn();
    break;
  case 'collector':
    $('#donator-form').hide();
    $('#volunteer-form').hide();
    $('#collector-form').fadeIn();
    $('#submit-form').fadeIn();
    break;
  default:
    $('#donator-form').hide();
    $('#collector-form').hide();
    $('#volunteer-form').hide();
    $('#submit-form').hide();
    break;
}
}); 

//Creating User

$('#submit-form').on('click', function() {
	var street = $('#street-address').val();
	var city = $('#city').val();
	var state = $('#state').val();
	var zipcode = $('#zipcode').val();
	var phoneNumber = $('#phone-number').val();
	var compnayName = $('#company-name').val();

	var createAddress = $.ajax({
		url: '/api/location/create',
		type: 'POST',
		data: { street_address: street, 
						   city: city,
						   state: state,
						   zip_code: zipcode,
				},
		dataType: 'html'
	});

	createAddress.done(function(address) {
		var userName = $('#user-name').val();
		var password = $('#password').val();
		var firstName = $('#first-name').val();
		var lastName = $('#last-name').val();
		var userRole = $('#user-role').val();

		var createUser = $.ajax({
			url: '/api/user/create',
			type: 'POST',
			data: { location_id: address.id,
							   username: userName,
							   password: password,
							   first_name: firstName,
							   last_name: lastName,
							   role: userRole
					},
			dataType: 'html'
		});
	});

	createAddress.fail(function(data) {
			console.log(data);
	});
});

$(':radio').change(
  function(){
    $('.choice').text( $(this).val() + ' stars' );
  }
)

// same hights
var height = $('#how-we-doit').height();
$('.cust-container').height(height);
