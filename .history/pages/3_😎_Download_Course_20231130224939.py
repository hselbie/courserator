import random
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

if download_points: 
    x = random_points.create_polygon(location_data=st.session_state['map_data'])
    random_points.create_groundoverlay_kmz(
        poly=x, 
        overlay_name='hugo_overlay')
    pts_kml = random_points.download_pts_kml(
        start_points=['36.9658,', '-122.024'],
        points=st.session_state['dl_points'],
        location_id='hugo1'
    )
    with open('output/hugo.kml') as f:
        st.download_button('Download points KML', f, file_name='hugo1.kml')
else:
    st.write('please save some points')
    switch_page('create polygon')