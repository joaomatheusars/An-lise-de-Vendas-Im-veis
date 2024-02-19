from dash import html, ddc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

from app import app

app.layout = dbc.Container(children=[], fluid=True)

if __name__ == "__main__":
    app.run(debug=True)
