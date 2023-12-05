import folium
import geopandas as gpd
import streamlit as st
from streamlit_folium import st_folium
import initialize_map
import random_points
from streamlit_extras.switch_page_button import switch_page 


st.set_page_config(
    page_title="st_folium Example",
    page_icon="🔎",
    layout="wide"
)
# Set up initial map state
CENTER_START = [37.8, -96]
ZOOM_START = 5

initialize_map.initialize_session_state(CENTER_START, ZOOM_START)

m = initialize_map.initialize_map(
    center=st.session_state["center"], zoom=st.session_state["zoom"])

data = st.session_state['map_data']

polygon = data.loc[data['shape_name'] == 'course_shape']
points = data.loc[data['type']=='point']

# Buttons
polygon_fg = folium.FeatureGroup(name="Game Area")
sim_geo = polygon.simplify(tolerance=0.001)
# sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
geo_j = sim_geo.to_json()
# geo_j = folium.GeoJson(data=geo_j, style_function=lambda x: {"fillColor": "orange"})
# geo_j.add_to(polygon_fg)
# polygon.add_to(polygon_fg)
folium.GeoJson(polygon).add_to(polygon_fg)

# folium.Popup(r["BoroName"]).add_to(geo_j)
m.add_child(polygon_fg)


# Create the map and store interaction data inside of session state
map_data = st_folium(m
    # m,
    # center=st.session_state["center"],
    # zoom=st.session_state["zoom"],
    # feature_group_to_add=fg,
    # key="new",
    # width=1285,
    # height=725,
    # returned_objects=["all_drawings"],
    # use_container_width=True
)

data = st.session_state['map_data']

polygon = data.loc[data['shape_name'] == 'course_shape']
points = data.loc[data['type']=='point']

fg_polygon = folium.FeatureGroup(name='Game Area')
for polygon in polygon.geometry:
    fg_polygon.add_child(folium.Polygon(polygon))