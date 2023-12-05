import streamlit as st
import pandas as pd
import folium
from streamlit_folium import folium_static

def main():
    st.title("Point Placer Web App")

    # Create a DataFrame to store points and their names
    points_df = pd.DataFrame(columns=["Latitude", "Longitude", "Name"])

    # Map Initialization
    map_center = [0, 0]
    map_zoom = 2
    m = folium.Map(location=map_center, zoom_start=map_zoom)

    # Display the map
    folium_static(m)

    # Sidebar for adding points
    st.sidebar.header("Add a Point")
    name = st.sidebar.text_input("Point Name:")
    latitude = st.sidebar.number_input("Latitude:", min_value=-90.0, max_value=90.0, value=0.0)
    longitude = st.sidebar.number_input("Longitude:", min_value=-180.0, max_value=180.0, value=0.0)

    if st.sidebar.button("Add Point"):
        # Add the point to the DataFrame
        new_point = {"Latitude": latitude, "Longitude": longitude, "Name": name}
   
