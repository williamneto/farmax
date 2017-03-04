var geocoder;
var map;

function geocodeAddress(geocoder, address) {
	geocoder.geocode({'address': address}, searchPharmacy);
}

function initMap() {
	var map = new google.maps.Map(document.getElementById('map'), {
		center: {lat:  -22.9068467, lng: -43.1728965},
		zoom: 10
	});
	geocoder = new google.maps.Geocoder();
  
	var infowindow = new google.maps.InfoWindow();
}
 
function searchPharmacy(results, status) {
	if (status === google.maps.GeocoderStatus.OK) {
		var service = new google.maps.places.PlacesService(map);
		
		alert(results[0].geometry.lat)
		
		service.nearbySearch({
			location: results[0].geometry.location,
			radius: 500,
			types: ['pharmacy']
		}, callback);	
    } else {
		alert('Geocode was not successful for the following reason: ' + status);
    }
}

function callback(results, status) {
	if (status === google.maps.places.PlacesServiceStatus.OK) {
		for (var i = 0; i < results.length; i++) {
			createMarker(results[i]);
		}
	}else{
		alert("ruim:")
	}
}

function createMarker(place) {
	var placeLoc = place.geometry.location;
	alert(placeLoc);
	var marker = new google.maps.Marker({
		map: map,
		position: place.geometry.location
	});
}


$(document).ready(function(){
	
	$("#search-next").click(function(){
		$("#search-first").hide();
		$("#search-second").show();
	});
	$("#search-prev").click(function(){
		$("#search-second").hide();
		$("#search-first").show();
	});
	
	$("#id_med").change(function(){
		var text = $("#id_med").val();
		$.ajax({
			url: ".",
			type: "GET",
			data: { "cmd": "search_autocomplete", "text": text },
			success: function(data){
				for ( i = 0; i < data.length; i++){
					var html = "<li class='med_sugest'>" + data[i] + "</li>"
					$("#med_autocomplete").html(html);
				}
			}
		});
	});
	
	$('#med_autocomplete').on('click', 'li', function() {
		$("#id_med").val($(this).text());
	});
	
	$("#search-form").submit(function(){
		// Geocode to get the location
		var cidade = $("#id_cidade").val();
		var bairro = "," + $("#id_bairro").val();
		var query = cidade + bairro;
		
		geocodeAddress(geocoder, query);
		
		return false;
	});
})
