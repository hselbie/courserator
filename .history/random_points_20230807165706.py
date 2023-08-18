import numpy as np
import random
from shapely.geometry import Polygon, Point
import shapely
import simplekml

polygon_raw = [(36.96115874872806, -122.091210258668,) 
               (36.96205031518519, -122.08417214221292), 
               (36.97103397911931, -122.07953728503519),
               (36.973776871327395, -122.07717694110208),
               (36.979673754837854, -122.07378662890726),
               (36.98595301731587, -122.07784573093771),
               (36.98831830390587, -122.09900299564718),
               (36.98845541971369, -122.10677067295431),
               (36.98567877643166, -122.11215654865622),
               (36.976936830277275, -122.11668411747335),
               (36.967439538920225, -122.11337963596701)]


poly = Polygon(polygon_raw)

def polygon_random_points (poly, num_points):
    min_x, min_y, max_x, max_y = poly.bounds
    points = []
    while len(points) < num_points:
            random_point = Point([random.uniform(min_x, max_x), random.uniform(min_y, max_y)])
            if (random_point.within(poly)):
                points.append(random_point)
    return points

def convert_rando_points_togeojson(points: list) -> dict:
    p = shapely.to_geojson(points)
    print(p)

def convert_rando_points_kml(points: list):
    kml = simplekml.Kml()
    for index, p in enumerate(points):
        flip = (p.coords[0][1], p.coords[0][0])
        kml.newpoint(name=f'p{index}', coords=[flip])
    kml.save('test.kml')
    print(kml)



if __name__ == '__main__':
    # Choose the number of points desired. This example uses 20 points. 
    points = polygon_random_points(poly,20)
    convert_rando_points_kml(points=points)