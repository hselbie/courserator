import streamlit as st
import folium

# Create a folium map
m = folium.Map(location=[37.7697, -122.4461], zoom_start=13)

# Add a marker to the map
marker = folium.Marker([37.7697, -122.4461], popup="This is a marker")
m.add_child(marker)

# Add a button to the map
button = folium.Button(location=[37.7697, -122.4461], text="Add a marker")
m.add_child(button)

# Add a callback to the button
def add_marker(event):
#"""Adds a marker to the map."""
    folium.Marker(location=[event.lat, event.lng], popup="This is a marker").add_to(m)

button.on_click(add_marker)

# Display the map in Streamlit
st.folium_map(m)