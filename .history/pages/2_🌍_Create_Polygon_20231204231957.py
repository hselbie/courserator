import folium
import geopandas as gpd
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
CENTER_START = [36.97447, -122.02091]
ZOOM_START = 12

course_name = st.text_input('input your course name')

initialize_map.initialize_session_state(CENTER_START, ZOOM_START)

m = initialize_map.initialize_map(
    center=st.session_state["center"], zoom=st.session_state["zoom"])

# Create the map and store interaction data inside of session state
map_data = st_folium(
    m,
    center=st.session_state["center"],
    zoom=st.session_state["zoom"],
    key="new",
    width=1285,
    height=725,
    returned_objects=["all_drawings"],
    use_container_width=True
)
point_number = st.number_input(label='how many points')
col1, col2 = st.columns(2)
with col1:
    st.markdown(
        "### Instructions:")
if col2.button("Add Start Point"):
    if map_data.get('all_drawings') is None:
        st.write('Please create a polygon')
    else:
        polygon = random_points.create_polygon(location_data=map_data)
        random_points = random_points.polygon_random_points(poly=polygon, num_points=point_number)
        point_data = {'course_name':[],'shape_name':[], 'geometry':[], 'type':[]}
        for point in random_points:
            point_data.get('course_name').append(course_name)
            point_data.get('shape_name').append('p1')
            point_data.get('geometry').append(point)
            point_data.get('type').append('point')


        polygon_data = {'course_name':[course_name],'shape_name':['course_shape'], 'geometry':[polygon], 'type':'polygon'}
        gdf = gpd.GeoDataFrame(d, crs="EPSG:4326")

        st.session_state['map_data'] = gdf
        st.session_state['course_name'] = course_name
        switch_page('start point')
        
elif col2.button("Clear Map", help="ℹ️ Click me to **clear the map and reset**"):
    initialize_map.reset_session_state(center_start=st.session_state["center"], zoom_start=st.session_state["zoom"])
    m = initialize_map.initialize_map(
        center=st.session_state["center"], zoom=st.session_state["zoom"])


st.write("## map_data")
st.write(map_data)
st.write("## session_state")
st.write(st.session_state)