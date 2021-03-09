import dash
import matplotlib
import dash_core_components as dcc
import dash_html_components as html
import dash_table
from .data import create_dataframe

import numpy as np
import pandas as pd

URL_BASE = '/dash/dash_app_1/'
MIN_HEIGHT = 200


def init_dashboard(server):
    """Create a Plotly Dash dashboard."""
    dash_app = dash.Dash(
        server=server,url_base_pathname=URL_BASE,
    )
    df = create_dataframe()
    dash_app.layout = html.Div(
        children=[
            dcc.Graph(
                id="histogram-graph",
                figure={
                    "data": [
                        {
                            "x": df["complaint_type"],
                            "text": df["complaint_type"],
                            "customdata": df["key"],
                            "name": "311 Calls by region.",
                            "type": "histogram",
                        }
                    ],
                    "layout": {
                        "title": "NYC 311 Calls category.",
                        "height": 500,
                        "padding": 150,
                    },
                },
            ),
            create_data_table(df),
        ],
        id="dash-container",
    )

    return dash_app





def create_data_table(df):
    """Create Dash datatable from Pandas DataFrame."""
    table = dash_table.DataTable(
        id="database-table",
        columns=[{"name": i, "id": i} for i in df.columns],
        data=df.to_dict("records"),
        sort_action="native",
        sort_mode="native",
        page_size=300,
    )
    return table
