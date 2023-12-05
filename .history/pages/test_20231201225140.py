import streamlit as st
import pandas as pd
import folium

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
        points_df = points_df.append(new_point, ignore_index=True)

        # Add the point to the map
        folium.Marker([latitude, longitude], popup=name).add_to(m)

        # Clear input fields
        st.sidebar.text_input("Point Name:", value="")
        st.sidebar.number_input("Latitude:", min_value=-90.0, max_value=90.0, value=0.0)
        st.sidebar.number_input("Longitude:", min_value=-180.0, max_value=180.0, value=0.0)

    # Display the points DataFrame
    st.header("Points Added:")
    st.dataframe(points_df)

# Function to display folium map in Streamlit
def folium_static(fig, width=700, height=500):
    fig.add_child(folium.LatLngPopup())
    components.html(fig._repr_html_(), width=width, height=height)

if __name__ == "__main__":
    main()

