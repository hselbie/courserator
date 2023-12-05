import streamlit as st
import folium
from streamlit_folium import folium_static
import pandas as pd

def main():
    st.title("Geospatial Point Adder")

    # Create a DataFrame to store points and their names
    points_df = pd.DataFrame(columns=["Latitude", "Longitude"])

    # Map Initialization
    map_center = [0, 0]
    map_zoom = 2
    m = folium.Map(location=map_center, zoom_start=map_zoom, control_scale=True)

    # Display the map
    folium_static(m)

    # Add a message to the user
    st.sidebar.info("Click on the map to add a point.")

    # Sidebar for handling the added points
    st.sidebar.header("Added Points")

    # Listen to the map click event
    m.add_child(folium.ClickForMarker(popup="Add a point"))

    # Handle the click event and add the point to the map and DataFrame
    @st.cache
    def handle_click(lat, lon):
        new_point = {"Latitude": lat, "Longitude": lon}
        points_df = pd.DataFrame([new_point])
        st.dataframe(points_df)

        # Add the point to the map
        folium.Marker([lat, lon], popup=f"({lat}, {lon})").add_to(m)
        folium_static(m)

    # Streamlit callback function for handling click event
    lat, lon = 0, 0
    if m.click_info is not None:
        lat, lon = m.click_info["lat_lng"]
        handle_click(lat, lon)

if __name__ == "__main__":
    main()
