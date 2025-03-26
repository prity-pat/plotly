import dash
from dash import html, dcc
from dash.dependencies import Input,Output
import plotly.express as px 
import pandas as pd

app = dash.Dash(__name__)

data = {
    'area':[100,200,300,400,500,600,700,800,900,950,1000],
    'cost':[98,150,200,250,300,350,400,450,500,550,600]
}

df = pd.DataFrame(data)

app.layout = html.Div([html.H1('hello'),
html.H2('area vs cost Graph'),
dcc.Dropdown(
    id = 'graph_type',
    options = [
        {'label': 'line plot', 'value' : 'line'},
        {'label': 'Scatter Plot', 'value' : 'scatter'},
        {'label': 'Bar plot', 'value': 'bar'}
    ]
),
dcc.Graph(id = 'graph')], 
style ={'textAlign': 'center', 'color' :'blue','background': 'lightblue'})

@app.callback(
        Output('graph', 'figure'),
        [Input('graph_type', ' value')]
)


def update_graph(graph_type):
    if graph_type == 'line':
        fig = px.line(df, x='area', y = 'cost')
    elif graph_type == 'scatter':
        fig = px.scatter(df , x = 'area', y = 'cost')
    else:
        fig = px.bar(df, x = 'area' , y = 'cost')
    return fig            

app.run(debug=True)
