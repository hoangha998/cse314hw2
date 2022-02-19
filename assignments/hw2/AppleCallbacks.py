import plotly.express as px
from dash import Output, Input
from dashboards.app import app, apple_df

@app.callback(
    Output('apple_graph', component_property='figure'),
    Input('date_range','start_date'),
    Input('date_range','end_date')
)
def update_date_range(start_date,end_date):
    """ Update stock line chart to display data from start_date to end_date

    Args:
        start_date (str): start date in YYYY-MM-DD format
        end_date (str): end date in YYYY-MM-DD format

    Returns:
        plotly.graph_objs._figure.Figure: Line chart displaying Apple stock data in selected range
    """
    filtered_df = apple_df.loc[start_date:end_date]
    return px.line(filtered_df, x=filtered_df.index, y='AAPL_y', title='Apple Stock Price in 2014',
            template='plotly_dark', labels={'AAPL_x': 'dates', 'AAPL_y': 'dollars'})


# chain callback to inform whether stock price went up or down in this interval
# output of "update_change_in_stock_price" callback is the input of "update_stock_direction" callback
@app.callback(
    Output('change_in_price', 'children'),
    Input('date_range','start_date'),
    Input('date_range','end_date')
)
def update_change_in_stock_price(start_date,end_date):
    """ Display the change in Apple stock price from start_date to end_date

    Args:
        start_date (str): start date in YYYY-MM-DD format
        end_date (str): end date in YYYY-MM-DD format

    Returns:
        str: A sentence informing the change in stock price 
    """
    change = apple_df.loc[end_date]['AAPL_y'] - apple_df.loc[start_date]['AAPL_y']
    text = 'Stock price chance in this interval = %.2f dollars' % (change)
    return text


@app.callback(
    Output('stock_direction', 'children'),
    Input('change_in_price','children')
)
def update_stock_direction(text):
    """ Utilize chained callback so that whenever the date range is changed and the callback 
    update_change_in_stock_price is called, this callback would use the output from that callback
    and inform whether the Apple stock price in the selected range went up or down.

    Args:
        text (str): A sentence informing the change in stock price 

    Returns:
        str: A sentence informing whether Apple stock price went up or down in the selected range
    """
    change = float(text.split(' ')[-2])
    if change < 0:
        return "Stock price went DOWN in this interval"
    return "Stock price went UP in this interval"