import random
import geopandas as gpd
import pandas as pd
import folium
import numpy as np
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

# Buttons
fg = folium.FeatureGroup(name="Markers")
download_points = st.session_state['markers']
for marker in st.session_state["markers"]:
    fg.add_child(marker)

# Create the map and store interaction data inside of session state
map_data = st_folium(
    m,
    center=st.session_state["center"],
    zoom=st.session_state["zoom"],
    feature_group_to_add=fg,
    key="new",
    width=1285,
    height=725,
    returned_objects=["all_drawings"],
    use_container_width=True
)

start_button = st.button('add point')
if map_data.get('all_drawings') is None:
        st.write('Please create a start point')
else:
    point = random_points.create_point(map_data)
    insert_row = {'course_name':st.session_state['course_name'],
                  'shape_name':['S1'], 
                  'geometry':[point],
                  'type':'point'}
    gdf1 = st.session_state['map_data']  
    gdf = pd.concat([gdf1, gpd.GeoDataFrame(insert_row, crs="EPSG:4326")], ignore_index=True)
    st.session_state['map_data'] = gdf
    switch_page('finish_point')
