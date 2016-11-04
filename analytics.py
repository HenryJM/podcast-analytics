import time
import plotlywrapper as pyw
import feedparser

DAYS_IN_SECONDS = 3600 * 24

def pull_and_clean_data(rss_source):
	parseresult = feedparser.parse(rss_source)
	sorted_data = sorted([(time.mktime(entry.published_parsed), 
						   entry.title, entry.itunes_duration)
					  for entry in parseresult.entries], key= lambda x : x[0])
	publish_delay = [(sorted_data[i+1][0] - sorted_data[i][0]) / DAYS_IN_SECONDS
					for i in range(len(sorted_data) - 1)]
	titles = [entry[1] for entry in sorted_data]
	duration_minutes = [utils.itunes_duration_to_minutes(entry[2]) 
						 for entry in sorted_data]
	return sorted_data, publish_delay, titles, duration_minutes

	
def make_plots(rss_source, chart_names):
	sorted_data, publish_delay, titles, duration_minutes \
	= pull_and_clean_data(rss_source)
	
	charts = dict()
	
	if 'releaseDelay' in chart_names:
		charts['releaseDelay'] = pyw.line_plot_sma(publish_delay, titles, 
		'Delay', 'Release Delay', 'Release Ordinal', 'Days Since Last Release', 
		[5,10])
		
	return charts