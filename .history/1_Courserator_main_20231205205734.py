import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Welcome to the Courserator! 👋")

st.markdown(
    """
    #### This is a quick and dirty app to generate a course for you to play around with using the maprun 7 software. 

    ### 👈 To create a course click 'Create Polygon link on the sidebar and follow the on screen instructions'

"""
)
st.markdown('''    
            ### Once you have downloaded your course.

    When you have created your course, and download you'll receive a zipfile with two kml's. You then need to two steps.
    1. Upload your course to maprun 7 checksites page [link](https://console.maprun.net/#/check_sites_create)
    2. Create your map on cal_topo [link](https://caltopo.com/map.html#ll=36.97571,-122.09742&z=14&b=om)

    For step 1. you do not need to upload a kmz, just upload the kml file that looks like 'your_course_name.kml'
    For step 2. you can go crazy here, but think about what you will need to navigate in terms of layers on the right to add or subtract
    in the map objects bar on the left click on import and import the kml 'cal_topo_your_course_name.kml'
    
    The reason for the two is for some reason mapping orgs reverse their dependencies on lat, lng to lng, lat.

            
            ''')