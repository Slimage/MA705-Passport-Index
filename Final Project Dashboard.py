"""
Dashboard 
"""

import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
#from dash import Dash, dash_table
import plotly.express as px
import pandas as pd

df = pd.read_csv(r"C:\Users\nubia\OneDrive\Documents\MSBA Courses\MA705.HB1.SP22.Cherveny.Data Science\Final Project\passport-index-matrix - cleaned.csv",encoding='utf-8')

stylesheet = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

### pandas dataframe to html table
def generate_table(dataframe, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])

app = dash.Dash(__name__, external_stylesheets=stylesheet)

server = app.server

fig = px.bar(df, x="Passport", y= "Mobility Score", color="Passport")

app.layout = html.Div(children=[
    html.H1(children='Passport Index Dashboard',
        style={'textAlign' : 'center'}),
    html.H2(children='by Sabrina Limage',
        style={'textAlign' : 'center'}),
    html.H4(children='What is the Passport Index?',
        style={'textAlign' : 'left'}),
    html.H6(children='The Passport Index is a passport ranking tool used by global travelers to explore different passports around the world. \
            It is the only real-time global ranking of the world’s passports, updated as frequently as new visa waivers and changes are implemented.\
            This dashboard was inspired by the original Passport Index created by Arton Capital.\
            Select a country name to get the mobility score.',
        style={'textAlign' : 'left'}),
   dcc.Dropdown(df.Passport, id='pandas-dropdown-1'),
   html.Div(id='pandas-output-container-1'),
   #dcc.Dropdown(df.VisaFree, id='pandas-dropdown-1'),
   #html.Div(id='pandas-output-container-1'),
   dcc.Graph(figure= fig)
   ])

@app.callback(
    Output('pandas-output-container-1', 'Passport'),
    Input('pandas-dropdown-1', 'value')
) 



def update_output(value):
    return f'You have selected {value}'


if __name__ == '__main__':
    app.run_server(debug=True)

