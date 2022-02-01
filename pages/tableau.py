# Import libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
# import base64

# Imports from this application
from app import app

# image_filename = 'tab.png' 
# tab = base64.b64encode(open(image_filename, 'rb').read())

# 1 column layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Tableau
            View the below link to view our interactive dashboard via Tableau. These visualizations will provide a good source of our analysis between the correlation between weather and crime in chicago. 
            """
        ),

    ],
)

column2 = dbc.Container(
    dbc.Row(
        dbc.Col(
            html.P(
                [
                    html.Span('Chicago Crime & Weather Visualizations', className='mr-2'), 
                    html.A(html.Button('VIEW!', className='three columns'),
                        href='https://public.tableau.com/views/chicago_crime_story_2/ChicagoCrimeDashboard?:language=en-US&publish=yes&:display_count=n&:origin=viz_share_link')
                ], 
                className='lead'
               
            )
        )
    )
)

# column3 = dbc.Container(
#     dbc.Row(
#         dbc.Col(
#             html.P(
#                 [
#                     html.Span('Chicago Crime & Weather Visualizations', className='mr-2'), 
#                     html.Iframe(src="https://public.tableau.com/app/profile/austen.marden/viz/chicago_crime_story_2/ChicagoCrimeDashboard?publish=yes",
#                                 style={"height": "1067px", "width": "100%"})
#                 ], 
#                 className='lead'
               
#             )
#         )
#     )
# )

# column3 = dbc.Container(
#     dbc.Row(
#         dbc.Col(
#             html.P(
#                 [
#                     html.Span('Chicago Crime & Weather Visualizations', className='mr-2'), 
#                     def b64_image(image_filename):
#                          with open(image_filename, 'rb') as f:
#                             image = f.read()
#                         return 'data:image/png;base64,' + base64.b64encode(image).decode('utf-8'))
#                 ], 
#                 className='lead'
               
#             )
#         )
#     )
# )

layout = dbc.Row([column1, column2]) 
