import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go

app = dash.Dash()

# parse data file into dataframe structure
df = pd.read_csv(r'./data/data.csv', sep='\t')


def build_query_string(smape_data, iterations=[]):
    selected_iterations = smape_data.iter_id.unique().tolist() if (len(iterations) <= 0 or iterations is None) else iterations
    return f'iter_id in {selected_iterations}'


def filter_data(smape_data, iterations=[]):
    iteration_data = smape_data.query(build_query_string(smape_data, iterations))
    filtered_data = iteration_data.proof_vector.unique()

    return [
        go.Scatter(
                x=iteration_data[iteration_data['proof_vector'] == i]['iter_id'],
                y=iteration_data[iteration_data['proof_vector'] == i]['proof_smape'],
                mode='markers',
                opacity=0.7,
                marker={
                    'size': 15,
                    'line': {'width': 0.5, 'color': 'white'}
                },
                name=i
            ) for i in filtered_data
    ]


app.layout = html.Div([
    dcc.Dropdown(
        id='drpdwn',
        multi=True,
        options=[{'value': i, 'label': i} for i in df.iter_id.unique().tolist()],
        placeholder="Select an iteration...",
        value=[i for i in df.iter_id.unique()]
    ),
    dcc.Graph(
        id='smape',
        animate=True,
        figure={
            'data': filter_data(df),
            'layout': go.Layout(
                xaxis={'type': 'log', 'title': 'proof vector'},
                yaxis={'title': 'MAPE'},
                margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                legend={'x': 0, 'y': -1},
                hovermode='closest'
            )
        }
    )
])


@app.callback(Output('smape', 'figure'),
              [Input('drpdwn', 'value')])
def update_smape_graph(selected_iterations):
    return {
        'data': filter_data(df, selected_iterations),
        'layout': go.Layout(
            xaxis={'type': 'log', 'title': 'proof vector'},
            yaxis={'title': 'MAPE'},
            margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
            legend={'x': 0, 'y': -1},
            hovermode='closest'
        )
    }


# Dash CSS
app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})
# Loading screen CSS
app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/brPBPO.css"})


if __name__ == '__main__':
    app.run_server()