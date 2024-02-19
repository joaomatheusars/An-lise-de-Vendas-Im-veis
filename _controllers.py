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

slider_size = [100, 500, 1000, 10000, 1000000]

controlers = dbc.Row([
    html.Img(id="logo", src=app.get_asset_url(
        "logo_dark.png"), style={"widht": "50%"}),
    html.H3("Vendas de imóveis - NYC", style={"margin-top": "30px"}),
    html.P("""Utilize este dashboard para analisar vendas ocorridas na cidade de New york no período de 1 ano."""),
    html.H4("Distrito", style={"margin-top": "50px", "margin-bottom": "25px"}),
    dcc.Dropdown(
        id="location-dropdown",
        options=[{"label": i, "value": j}
                 for i, j in list_of_locations.items()],
        value=0,
        placeholder="Selecione um distrito",
    ),
    html.H4("Metragem (m2)", style={
            "margin-top": "20px", "margin-bottom": "20px"}),
    dcc.Slider(min=0, max=4, id="slider-square-size",
               marks={i: str(j) for i, j in enumerate(slider_size)}),
    html.H4("Variável de controle", style={
            "margin-top": "20px", "margin-bottom": "20px"}),
    dcc.Dropdown(
        options=[
            {'label': 'Year Built', 'value': 'Year Built'},
            {'label': 'Total Units', 'value': 'Total Units'},
            {'label': 'Sale Price', 'value': 'Sale Price'},
        ],
        value='Sale Price',
        id='dropdown-color'
    )
])
