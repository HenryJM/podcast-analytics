import plotlywrapper as pyw
import idnamemethod

class ChartMaker:

    def __init__(self, sorted_data, publish_delay, titles, duration_minutes):
        self.sorted_data = sorted_data
        self.publish_delay = publish_delay
        self.titles = titles
        self.duration_minutes = duration_minutes
        
    def release_delay_chart(self):
        return pyw.line_plot_sma(self.publish_delay, self.titles, 
        'Delay', 'Release Delay', 'Release Ordinal', 'Days Since Last Release', 
        [5,10])
        
    def duration_chart(self):
        return pyw.line_plot_sma(self.duration_minutes, self.titles, 
		'Duration', 'Duration', 'Release Ordinal', 'Duration (Minutes)', [5,10])
        
    def make_charts(self, chart_names):
        charts = dict()
        for name in chart_names:
            if name in idnamemethod.NAME_TO_METHOD:
                charts[name] = getattr(self, idnamemethod.NAME_TO_METHOD[name][0])()
        return charts