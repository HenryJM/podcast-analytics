function validateRssUrl(url){
	return true;
}

function loadPlots(){
	var rssUrl = encodeURIComponent($('#rssurl').val());
	
	$("#infoDisplay").hide();
	$("#loadingDisplay").show();
	
	if(validateRssUrl(rssUrl)){
		console.log(rssUrl);
		$.get( "/plot", {
			rssUrl: encodeURIComponent(rssUrl),
			charts: CHARTS_TO_PLOT} 
		).done(function( data ) {
			data = jQuery.parseJSON(data);
			console.log(data);
			$("#loadingDisplay").hide();
			$("#infoDisplay").show();
			
			// Modify Title
			if(data.titleData != undefined){
				console.log(data.titleData);
				if(data.titleData.title != undefined) $("#podcastTitle").text(data.titleData.title);
				if(data.titleData.link != undefined) $("#podcastTitle").attr("href", data.titleData.link);
				if(data.titleData.subtitle != undefined) $("#podcastSubtitle").text(data.titleData.subtitle);
			}

			// Display Charts
			$.each(CHARTS_TO_PLOT, function(key, value){
				$el = $("#" + value);
				$el.show();
				$el.children(".chart").html(data[value]);
			});
		})
	} else {
	}
}