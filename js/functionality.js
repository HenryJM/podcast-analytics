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
		  console.log("Data Data Data");
		})
	} else {
	}
}