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
fg = folium.FeatureGroup(name="Markers")
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
col1, col2 = st.columns(2)
with col1:
    st.markdown(
        "### Instructions:")
if col2.button("Add Random Checkpoints"):
    if map_data.get('all_drawings') is None:
        st.write('Please create a polygon')
    x = random_points.create_polygon(location_data=map_data)
    # x = random_points.polygon_random_points(poly=map_data, num_points=5)

    print('hugo')
# if col2.button("Add Random Checkpoints"):
#     st.session_state["markers"] = [folium.Marker(location=[random.randint(37, 38), random.randint(
#         -97, -96)], popup="Test", icon=folium.Icon(icon='user', prefix='fa', color="lightgreen")) for i in range(0, 10)]

if col2.button("Clear Map", help="ℹ️ Click me to **clear the map and reset**"):
    initialize_map.reset_session_state()
    m = initialize_map.initialize_map(
        center=st.session_state["center"], zoom=st.session_state["zoom"])


st.write("## map_data")
st.write(map_data)
st.write("## session_state")
st.write(st.session_state)