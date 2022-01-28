# Import libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app

# 1 column layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Tableau
            View our Tableau Dashboard here: https://public.tableau.com/views/chicago_crime_story_2/ChicagoCrimeDashboard?:language=en-US&publish=yes&:display_count=n&:origin=viz_share_link
            """
        ),

    ],
)

layout = dbc.Row([column1])