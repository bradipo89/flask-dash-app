import dash

import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px

import pandas as pd


URL_BASE = '/dash/dash_app_2/'
MIN_HEIGHT = 200


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

def init_dashboard(server):
    """Create a Plotly Dash dashboard."""
    dash_app = dash.Dash(
        server=server,url_base_pathname=URL_BASE,
    external_stylesheets=external_stylesheets)


    df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]})

    fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

    dash_app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )])

    return dash_app