import streamlit as st
import pandas as pd
import pydeck as pdk

def main():
    st.title("Geospatial Point Adder")

    # Create a DataFrame to store points and their names
    points_df = pd.DataFrame(columns=["Latitude", "Longitude"])

    # Map Initialization
    view_state = pdk.ViewState(latitude=0, longitude=0, zoom=2)
    layer = pdk.Layer(type="ScatterplotLayer", data=points_df, get_position="[Longitude, Latitude]", get_radius=1000)
    map_config = pdk.Deck(layers=[layer], initial_view_state=view_state, map_style="mapbox://styles/mapbox/light-v9")

    # Display the map
    st.pydeck_chart(map_config)

    # Add a message to the user
    st.sidebar.info("Click on the map to add a point.")

    # Sidebar for handling the added points
    st.sidebar.header("Added Points")

    # Listen to the map click event
    click_data = st.pydeck_chart(map_config, use_container_width=True, key="map")

    # Handle the click event and add the point to the map and DataFrame
    if click_data is not None and "latitude" in click_data:
        lat, lon = click_data["latitude"], click_data["longitude"]
        new_point = {"Latitude": lat, "Longitude": lon}
        points_df = pd.DataFrame([new_point])
        st.dataframe(points_df)

if __name__ == "__main__":
    main()
