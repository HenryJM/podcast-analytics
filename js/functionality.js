GLOBAL_DATA = 4;

function validateRssUrl(url){
	return true;
}

function loadPlots(){
	var CHARTS_TO_PLOT = ["releaseDelay"];
	var rssUrl = encodeURIComponent($('#rssurl').val());
	
	if(validateRssUrl(rssUrl)){
		console.log(rssUrl);
		$.get( "/plot", {
			rssUrl: encodeURIComponent(rssUrl),
			charts: CHARTS_TO_PLOT} 
		).done(function( data ) {
			GLOBAL_DATA = data;
			console.log(data);
			console.log(data.json());
			data = jQuery.parseJSON(data);
			console.log(data['releaseDelay']);
			$("#releaseDelay > .chart").html(data.releaseDelay);
			$("#releaseDelay").show();
		})
	} else {
	}
}