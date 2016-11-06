import time
import feedparser
import logging
import utils
import chartmaker

DAYS_IN_SECONDS = 3600 * 24

TITLE_DATA_VARIABLES = ['title', 'subtitle', 'link']
BASIC_DATA_VARIABLES = ['updated', 'author', 'published']

def pull_and_clean_data(rss_source):
    parseresult = feedparser.parse(rss_source)

    # Title Data
    title_data = {field: parseresult.feed[field] for field in TITLE_DATA_VARIABLES if field in parseresult.feed.keys()}

    # Basic Data
    basic_stats = {field: parseresult.feed[field] for field in BASIC_DATA_VARIABLES if field in parseresult.feed.keys()}

    sorted_data = sorted([(time.mktime(entry.published_parsed), 
                           entry.title, entry.itunes_duration)
                      for entry in parseresult.entries], key= lambda x : x[0])
    publish_delay = [(sorted_data[i+1][0] - sorted_data[i][0]) / DAYS_IN_SECONDS
                    for i in range(len(sorted_data) - 1)]
    titles = [entry[1] for entry in sorted_data]
    duration_minutes = [utils.itunes_duration_to_minutes(entry[2]) 
                         for entry in sorted_data]
    return title_data, basic_stats, sorted_data, publish_delay, titles, duration_minutes

    
def make_plots(rss_source, chart_names):
    title_data, basic_stats, sorted_data, publish_delay, titles, duration_minutes \
    = pull_and_clean_data(rss_source)
    
    chart_maker = chartmaker.ChartMaker(
    basic_stats, sorted_data, publish_delay, titles, duration_minutes)
    
    charts = chart_maker.make_charts(chart_names)
    charts['titleData'] = title_data
        
    return charts