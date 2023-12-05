import streamlit as st
import pandas as pd
import folium
from streamlit_folium import folium_static
import pydeck as pdk

# Create a sample DataFrame with some data
data = {
    'latitude': [37.7749, 40.7128, 34.0522],
    'longitude': [-122.4194, -74.0060, -118.2437],
    'location': ['San Francisco', 'New York', 'Los Angeles']
}
df = pd.DataFrame(data)

# Create a Streamlit app
st.title('Folium Map with Streamlit')

# Display the Folium map with the provided coordinates
m = folium.Map(location=[df['latitude'].mean(), df['longitude'].mean()], zoom_start=4)

for index, row in df.iterrows():
    folium.Marker([row['latitude'], row['longitude']], popup=row['location']).add_to(m)

# Display the Folium map using the folium_static function
folium_static(m)

# Use pydeck to handle map interactions and retrieve the clicked coordinates
layer = pdk.Layer(
    "ScatterplotLayer",
    data=df,
    get_position="[longitude, latitude]",
    get_radius=200000,
    get_color="[200, 30, 0, 160]",
    pickable=True,
)
view_state = pdk.ViewState(latitude=df['latitude'].mean(), longitude=df['longitude'].mean(), zoom=4, pitch=40.5, bearing=-27)
tooltip = {"text": "Location: {location}\nLat: {latitude}\nLong: {longitude}"}
r = pdk.Deck(map_style="mapbox://styles/mapbox/light-v9", layers=[layer], initial_view_state=view_state, tooltip=tooltip)

# Display the pydeck map using the st.pydeck_chart function
st.pydeck_chart(r)

# Display the clicked coordinates
if st.pydeck_chart(r):
    st.write("Clicked Coordinates:", st.pydeck_chart(r).json_click["geometry"]["coordinates"])
