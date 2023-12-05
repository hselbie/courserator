import folium
from folium.plugins import GroupedLayerControl
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
point_fg = folium.FeatureGroup(name='points')
folium.GeoJson(polygon).add_to(polygon_fg)

# Create a geometry list from the GeoDataFrame
geo_df_list = [[point.xy[1][0], point.xy[0][0]] for point in points.geometry]

for index, coordinates in enumerate(geo_df_list):
    print(index, coordinates)
    type_color='red'
    # assign a color marker for the type of volcano, Strato being the most common
    # name = points['shape_name'][index] 
    # if name == "p1":
    #     type_color = "green"
    # else:
    #     type_color = "purple"

    # Place the markers with the popup labels and data

    folium.Marker(location=coordinates, icon=folium.Icon(color="%s" % type_color)).add_to(point_fg)
print(points.head(50))

m.add_child(polygon_fg)
m.add_child(point_fg)
folium.LayerControl(collapsed=False).add_to(m)


# Create the map and store interaction data inside of session state
map_data = st_folium(m, width=1285, height=725)

data = st.session_state['map_data']

polygon = data.loc[data['shape_name'] == 'course_shape']
points = data.loc[data['type']=='point']