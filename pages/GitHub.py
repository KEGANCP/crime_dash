# Import libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app

app.layout = html.Div([
    html.Div(id='target'),
    dcc.Dropdown(
        id='dropdown',
        options=[
            {'label': 'Video 1', 'value': 'video1'},
            {'label': 'Video 2', 'value': 'video2'},
            {'label': 'Video 3', 'value': 'video3'},
        ],
        value='video1'
    )
])


@app.callback(Output('target', 'children'), [Input('dropdown', 'value')])
def embed_iframe(value):
    videos = {
        'video1': 'sea2K4AuPOk',
        'video2': '5BAthiN0htc',
        'video3': 'e4ti2fCpXMI',
    }
    return html.Iframe(src=f'https://www.youtube.com/embed/{videos[value]}')
