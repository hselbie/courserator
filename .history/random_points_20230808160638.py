import numpy as np
import random
from shapely.geometry import Polygon, Point
import shapely
import simplekml
import location_library

location_keys = location_library.local_zone_collection.keys()
rand_number = random.randint(0,len(location_library.local_zone_collection))

polygon_raw = location_library.local_zone_collection.get(location_keys[rand_number])

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