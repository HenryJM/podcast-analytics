import plotly as py
import plotly.graph_objs as go
import utils

def line_plot_sma(inputs, labs, valname, title, xlab, ylab, sma_sizes):
    ordinal = range(1,len(inputs)+1)
    data = [go.Scatter(x=ordinal,
                       y=inputs,
                       text=labs,
                       mode = 'lines+markers',
                       name = valname)]
    
    for size in sma_sizes:
        data.append(go.Scatter(x=ordinal[size-1:],
                       y=utils.sma(inputs, size),
                       mode = 'lines',
                       name = 'SMA-'+str(size)))                       

    layout = go.Layout(title=title,
                       xaxis=dict(title = xlab),
                       yaxis=dict(title = ylab))
                       
    return py.offline.plot({
        "data": data,
        "layout": layout,
        },
        output_type = "div",
        include_plotlyjs=False,
        show_link = False
    )

    
def histogram(inputs, title, binsize):
    data = [go.Histogram(x=inputs,
                xbins=dict(
                    start=min(inputs), 
                    size=binsize, 
                    end=max(inputs)
                )
            )]
    
    return py.offline.plot({
        "data": data,
        "layout" : go.Layout(title=title)
        },
        output_type = "div",
        include_plotlyjs=False,
        show_link = False
    )