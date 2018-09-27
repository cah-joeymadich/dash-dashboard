# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

# Dash CSS
app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})
# Bootstrap CSS
# app.css.append_css({"external_url": "https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css"})
# app.css.append_css({"external_url": "https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css"})
# Loading screen CSS
app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/brPBPO.css"})

app.layout = html.H1('On Dasher!')

if __name__ == '__main__':
    app.run_server(debug=True)