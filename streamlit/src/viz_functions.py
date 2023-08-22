# Data visualization
import plotly.express as px

# Kepler.gl maps
from streamlit_keplergl import keplergl_static
from keplergl import KeplerGl

# Kepler.gl map viz
def kepler_map_viz(city, df, geojson, config):
    '''
    Creates Kepler map
    '''

    map = KeplerGl(height=400, data={f'airbnb_{city}': df}, config=config);
    map.add_data(data=geojson, name=f'neighbourhood_{city}');

    return map

# Histogram
def histogram_viz(df, option):
    '''
    Creates histogram representation for the chosen city's districts
    '''

    fig = px.histogram(df, x = df[option])
    fig.update_xaxes(categoryorder = 'total descending')
    fig.update_xaxes(tickangle = 270)

    return fig

# Filtered histogram
def histogram_with_filter_viz(df, option, option2, filter):
    '''
    Creates histogram representation for the chosen district's neighbourhoods
    '''

    fig = px.histogram(df, x = df[option2][df[option] == filter], labels={'x': 'Neighbourhood'})
    fig.update_xaxes(categoryorder = 'total descending')
    fig.update_xaxes(tickangle = 270)

    return fig