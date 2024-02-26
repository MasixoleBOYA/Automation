import pandas as pd
import plotly.express as px
import dash
from dash import html
from dash import dcc

# Sample data
data = {
    'depot': ['ALRODE', 'E10 Petrolium', 'ELEGANT FUEL', 'GLOBAL OIL', 'CAPE TOWN', 'ELEGANT FUEL', 'GULFSTREAM', 'IVT', 'OKSANA FUELS', 'GULFSTREAM', 'Natref', 'OPEVIA', 'ELEGANT FUEL'],
    'customer': ['ALRODE', 'E10 Petrolium', 'ELEGANT FUEL', 'GLOBAL OIL', 'CAPE TOWN', 'ELEGANT FUEL', 'GULFSTREAM', 'IVT', 'OKSANA FUELS', 'GULFSTREAM', 'Natref', 'OPEVIA', 'ELEGANT FUEL'],
    'D50': [2834312, 38287, 0, 53489, 1004146, 330549, 673597, 150, 30, 20, 200, 40, 25],
    'ULP93': [0, 0, 0, 0, 0, 0, 0, 25, 5, 7, 10, 5, 8],
    'ULP95': [778986, 0, 42797, 111286, 690017, 463860, 226157, 75, 15, 10, 150, 20, 30],
}

df = pd.DataFrame(data)

# Create the Dash app
app = dash.Dash(__name__)

# Define the layout of the dashboard
app.layout = html.Div([
    html.H1('Sales Dashboard'),

    html.Div([
        html.Label('Select Depot:'),
        dcc.Dropdown(
            id='depot-dropdown',
            options=[{'label': depot, 'value': depot} for depot in df['depot'].unique()],
            value=df['depot'].unique()[0]
        )
    ]),

    html.Div([
        dcc.Graph(id='sales-graph')
    ])
])

# Define callback to update the graph based on the selected depot
@app.callback(
    dash.dependencies.Output('sales-graph', 'figure'),
    [dash.dependencies.Input('depot-dropdown', 'value')]
)
def update_graph(selected_depot):
    filtered_df = df[df['depot'] == selected_depot]
    melted_df = pd.melt(filtered_df, id_vars=['customer'], var_name='fuel_type', value_name='sales')

    fig = px.bar(melted_df, x='customer', y='sales', color='fuel_type', barmode='group',
                 labels={'sales': 'Sales Amount', 'customer': 'Customer', 'fuel_type': 'Fuel Type'},
                 title=f'Sales by Customer for {selected_depot}')

    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
