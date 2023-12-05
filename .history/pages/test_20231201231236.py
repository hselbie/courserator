import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import plotly.express as px
import pandas as pd

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Graph(
        id='map',
        config={'scrollZoom': False, 'displayModeBar': False},
        style={'height': '80vh'}
    ),
    html.Button('Add Polygon', id='add-polygon-button'),
])

@app.callback(
    Output('map', 'figure'),
    Input('add-polygon-button', 'n_clicks'),
    prevent_initial_call=True
)
def update_map(n_clicks):
    # Assume you have a DataFrame to store polygon coordinates
    # You can replace this with your data or external data source
    df_polygons = pd.DataFrame(columns=["Polygon"])

    # Create a scatter plot to display the map
    fig = px.scatter_geo(df_polygons, lat=[0], lon=[0], projection="natural earth")

    # Add polygons to the map
    if df_polygons.shape[0] > 0:
        for polygon in df_polygons["Polygon"]:
            fig.add_trace(polygon)

    return fig

@app.callback(
    Output('map', 'config'),
    Input('add-polygon-button', 'n_clicks'),
    State('map', 'config'),
    prevent_initial_call=True
)
def add_polygon(n_clicks, current_config):
    # Get the latest click data
    click_data = dash.callback_context.triggered[0]['prop_id'].split('.')[0]

    # Check if the click event was triggered by the 'Add Polygon' button
    if click_data == 'add-polygon-button':
        # Get the coordinates of the clicked point (assuming a point for simplicity)
        # You can modify this to handle polygon drawing
        # For example, you can use JavaScript to capture mouse clicks and draw a polygon
        # and then send the polygon coordinates to the server
        polygon_coordinates = [[0, 0], [1, 1], [1, 0]]

        # Add the polygon to the DataFrame
        df_polygons = pd.DataFrame({"Polygon": [dict(type='scattergeo', mode='lines', lat=[p[0] for p in polygon_coordinates], lon=[p[1] for p in polygon_coordinates])]})
        
        # Modify the config to enable zooming after adding the polygon
        current_config['scrollZoom'] = True

        return current_config

if __name__ == '__main__':
    app.run_server(debug=True)
