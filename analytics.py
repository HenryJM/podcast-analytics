import time
import feedparser
import logging
import utils
import chartmaker

DAYS_IN_SECONDS = 3600 * 24

BASIC_DATA_VARIABLES = ["title", "link", "updated", "authors"]

def pull_and_clean_data(rss_source):
    parseresult = feedparser.parse(rss_source)
    basic_data = {field: parseresult.feed[field] for field in BASIC_DATA_VARIABLES}
    logging.info(basic_data)
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
    
    chart_maker = chartmaker.ChartMaker(
    sorted_data, publish_delay, titles, duration_minutes)
    
    charts = chart_maker.make_charts(chart_names)
        
    return charts