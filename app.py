import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

pd.core.common.is_list_like = pd.api.types.is_list_like
from pandas.api.types import is_list_like
import pandas_datareader
from pandas_datareader import data as web
import plotly.graph_objs as go
import numpy as np

from datetime import datetime as dt

app = dash.Dash('Compare Score')
app.config.supress_callback_exceptions = True

df = pd.read_csv(r'./data.csv', sep='\t')


def traceList(df):
    trace1 = go.Scatter(x=list(df.iter_id.unique()),
                        y=[df[df.proof_vector == 'Gender'].proof_smape.tolist()[-1]],
                        marker={"color": "blue", "size": 10},
                        mode="lines+markers",
                        name="Gender"
                        )
    trace2 = go.Scatter(x=list(df.iter_id.unique()),
                        y=[df[df.proof_vector == 'Age Bin'].proof_smape.tolist()[-1]],
                        marker={"color": "yellow", "size": 10},
                        mode="lines+markers",
                        name="Age Bin"
                        )
    trace3 = go.Scatter(x=list(df.iter_id.unique()),
                        y=[df[df.proof_vector == 'Race'].proof_smape.tolist()[-1]],
                        marker={"color": "red", "size": 10},
                        mode="lines+markers",
                        name="Race"
                        )
    trace4 = go.Scatter(x=list(df.iter_id.unique()),
                        y=[df[df.proof_vector == 'Zip Code'].proof_smape.tolist()[-1]],
                        marker={"color": "green", "size": 10},
                        mode="lines+markers",
                        name="Location"
                        )
    trace5 = go.Scatter(x=list(df.iter_id.unique()),
                        y=[df[df.proof_vector == 'Condition'].proof_smape.tolist()[-1]],
                        marker={"color": "grey", "size": 10},
                        mode="lines+markers",
                        name="Condition"
                        )
    trace6 = go.Scatter(x=list(df.iter_id.unique()),
                        y=[df[df.proof_vector == 'Medication'].proof_smape.tolist()[-1]],
                        marker={"color": "orange", "size": 10},
                        mode="lines+markers",
                        name="Medication"
                        )
    trace7 = go.Scatter(x=list(df.iter_id.unique()),
                        y=[df[df.proof_vector == 'Condition length'].proof_smape.tolist()[-1]],
                        marker={"color": "cyan", "size": 10},
                        mode="lines+markers",
                        name="Condition length"
                        )
    data = [trace1, trace2, trace3, trace4, trace5, trace6, trace7]
    return data


data = traceList(df)

app.layout = html.Div([
    html.Label('select iteration number'),
    dcc.Dropdown(
        id='drpdwn',
        # value = np.asarray([i for i in df.iter_id.unique()]),
        # options=[
        #   {'label': 'Iteration1', 'value': 'i1'},
        multi=True,
        options=[{'value': i, 'label': i} for i in df.iter_id.unique().tolist()],
        # placeholder="Select an iteration"
        value=[i for i in df.iter_id.unique()]
    ),
    dcc.Graph(
        id='smape',
        animate=True,
        figure={
            'data': data,
            'layout': go.Layout(
                xaxis={'type': 'log', 'title': 'proof vector'},
                yaxis={'title': 'MAPE'},
                margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                legend={'x': 0, 'y': 1},
                hovermode='closest'
            )
        }
    )
])


@app.callback(Output('smape', 'figure'),
              [Input('drpdwn', 'value')])
def smapeGraph(inp):
    print("inp", inp)
    # dff = df[df['iter_id'] ]
    graphs = []
    for itera in inp:
        dff = df[df['iter_id'] == itera]
        print(itera)
        # print("dff", dff)
        data1 = traceList(dff)
        print(data1)

        graphs.append(dcc.Graph(
            id='smape',
            animate=True,
            figure={
                'data': data1,
                'layout': go.Layout(
                    xaxis={'type': 'log', 'title': 'proof vector'},
                    yaxis={'title': 'MAPE'},
                    margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                    legend={'x': 0, 'y': 1},
                    hovermode='closest'

                )}))

    return graphs


# Dash CSS
app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})

# Loading screen CSS
app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/brPBPO.css"})
if __name__ == '__main__':
    app.run_server(port=8089, host='0.0.0.0', debug=False)
