# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash(__name__)

# Dash CSS
# app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})
# Bootstrap CSS
# app.css.append_css({"external_url": "https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css"})
app.css.append_css({"external_url": "https://bootswatch.com/4/darkly/bootstrap.min.css"})
# Loading screen CSS
app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/brPBPO.css"})

colors = {
    'background': '#222222',
    'text': '#FFFFFF'
}

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='On Dasher!',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.Div(children='Dash: A web application framework for Python.', style={
        'textAlign': 'center',
        'color': colors['text']
    }),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization',
                'plot_bgcolor': colors['background'],
                'paper_bgcolor': colors['background'],
                'font': {
                    'color': colors['text']
                }
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)