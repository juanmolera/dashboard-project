# Data visualization
import plotly.express as px

# Kepler.gl maps
from streamlit_keplergl import keplergl_static
from keplergl import KeplerGl

# Histogram
def histogram_viz(df, option):

    fig = px.histogram(df, x = df[option])
    fig.update_xaxes(categoryorder = 'total descending')
    fig.update_xaxes(tickangle = 90)

    return fig

# Filtered histogram
def histogram_with_filter_viz(df, option, option2, filter):

    fig = px.histogram(df, x = df[option2][df[option] == filter])
    fig.update_xaxes(categoryorder = 'total descending')
    fig.update_xaxes(tickangle = 90)

    return fig

# Kepler.gl map viz
def kepler_map_viz(df, config):

    map = KeplerGl(height=400, data={'data1': df}, config=config)

    return map