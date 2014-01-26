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
		for(var x=0;x<neighborhoods.length;x++){
		    $("#neighborhoods").append('<tr id="neigh'+x+'"><td class="n_title">'+neighborhoods[x]+'</td><td class="n_driving" id="neigh'+x+'_driving">..</td><td class="n_transit">..</td><td class="n_citibike">..</td></tr>')

		    $.getJSON("/info?start="+$("#place").val()+"&end="+neighborhoods[x]+"&id=neigh"+x,function(d){
			$("#"+d.id+" .n_driving").text(d.driving_time);
			$("#"+d.id+" .n_transit").text(d.transit_time);
		    });

		}

		$("#rightPane").fadeIn("slow");
	    });
	});

	$("#locationGoName").text($("#place").val());
    });
});


   