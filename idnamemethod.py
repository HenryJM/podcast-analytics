NAMES = ['basicStats', 'releaseDelay', 'duration']

NAME_TO_METHOD = {
	'basicStats' : ('basic_stats_table', "Basic Stats"),
    'releaseDelay' : ('release_delay_chart', "Release Delay"),
    'duration' : ('duration_chart', "Duration")
}

EXAMPLE_PODCASTS = [
	("Hello Internet", "http://www.hellointernet.fm/podcast?format=rss"),
	("Cortex", "https://www.relay.fm/cortex/feed"),
	("Market Foolery", "http://marketfoolery.themotleyfool.libsynpro.com/rss"),
	("Serial", "http://feeds.serialpodcast.org/serialpodcast")
]