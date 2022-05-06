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

app.layout = html.Div([
    html.H1('Passport Index',
        style={'textAlign' : 'center'}),
    html.H2('by Sabrina Limage',
        style={'textAlign' : 'center'}),
    html.H4('What is the Passport Index?',
        style={'textAlign' : 'left'}),
    html.H6('The Passport Index is a passport ranking tool used by visitors to explore different passports around the world. Select a country name to get the mobility score.',
        style={'textAlign' : 'left'}),
    dcc.Dropdown(df.Passport, id='pandas-dropdown-1'),
    html.Div(id='pandas-output-container-1'),
    dcc.Dropdown(df.VisaFree, id='pandas-dropdown-1'),
    html.Div(id='pandas-output-container-1'),
    dcc.Graph(figure= fig)
    ])

#app.layout = dash_table.DataTable(df.to_dict('records'), [{"Mobility Score": i, "Visa Required": i} for i in df.columns])

@app.callback(
    Output('pandas-output-container-1', 'Passport'),
    Input('pandas-dropdown-1', 'value')
)
def update_output(value):
    return f'You have selected {value}'


if __name__ == '__main__':
    app.run_server(debug=True)

