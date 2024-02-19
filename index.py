from dash import html, dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
from app import app
from _map import *
from _histogram import *
from _controllers import *

# -------------------
# Data ingestion
# -------------------

df_data = pd.read_csv('data/cleaned_data.csv', index_col=0)
mean_lat = df_data["LATITUDE"].mean()
mean_long = df_data["LONGITUDE"].mean()

df_data["size_m2"] = df_data["GROSS SQUARE FEET"] / 10.764
df_data = df_data[df_data["YEAR BUILT"] > 0]
df_data["SALE DATE"] = pd.to_datetime(df_data["SALE DATE"])

df_data.loc[df_data["size_m2"] > 10000, "size_m2"] = 10000
df_data.loc[df_data["SALE PRICE"] > 50000000, "SALE PRICE"] = 50000000
df_data.loc[df_data["SALE PRICE"] < 1000000, "SALE PRICE"] = 100000

# -------------------
# Layout
# -------------------
app.layout = dbc.Container(
    children=[
        dbc.Row([
            dbc.Col([controlers], md=3),
            dbc.Col([map, hist], md=9),
        ])
    ],
    fluid=True
)

# -------------------
# Callbacks
# -------------------


@app.callback([Output('hist-graph', 'figure')],
              [Input('location-dropdown', 'value'),
               Input('slider-square-size', 'value'),
               Input('dropdown-color', 'value')])
def update_hist(location, square_size, color_map):
    if location is None:
        df_intermediate = df_data.copy()
    else:
        df_intermediate = df_data[df_data["BOROUGH"] ==
                                  location] if location != 0 else df_data.copy()
        size_limit = slider_size[square_size] if square_size is not None else df_data["GROSS SQUARE FEET"].max(
        )
        df_intermediate = df_intermediate[df_intermediate["GROSS SQUARE FEET"] <= size_limit]

    hist_fig = px.histogram(df_intermediate, x=color_map, opacity=0.75)
    hist_layout = go.Layout(
        margin=go.layout.Margin(l=10, r=0, t=0, b=5),
        showlegend=False,
        template="plotly_dark",
        paper_bgcolor="rgba(0, 0, 0, 0)"
    )

    hist_fig.layout = hist_layout
    return hist_fig


if __name__ == "__main__":
    app.run(debug=True)
