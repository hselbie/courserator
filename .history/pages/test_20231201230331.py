import streamlit as st
import pandas as pd
import streamlit_leaflet as st_leaflet

def main():
    st.title("Geospatial Point Adder")

    # Create a DataFrame to store points and their names
    points_df = pd.DataFrame(columns=["Latitude", "Longitude"])

    # Map Initialization
    map_center = [0, 0]
    map_zoom = 2

    # Create a Streamlit Leaflet map
    m = st_leaflet(st.empty(), center=map_center, zoom=map_zoom, key="map")

    # Add a message to the user
    st.sidebar.info("Click on the map to add a point.")

    # Sidebar for handling the added points
    st.sidebar.header("Added Points")

    # Listen to the map click event
    click_data = st_leaflet(callback="click", key="map")

    # Handle the click event and add the point to the map and DataFrame
    if click_data is not None and "latlng" in click_data:
        lat, lon = click_data["latlng"]["lat"], click_data["latlng"]["lng"]
        new_point = {"Latitude": lat, "Longitude": lon}
        points_df = pd.DataFrame([new_point])
        st.dataframe(points_df)

        # Add the point to the map
        st_leaflet.marker(locations=[[lat, lon]], key="map")

if __name__ == "__main__":
    main()
