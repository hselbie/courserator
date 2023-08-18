import numpy as np
import random
from shapely.geometry import Polygon, Point
import simplekml
import location_db

def get_rando_location_object():
    locations = location_db.get_all_shape_names()
    rand_number = random.randint(0,len(locations)-1)   
    return locations[rand_number]

def get_polygon(location_id: str):
    polygon_raw = location_db.get_shape_data(location_id=location_id, d_type='polygon')
    poly = Polygon(polygon_raw)
    return poly

def get_start_points(location_id: str):
    start_points = location_db.local_zone_collection.get(location_id)['start_points']
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

def sort_distances(dist_list):
   tranches = int(len(dist_list)/3)
   sorted_list = sorted(dist_list)
   sample = {}
   sample['top'] = [sorted_list[-tranches:]][0]
   sample['middle'] = [sorted_list[tranches:-tranches]][0]
   sample['bottom'] = [sorted_list[0:tranches]][0]
   return sample

def find_key(input_dict, value):
    for k,v in input_dict.items():
        if value in v:
            return k
        
def convert_rando_points_kml(start_points: list, points: list, location_id: str):
    kml = simplekml.Kml()
    distance_list = create_distances(start_points=start_points, points=points)
    dist_dict = sort_distances(dist_list=distance_list)
    sp = Point([start_points[0]])
    kml.newpoint(name='S1', coords = flip_lat_lng(start_points[0]))
    for index, p in enumerate(points):
        dist = sp.distance(p)
        distance=find_key(dist_dict, dist)
        if distance == 'top':
            pvalue = 5
        elif distance == 'middle':
            pvalue = 2
        elif distance == 'bottom':
            pvalue = 1

        flip = flip_lat_lng(p)
        kml.newpoint(name=f'{pvalue}{index}', coords=flip)
    kml.newpoint(name='F1', coords = flip_lat_lng(start_points[1]))
    kml.save(f'output/{location_id}.kml')
    kml.savekmz(f'output/{location_id}.kmz')
    print('imma done')

def main(p_number):    
    location_string = get_rando_location_object()
    chosen_polygon = get_polygon(location_id=location_string)
    spoint = get_start_points(location_id=location_string)
    points = polygon_random_points(poly=chosen_polygon,num_points= p_number)
    convert_rando_points_kml(start_points=spoint, points=points, location_id=location_string)


if __name__ == '__main__':
    # Choose the number of points desired. This example uses 20 points. 

    # location_string = get_rando_location_object()
    chosen_polygon = get_polygon(location_id=location_string)
    # spoint = get_start_points(location_id=location_string)
    # points = polygon_random_points(poly=chosen_polygon,num_points= 20)
    # convert_rando_points_kml(start_points=spoint, points=points, location_id=location_string)
    # format_point_list(point_list=sample_data)