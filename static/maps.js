var locationMarker;
var map;
var polylines = [];
var drawnPolylines = [];
var markers = [];


function initialize() {
    geocoder = new google.maps.Geocoder();
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

	locationMarker.setMap(null);
	geocoder.geocode( { 'address': $("#place").val()+", New York"}, function(results, status) {
	    if (status == google.maps.GeocoderStatus.OK) {
		map.setCenter(results[0].geometry.location);
		var marker = new google.maps.Marker({
		    map: map,
		    position: results[0].geometry.location
		});
	    }
	});

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
		$("#rightPane").fadeIn("slow");
	    });

	});

	// replace with neighborhoods
	for(var x=0;x<neighborhoods.length;x++){
	    $("#neighborhoods").append('<tr id="neigh'+x+'"><td class="n_title">'+neighborhoods[x]+'</td><td class="n_driving" id="neigh'+x+'_driving">..</td><td class="n_transit">..</td></tr>')

	    $.getJSON("/info?start="+$("#place").val()+"&end="+neighborhoods[x]+"&id="+x,function(d){
		$("#neigh"+d.id+" .n_driving").text(d.driving_time);
		$("#neigh"+d.id+" .n_transit").text(d.transit_time);
		setMarker(d.marker,d.id*1,d.driving_time,d.transit_time);
		polylines[d.id] = [d.driving_polyline,d.transit_polyline];
	    });

	}





	$("#locationGoName").text($("#place").val());
    });
});


function setMarker(a,b,drive,transit){
    var c = new google.maps.Marker({
	num:b,
	position: new google.maps.LatLng(a[0],a[1]),
	map: map,
	title: neighborhoods[b]+" [Drive: "+drive+" | Transit: "+transit+"]",
	driving:drive,
	transit:transit,
	icon:"http://chart.apis.google.com/chart?chst=d_map_pin_letter&chld="+transit+"|"+gradient(transit)+"|FFFFFF"
    });
    markers.push(c);
    google.maps.event.addListener(c,"mouseover",function(){
	clearPolylines();
	for(var x=0;x<2;x++){
	    var p = new google.maps.Polyline({
		path:google.maps.geometry.encoding.decodePath(polylines[this.num][x]),
		geodesic: true,
		strokeColor: x==0?"#FE2E2E":"#2E2EFE",
		strokeOpacity: 1.0,
		strokeWeight: x==0?2:6
	    });
	    p.setMap(map);
	    drawnPolylines.push(p);
	}
    });
    google.maps.event.addListener(c,"mouseout",function(){
	clearPolylines();
    });
}

function clearPolylines(){
    for(var x=0;x<drawnPolylines.length;x++){
	drawnPolylines[x].setMap(null);
    }
}

function gradient(a){
    return rgbToHex(Math.min(255,a*4),Math.max(0,255-a*4),0).replace("#","")
}


/* rgbToHex source: http://stackoverflow.com/questions/5623838/rgb-to-hex-and-hex-to-rgb */
function rgbToHex(r, g, b) {
    return "#" + ((1 << 24) + (r << 16) + (g << 8) + b).toString(16).slice(1);
}