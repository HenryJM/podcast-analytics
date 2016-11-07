function resizePlots(){
	$.each($(".plotly-graph-div"), function(index, value){
		Plotly.Plots.resize(value);
	});
}

function setValidation(validationStatus){
	if(validationStatus){
		console.log("hide invalid URL");
		$("#invalidURL").hide();
		$("#rssUrl").removeClass("form-control-error");
		$("#rssFormGroup").removeClass("has-error");
	} else {
		$("#invalidURL").show();
		$("#rssUrl").addClass("form-control-error");
		$("#rssFormGroup").addClass("has-error");
	}
}

function validateRssUrl(url){
	var result = re_weburl.test(url);
	setValidation(result);
	return result;
}

function loadPlots(){
	var rssUrl = $("#rssurl").val();
	
	$("#infoDisplay").hide();
	
	if(validateRssUrl(rssUrl)){
		$("#loadingDisplay").show();
		
		$.get( "/plot", {
			rssUrl: encodeURIComponent(rssUrl),
			charts: CHARTS_TO_PLOT} 
		).done(function( data ) {
			data = jQuery.parseJSON(data);

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
			
			window.onresize = resizePlots;
		})
	} else {
	}
}