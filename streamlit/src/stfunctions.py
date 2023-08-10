import plotly.express as px

# Histogram
def histogram_viz(df, option):

    fig = px.histogram(df, x = df[option])
    fig.update_xaxes(categoryorder = 'total descending')
    fig.update_xaxes(tickangle = 90)

    return fig

# Filtered histogram
def histogram_viz_with_filter(df, option, option2, filter):

    fig = px.histogram(df, x = df[option2][df[option] == filter])
    fig.update_xaxes(categoryorder = 'total descending')
    fig.update_xaxes(tickangle = 90)

    return fig