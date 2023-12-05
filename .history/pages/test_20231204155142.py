import streamlit as st
import folium
from streamlit_folium import folium_static

# Function to initialize or update the session state
def init_session_state():
    if "points" not in st.session_state:
        st.session_state.points = []

# Function to add a new point to the session state
def add_point(name, latitude, longitude):
    st.session_state.points.append({"name": name, "latitude": latitude, "longitude": longitude})

# Function to display the Folium map and handle points
def display_map():
    m = folium.Map(location=[37.7749, -122.4194], zoom_start=4)

    # Check if there are existing points and display them on the map
    if st.session_state.points:
        for point in st.session_state.points:
            folium.Marker([point["latitude"], point["longitude"]], popup=point["name"]).add_to(m)

    # Display the Folium map using the folium_static function
    folium_static(m)

# Main Streamlit app
st.title('Folium Map with Streamlit')

# Initialize or update the session state
init_session_state()

# Display the Folium map and handle points
display_map()

# Allow the user to add a new point
st.header("Add New Point")
new_point_name = st.text_input("Enter Point Name:")
new_latitude = st.number_input("Enter Latitude:")
new_longitude = st.number_input("Enter Longitude:")

if st.button("Add Point"):
    # Add the new point to the session state
    add_point(new_point_name, new_latitude, new_longitude)

    # Rerun the app to update the map with the new point
    st.experimental_rerun()
