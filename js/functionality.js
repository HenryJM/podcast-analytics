function validateRssUrl(url){
	return true;
}

function loadPlots(){
	var CHARTS_TO_PLOT = ["releaseDelay"];
	var rssUrl = encodeURIComponent($('#rssurl').val());
	
	$("#loadingDisplay").show();
	
	if(validateRssUrl(rssUrl)){
		console.log(rssUrl);
		$.get( "/plot", {
			rssUrl: encodeURIComponent(rssUrl),
			charts: CHARTS_TO_PLOT} 
		).done(function( data ) {
			data = jQuery.parseJSON(data);
			$("#loadingDisplay").hide();
			$("#infoDisplay").show();
			
			$.each(CHARTS_TO_PLOT, function(key, value){
				$el = $("#" + value);
				$el.show();
				$el.children(".chart").html(data[value]);
			});
		})
	} else {
	}
}