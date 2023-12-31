import folium
from folium.plugins import GroupedLayerControl
import geopandas as gpd
import streamlit as st
from streamlit_folium import st_folium
import initialize_map
import random_points
from streamlit_extras.switch_page_button import switch_page 
import fiona


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

for row in points.iterrows():
    # assign a color marker for the type of volcano, Strato being the most common
    geom = row[1].geometry
    coordinates = [geom.xy[1][0], geom.xy[0][0]]
    if row[1]['shape_name']== "S1":
        type_color = "green"
    elif row[1]['shape_name']== "F1":
        type_color = 'black'
    else:
        type_color = "red"

    # Place the markers with the popup labels and data

    folium.Marker(location=coordinates, icon=folium.Icon(color="%s" % type_color)).add_to(point_fg)
print(points.head(50))

m.add_child(polygon_fg)
m.add_child(point_fg)
folium.LayerControl(collapsed=False).add_to(m)

# Create the map and store interaction data inside of session state
map_data = st_folium(m, width=1285, height=725)

point_s1= points[points['shape_name']=='S1']['geometry'].iloc[0]
course_name = points[points['shape_name']=='S1']['course_name'].iloc[0]
 
points['distance_from_start']= points['geometry'].distance(point_s1)

test = points.to_json()

random_points.download_pts_kml(points = test)
random_points.download_pts_kml(points= test, caltopo=True)
import zipfile
zip = zipfile.ZipFile("output/course_files.zip", "w", zipfile.ZIP_DEFLATED)
zip.write(f'output/{course_name}.kml')
zip.write(f'output/cal_topo_{course_name}.kml')
zip.close()

st.write('Does this course look good to you, if so click the download button')
with open(f'output/course_files.zip', 'rb') as f:
    st.download_button('Download Course', f, file_name=f'{course_name}.zip')  # Defaults to 'application/octet-stream'
link = '[Checksites Maprun Link](https://console.maprun.net/#/check_sites_create)'
st.markdown(link, unsafe_allow_html=True)


