import streamlit as st
import folium

# st.write('working')
# Create a folium map
m = folium.Map(location=[37.7697, -122.4461], zoom_start=13)

# Add a marker to the map
marker = folium.Marker([37.7697, -122.4461], popup="This is a marker")
m.add_child(marker)

# Add a button to the map
# button = folium.Button(location=[37.7697, -122.4461], text="Add a marker")
# m.add_child(button)
lat = st.number_input('latitude')
lng = st.number_input('longitude')
btn_name = st.text_input('name')

button = st.button('clickme', on_click=add_marker(lat, lng, btn_name))

# Add a callback to the button
def add_marker(latitude, longitude, name):
#"""Adds a marker to the map."""
    folium.Marker(location=[latitude, longitude], popup=name).add_to(m)


# Display the map in Streamlit
st.folium_map(m)