import streamlit as st
import numpy as np
from shapely.geometry import Point, Polygon
import matplotlib.pyplot as plt
import geopandas as gpd
import geopandas.tools

def generate_random_points_in_polygon(polygon, num_points):
    minx, miny, maxx, maxy = polygon.bounds
    points = []
    while len(points) < num_points:
        random_point = Point(np.random.uniform(minx, maxx), np.random.uniform(miny, maxy))
        if polygon.contains(random_point):
            points.append(random_point)
    return points

def main():
    st.title("Random Points in User-Generated Polygon")

    # User draws a polygon
    st.sidebar.header("Draw a Polygon:")
    polygon_geojson = st.sidebar.map.draw_polygon()

    # Convert GeoJSON to Shapely Polygon
    polygon = gpd.GeoSeries.from_features([polygon_geojson]).iloc[0]

    # Display the user-generated polygon
    fig, ax = plt.subplots()
    gpd.GeoSeries([polygon]).plot(ax=ax, alpha=0.5, color='blue')
    ax.set_title("User-Generated Polygon")
    st.pyplot(fig)

    # Number of random points input
    num_points = st.sidebar.number_input("Number of Random Points", min_value=1, step=1, value=10)

    # Generate and display random points in the polygon
    random_points = generate_random_points_in_polygon(polygon, num_points)
    random_points_gdf = gpd.GeoDataFrame(geometry=random_points)

    # Plotting the random points
    fig, ax = plt.subplots()
    gpd.GeoSeries([polygon, random_points_gdf]).plot(ax=ax, alpha=0.5, color=['blue', 'red'])
    ax.set_title("Random Points in Polygon")
    st.pyplot(fig)

if __name__ == "__main__":
    main()
