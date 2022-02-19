import plotly.express as px
from dash import Output, Input
from dashboards.app import app, school_df

@app.callback(
    Output(component_id='school_graph', component_property='figure'),
    Input('schools','value')
)
def update_school_graph(schools):
    """ Whenever the checklist for the schools selected is changed, this callback is called and update the bar chart
        to display only the data from the selected schools.

    Args:
        schools (list): list of schools selected

    Returns:
        plotly.graph_objs._figure.Figure: A barchart object containing earnings data for the selected schools
    """
    filtered_df = school_df[school_df['School'].isin(schools)]
    return px.bar(filtered_df, x='School', y='Earning', color='Gender', title='School Earnings by Gender',
                    template='plotly', labels={'Earning': 'Earning (Thousand Dollars)'})