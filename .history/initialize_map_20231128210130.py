import random
import folium
import numpy as np
import streamlit as st
from folium.plugins import Draw, MeasureControl
from streamlit_folium import st_folium

st.set_page_config(
    page_title="st_folium Example",
    page_icon="🔎",
    layout="wide"
)

def initialize_session_state(center_start: list, zoom_start: int):
    if "center" not in st.session_state:
        st.session_state["center"] = center_start
    if "zoom" not in st.session_state:
        st.session_state["zoom"] = zoom_start
    if "markers" not in st.session_state:
        st.session_state["markers"] = []
    if "map_data" not in st.session_state:
        st.session_state["map_data"] = {}
    if "all_drawings" not in st.session_state["map_data"]:
        st.session_state["map_data"]["all_drawings"] = None
    if "upload_file_button" not in st.session_state:
        st.session_state["upload_file_button"] = False


def reset_session_state(center_start: list, zoom_start: int):
    # Delete all the items in Session state besides center and zoom
    for key in st.session_state.keys():
        if key in ["center", "zoom"]:
            continue
        del st.session_state[key]
    initialize_map.initialize_session_state(CENTER_START, ZOOM_START)


def initialize_map(center, zoom):
    m = folium.Map(location=center, zoom_start=zoom, scrollWheelZoom=False)
    draw = Draw(export=False,
                filename='custom_drawn_polygons.geojson',
                position='topright',
                draw_options={'polyline': False,  # disable polyline option
                              'rectangle': False,  # disable rectangle option for now
                              # enable polygon option
                              #   'polygon': {'showArea': True, 'showLength': False, 'metric': False, 'feet': False},
                              'polygon': {'showArea': True},  # disable rectangle option for now
                              # enable circle option
                              'circle': False,
                            #   'circle': {'showArea': True, 'showLength': False, 'metric': False, 'feet': False},
                              'circlemarker': False,  # disable circle marker option
                              'marker': False,  # disable marker option
                              },
                edit_options={'poly': {'allowIntersection': False}})
    draw.add_to(m)
    MeasureControl(position='bottomleft', primary_length_unit='miles',
                   secondary_length_unit='meters', primary_area_unit='sqmiles', secondary_area_unit=np.nan).add_to(m)
    return m