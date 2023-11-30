import random
import folium
import numpy as np
import streamlit as st
from streamlit_folium import st_folium
import initialize_map
import random_points

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
# Create the map and store interaction data inside of session state

col1, col2 = st.columns(2)
with col1:
    st.markdown(
        "### Instructions:")
if col2.button("Add Random Checkpoints"):
    if map_data.get('all_drawings') is None:
        st.write('Please create a polygon')
    else:
        x = random_points.create_polygon(location_data=map_data)
        y = random_points.polygon_random_points(poly=x, num_points=5)
        st.session_state["markers"] = [folium.Marker(location=[pt.coords[0][0], pt.coords[0][1]], popup='test', icon=folium.Icon(icon='user', prefix='fa')).add_to(m) for pt in y]


# elif col2.button("Clear Map", help="ℹ️ Click me to **clear the map and reset**"):
#     initialize_map.reset_session_state()
#     m = initialize_map.initialize_map(
#         center=st.session_state["center"], zoom=st.session_state["zoom"])

fg = folium.FeatureGroup(name="Markers")
for marker in st.session_state["markers"]:
    fg.add_child(marker)
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

st.write("## map_data")
st.write(map_data)
st.write("## session_state")
st.write(st.session_state)