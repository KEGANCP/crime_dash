import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import flask 

# Imports from this application
from app import app, server
from pages import index, predictions, GitHub, tableau

# Navbar 
navbar = dbc.NavbarSimple(
    brand='Predicting Crime in Chicago',
    brand_href='/', 
    children=[
        dbc.NavItem(dcc.Link('Predictions', href='/predictions', className='nav-link')), 
        dbc.NavItem(dcc.Link('GitHub', href='/GitHub', className='nav-link')), 
        dbc.NavItem(dcc.Link('Tableau', href='/tableau', className='nav-link'))
    ],
    sticky='top',
    color='dark', 
    light=False, 
    dark=True
)

footer = dbc.Container(
    dbc.Row(
        dbc.Col(
            html.P(
                [
                    html.Span('Crime Prediction Team', className='mr-2'), 
                    html.Span('Kegan Propster', className='mr-1), 
                    html.Span('Sean Farr', className='mr-1), 
                    html.Span('Austen Marden', className='mr-1)                ], 
                className='lead'
            )
        )
    )
)


# Layout 
app.layout = html.Div([
    dcc.Location(id='url', refresh=False), 
    navbar, 
    dbc.Container(id='page-content', className='mt-4'), 
    html.Hr(),
    footer
])


# URL Routing
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
        return index.layout
    elif pathname == '/predictions':
        return predictions.layout
    elif pathname == '/GitHub':
        return GitHub.layout
    elif pathname == '/tableau':
        return tableau.layout       
    else:
        return dcc.Markdown('## Page not found')

# Run app server
if __name__ == '__main__':
    app.run_server(debug=True)


