var locationMarker;
var map;

function initialize() {
    var mapOptions = {
	zoom: 13,
	center: new google.maps.LatLng(40.717587,-74.013375)
    }

    map = new google.maps.Map(document.getElementById('map-canvas'), mapOptions);

    locationMarker = new google.maps.Marker({
	position: mapOptions.center,
	map: map,
	title: 'Selected Location',
	draggable:true
    });
}

google.maps.event.addDomListener(window, 'load', initialize);




// handle events
$(function(){
    $("#locator").submit(function(e){
	e.preventDefault ? e.preventDefault() : e.returnValue = false;
	
//	alert($("#place").val());
	$("#leftStuff").slideUp(2500);
	$("#map-canvas").animate({ height:"100%" },2500,function(){
	    google.maps.event.trigger(map,'resize');
	    $("#map-canvas").animate({ width:"100%" },2500);
	    $("#leftPane").animate({ width:"50%" },2500,function(){
		map.setCenter(new google.maps.LatLng(40.7, -73.9931672372818));
		map.setZoom(11);
		$("#leftPane").css({
		    position:"fixed",
		    top:"0",
		    height:"100%",
		    left:"0"
		});
		$("#leftPane").css("float","left");

		// replace with neighborhoods
		for(var x=1;x<neighborhoods.length;x++){
		    $("#neighborhoods").append('<tr><td class="n_title">'+neighborhoods[x]+'</td><td class="n_driving">10</td><td class="n_transit">15</td><td class="n_citibike">12</td></tr>')
		}

		$("#rightPane").fadeIn("slow");
	    });
	});

	$("#locationGoName").text($("#place").val());
    });
});

   