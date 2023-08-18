import numpy as np
import random
from shapely.geometry import Polygon, Point
import shapely
import simplekml
import location_library

def get_rando_location_object():
    location_keys = list(location_library.local_zone_collection.keys())
    rand_number = random.randint(0,len(location_library.local_zone_collection)-1)
    return location_keys[rand_number]

def get_polygon(location_id: str):
    polygon_raw = location_library.local_zone_collection.get(location_id)['polygon']
    poly = Polygon(polygon_raw)
    return poly

def get_start_points(location_id: str):
    start_points = location_library.local_zone_collection.get(location_id)['start_points']
    return start_points

def polygon_random_points (poly, num_points):
    min_x, min_y, max_x, max_y = poly.bounds
    points = []
    while len(points) < num_points:
            random_point = Point([random.uniform(min_x, max_x), random.uniform(min_y, max_y)])
            if (random_point.within(poly)):
                points.append(random_point)
    return points

def flip_lat_lng(p):
    if isinstance(p, Point):
        flip = (p.coords[0][1], p.coords[0][0])
    else:
        flip = (p[1],p[0])
    return [flip]

def create_distances(start_points: list, points: list):
    dist_distribution = []
    start_points = Point([start_points[0]])
    for p in points:
        dist = start_points.distance(p) 
        dist_distribution.append(dist)
    return dist_distribution
    

def convert_rando_points_kml(start_points: list, points: list):
    kml = simplekml.Kml()
    distance_list = create_distances(start_points=start_points, points=points)
    for index, p in enumerate(points):
        flip = flip_lat_lng(p)
        kml.newpoint(name=f'p{index}', coords=flip)
    kml.newpoint(name='s1', coords = flip_lat_lng(start_points[0]))
    kml.newpoint(name='f1', coords = flip_lat_lng(start_points[1]))
    kml.save('test.kml')
    print('imma done')



if __name__ == '__main__':
    # Choose the number of points desired. This example uses 20 points. 
    location_string = get_rando_location_object()
    chosen_polygon = get_polygon(location_id=location_string)
    spoint = get_start_points(location_id=location_string)
    points = polygon_random_points(chosen_polygon,20)
    convert_rando_points_kml(start_points=spoint, points=points)