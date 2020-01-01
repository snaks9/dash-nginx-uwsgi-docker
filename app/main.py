import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.figure_factory as ff

import flask

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = flask.Flask(__name__)
dash_app = dash.Dash(__name__, server=app, external_stylesheets=external_stylesheets)

dash_app.scripts.config.serve_locally=True

df = [dict(Task="Rig 1", Start='2009-01-01', Finish='2009-02-28', State='Running'),
      dict(Task="Rig 2", Start='2009-03-05', Finish='2009-04-15', State='Running'),
      dict(Task="Rig 2", Start='2009-04-15', Finish='2009-04-17', State='Waiting'),
      dict(Task="Rig 2", Start='2009-04-17', Finish='2009-04-29', State='Running'),
      dict(Task="Rig 2", Start='2009-04-29', Finish='2009-05-05', State='Idle'),
      dict(Task="Rig 3", Start='2009-02-20', Finish='2009-05-30', State='Running')]

colours = {'Running': 'rgb(  0,128,  0)',
           'Waiting': 'rgb(255,165,  0)',
           'Idle'   : 'rgb(128,128,128)'}

fig_g = ff.create_gantt(df, group_tasks=True, index_col='State', colors=colours)

dash_app.layout = html.Div(children=[
    html.H1(children='Hello User, plotly examples'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    ),

    dcc.Graph(figure=fig_g, id='gantt')

])

if __name__ == '__main__':
    print('About to run app')
    dash_app.run_server(host='0.0.0.0', debug=True, port=80)
