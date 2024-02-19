from dash import html, dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
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

if __name__ == "__main__":
    app.run(debug=True)
