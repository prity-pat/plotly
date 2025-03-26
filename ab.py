import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

app = dash.Dash(__name__)

data = {
    'area' : [100, 200, 300, 400, 500],
    'price' : [10, 20, 30, 40, 50]
}

df= pd.DataFrame(data)


app.layout = html.Div([html.H1('My Application'),
   html.H2('Area vs Price Graph'),
   dcc.Dropdown(
       id = 'graph_type',
         options = [
              {'label': 'Scatter Plot', 'value': 'scatter'},
              {'label': 'Line Plot', 'value': 'line'},
                {'label': 'Bar Plot', 'value': 'bar'}
         ],
   ),
   dcc.Graph(id= 'graph')],
   style={'textAlign': 'center', 'color': 'red', 'backgroundColor': 'blue'})

@app.callback(
    Output('graph', 'figure'), 
    [Input('graph_type', 'value')])

def update_graph(graph_type):
    if graph_type == 'scatter':
        fig = px.scatter(df, x='area', y='price')
    elif graph_type == 'line':
        fig = px.line(df, x='area', y='price')
    else:
        fig = px.bar(df, x='area', y='price')

    return fig

app.run(debug= True)
