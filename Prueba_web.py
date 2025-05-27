# Librerías
import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd

# Crear datos de ejemplo
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

# Crear app
app = dash.Dash(__name__)
server = app.server  # <-- Esta línea debe estar aquí, fuera del main

app.layout = html.Div(children=[
    html.H1(children='Primer dashboard prros'),

    html.Div(children='Gráfico interactivo de prueba (a ver qué tal)'),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
