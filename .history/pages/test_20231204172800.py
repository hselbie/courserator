import streamlit as st
import folium
from streamlit_folium import folium_static
from streamlit_custom_notification_box import custom_notification_box
st.subheader("Component with constant args")

styles = {'material-icons':{'color': 'red'},
          'text-icon-link-close-container': {'box-shadow': '#3896de 0px 4px'},
          'notification-text': {'':''},
          'close-button':{'':''},
          'link':{'':''}}

custom_notification_box(icon='info', textDisplay='We are almost done with your registration...', externalLink='more info', url='#', styles=styles, key="foo")
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
modal = st.expander("Advanced options")

option_1 = modal.checkbox("Option 1")
option_2 = modal.checkbox("Option 2")
option_3 = modal.checkbox("Option 3")
option_4 = modal.checkbox("Option 4")

if option_1:
   st.write("Hello world 1")

if option_2:
   st.write("Hello world 2")

if option_3:
   st.write("Hello world 3")

if option_4:
   st.write("Hello world 4")
   
if st.button("Add Point"):
    # Add the new point to the session state
    add_point(new_point_name, new_latitude, new_longitude)

    # Rerun the app to update the map with the new point
    st.experimental_rerun()
