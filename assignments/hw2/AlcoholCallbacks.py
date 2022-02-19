import plotly.express as px
from dash import Output, Input
from dashboards.app import app, alcohol_df
    
@app.callback(
    Output(component_id='alcohol_graph', component_property='figure'),
    Input('countries','value')
)
def update_alcohol_graph(countries):
    """ Update the list of countries being displayed in the eCDF chart

    Args:
        countries (list): contains the list of countries selected

    Returns:
        plotly.graph_objs._figure.Figure: eCDF alcohol consumption figure containing the selected countries
    """
    filtered_df = alcohol_df[alcohol_df['location'].isin(countries)]
    return px.ecdf(filtered_df, x='location', y='alcohol', title='Alcohol consumption by country', 
            template='plotly')