from dash import html, dcc
import dash_bootstrap_components as dbc
from app import app

list_of_locations = {
    "All": 0,
    "Manhattan": 1,
    "Bronx": 2,
    "Brooklyn": 3,
    "Queens": 4,
    "Staten Islands": 5,
}

slider_list = [100, 500, 1000, 10000, 1000000]

controlers = dbc.Row([
    html.Img(id="logo", src=app.get_asset_url(
        "logo_dark.png"), style={"widht": "50%"})
])
