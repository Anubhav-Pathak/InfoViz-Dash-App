from dash import Dash, html, dcc, Input, Output, callback
from figure import fig1, fig3, fig5, inst, get_inst

app = Dash(__name__)
server = app.server

app.layout = html.Div(children=[
    html.H1(children='''Data Visualization Project''', style={'text-align': 'center', 'margin-bottom': '2rem'}),

    html.Section(children=[
        html.H2(children='''No. of Publications per Institution'''),
        html.P(children='''This is a pie chart showing the number of publications for top institution.'''),
        dcc.Graph(
            id='example-graph',
            figure=fig1
        ),
    ]),
    
    html.Section(children=[
        html.H2(children='Start, First and Last Authored Publications'),
        html.P(children='''This plot shows the number of publications for each author rank for the top 50 authors.'''),
        dcc.Graph(id='example-graph-3',figure=fig3),
    ], style={'padding': '2rem 0'}),

    html.Section(children = [
        html.Div(children=[
            html.H2(children='Institutions Radar Plot'),
            html.P(children='''This plot shows the average number of publications, citations, h-index, rank and number of first authored publications for the selected institutions.'''),
            html.Label('Add Institution names'),
            dcc.Dropdown(inst, id='inst', multi=True),
        ]),
        dcc.Graph(id='example-graph-4'),
    ], 
    style={'padding': '0 20px', 'display': 'flex', 'align-items': 'center', 'justify-content': 'center'}),

    html.Section(children=[
        html.Img(src=app.get_asset_url('output10.png')),
        html.Div(children=[
            html.H2(children='Wordmap'),
            html.P(children='''This plot shows the most frequent words in the abstracts of the publications.'''),
        ],
        style={'margin-left': '2rem'}),
        ], 
    style={'display': 'flex', 'align-items': 'center', 'justify-content': 'center', 'padding': '2rem 0'}),

    html.Section(children=[ 
        html.H2(children='''Chloropleth Map'''),
        html.P(children='''This is a heatmap showing the number of publications for each country.'''),
        dcc.Graph(id='example-graph-5',figure=fig5),
    ]),

], style={'padding': '0 4rem'})

@callback(
    Output('example-graph-4', 'figure'),
    Input('inst', 'value'))
def update_output_div(input_value):
    return get_inst(input_value)

if __name__ == '__main__':
    app.run(debug=True)
