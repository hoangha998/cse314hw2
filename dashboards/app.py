# Run this app with `python dashboards/app.py` and
# visit http://127.0.0.1:8050/ in your web browser.
# open a new terminal window (Ctrl+Shift+` in VS Code.)

from dash import Dash, html, dcc, Output, Input
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd

# Creating app
app = Dash(__name__, external_stylesheets=[dbc.themes.MORPH]) # bootstrap theme added

# loading alcohol data
alcohol_df = pd.read_csv('../data/2010_alcohol_consumption_by_country.csv')

# loading apple data
apple_df = pd.read_csv('../data/2014_apple_stock.csv')
apple_df = apple_df.set_index('AAPL_x')
dates = apple_df.index
min_date, max_date = dates[0], dates[-1]


# loading school earnings data
origin_school_df = pd.read_csv('../data/school_earnings.csv')
school_df = []
for row_idx in range(origin_school_df.shape[0]):   # reformat data for bar chart
    school, male_earning, female_earning = origin_school_df.iloc[row_idx].values[:3]
    school_df.append([school, male_earning, 'Male'])
    school_df.append([school, female_earning, 'Female'])
school_df = pd.DataFrame(school_df, columns=['School', 'Earning', 'Gender'])



# main layout
app.layout = html.Div(
    [
        html.H1("Data Manipulation HW2", style={'text-align':'center', 'padding':'10px'}),
        dcc.Tabs(id="tabs-example-graph", children=[

            dcc.Tab(label='Alcohol Consumption', children=[
                dcc.Graph(id='alcohol_graph'),
                dcc.Checklist(alcohol_df['location'].unique(), ['China', 'Germany', 'United States'], id='countries',
                    style={'width':'80%', 'margin':'20px auto 20px auto', 'display':'flex',
                        'justify-content':'space-evenly', 'flex-wrap':'wrap'},
                    labelStyle={'color': 'black', 'width':'120px'}
                )
            ]),

            dcc.Tab(label='Apple Stock', children=[
                dcc.Graph(id='apple_graph'),
                dcc.DatePickerRange(
                    id='date_range',
                    min_date_allowed=min_date,
                    max_date_allowed=max_date,
                    start_date = min_date,
                    end_date = max_date,
                    style={'display': 'block', 'text-align':'center', 'margin-top':'20px'},
                ),
                html.H3(id='change_in_price', style={'display': 'block', 'text-align':'center'}),
                html.H3(id='stock_direction', style={'display': 'block', 'text-align':'center'}),
            ]),

            dcc.Tab(label='School Earnings', children=[
                dcc.Graph(id='school_graph', style={'width':'80%', 'margin':'auto'}),
                dcc.Checklist(school_df['School'].unique(), ['MIT', 'Stanford', 'Harvard'], id='schools',
                    style={'width':'50%', 'margin':'20px auto 20px auto', 'display':'flex',
                        'flex-wrap':'wrap'},
                    labelStyle={'color': 'black', 'width':'120px'}
                )
            ])

        ])
    ]
)

# Retrieve callbacks 
from assignments.hw2.AlcoholCallbacks import *
from assignments.hw2.AppleCallbacks import *
from assignments.hw2.SchoolCallbacks import *


if __name__ == "__main__":
    app.run_server(debug=True)
