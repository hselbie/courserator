import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State
import plotly.express as px
import geopandas as gpd
from shapely.geometry import Polygon, Point
import random

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
    # Assume you have a GeoDataFrame to store polygons
    # You can replace this with your data or external data source
    gdf_polygons = gpd.GeoDataFrame(geometry=[])

    # Create a scatter plot to display the map
    fig = px.scatter_geo(gdf_polygons, projection="natural earth")

    # Add polygons to the map
    if gdf_polygons.shape[0] > 0:
        for polygon in gdf_polygons["geometry"]:
            x, y = polygon.exterior.xy
            fig.add_trace(px.line_geo(lat=y, lon=x).data[0])

    return fig

@app.callback(
    Output('map', 'figure'),
    Input('add-polygon-button', 'n_clicks'),
    prevent_initial_call=True
)
def add_polygon(n_clicks):
    # Generate a random polygon for simplicity
    min_lat, max_lat = random.uniform(-90, 90), random.uniform(-90, 90)
    min_lon, max_lon = random.uniform(-180, 180), random.uniform(-180, 180)
    polygon = Polygon([(min_lon, min_lat), (min_lon, max_lat), (max_lon, max_lat), (max_lon, min_lat)])

    # Add the polygon to the GeoDataFrame
    gdf_polygons = gpd.GeoDataFrame(geometry=[polygon])

    # Generate random points within the polygon
    num_points = 10
    points_within_polygon = []
    while len(points_within_polygon) < num_point
