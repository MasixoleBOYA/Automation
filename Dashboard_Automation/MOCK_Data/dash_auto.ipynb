import pandas as pd
import plotly.express as px
import dash
from dash import html
from dash import dcc

# Sample data
data = {
    'depot': ['Alrode', 'Alrode', 'Alrode', 'Watloo', 'Watloo', 'IVT', 'Natref'],
    'customer': ['Ab Fuels', 'ef fuels', 'cd fuels', 'Ab Fuels', 'ef fuels', 'cd fuels', 'ef fuels'],
    'D50': [2000000, 0, 340000, 0, 130000, 0, 4000000],
    'ULP93': [0, 0, 450000, 0, 0, 0, 0],
    'ULP95': [60000, 0, 0, 0, 0, 0, 199000]
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
    melted_df = pd.melt(filtered_df, id_vars=['depot', 'customer'], var_name='fuel_type', value_name='sales')

    fig = px.bar(melted_df, x='customer', y='sales', color='fuel_type', barmode='group',
                 labels={'sales': 'Sales Amount', 'customer': 'Customer', 'fuel_type': 'Fuel Type'},
                 title=f'Sales by Customer for {selected_depot}')

    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
