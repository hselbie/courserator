import numpy as np
import random
from shapely.geometry import Polygon, Point
import simplekml
import json

def create_point(location_data: list):
    pts = location_data['all_drawings'][0]['geometry']['coordinates']
    point = Point([pts[0], pts[1]])
    return point 

def create_polygon(location_data: list):
    pts = location_data['all_drawings'][0]['geometry']['coordinates'][0]
    polygon = Polygon(pts)
    return polygon

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

def distance_breakdown(distance_list: list):
    pass

def verify_distance_buckets(distance_buckets: dict, distance_number: int):
    pass

def download_pts_kml(points: dict):
    kml = simplekml.Kml()
    geodata = json.loads(points)
    features = geodata.get('features')
    distance_list = [data['properties'].get('distance_from_start') for data in features]
    distance_buckets = distance_breakdown(distance_list)
    S1 = [data['properties'] for data in features if data['properties'].get('shape_name') in ['S1']]
    F1 = [data['properties'] for data in features if data['properties'].get('shape_name') in ['F1']]
    course_name = features[0]['properties'].get('course_name')
    kml.newpoint(name='S1', coords = flip_lat_lng(S1.get('geometry').get('coordinates')))

    for point in features:
        point_data = point['properties']
        point_name = point_data.get('shape_name')
        if point_name not in ['S1','F1']:
            point_value = verify_distance_buckets(distance_buckets=distance_buckets, distance_number=point_data.get('distance_from_start'))
            flip = flip_lat_lng(point.get('geometry').get('coordinates'))
            kml.newpoint(name=f'{point_value}', coords=flip)
    kml.newpoint(name='F1', coords = flip_lat_lng(F1.get('geometry').get('coordinates')))
    kml.save(f'output/{location_id}.kml')
    print('imma done')

def create_groundoverlay_kmz(poly, overlay_name:str):
    kml = simplekml.Kml()
    file_path = kml.addfile('output/hugo1.kml')
    fol = kml.newfolder(name='test')
    min_x, min_y, max_x, max_y = poly.bounds
    ground = fol.newgroundoverlay(name='GroundOverlay')
    ground.icon.href = file_path
    ground.latlonbox.north = max_y
    ground.latlonbox.south = min_y 
    ground.latlonbox.east = min_x 
    ground.latlonbox.west = min_x 
    ground.latlonbox.rotation = -14
    kml.savekmz(f"output/{overlay_name}.kmz")

       
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

def get_specific_course(location_string, p_number):
    chosen_polygon = get_polygon(location_id=location_string)
    spoint = get_start_points(location_id=location_string)
    points = polygon_random_points(poly=chosen_polygon,num_points= p_number)
    convert_rando_points_kml(start_points=spoint, points=points, location_id=location_string)



if __name__ == '__main__':
    pass
    # Choose the number of points desired. This example uses 20 points. 

    # location_string = get_rando_location_object()
    # chosen_polygon = get_polygon(location_id=location_string)
    # spoint = get_start_points(location_id=location_string)
    # points = polygon_random_points(poly=chosen_polygon,num_points= 20)
    # convert_rando_points_kml(start_points=spoint, points=points, location_id=location_string)
    # format_point_list(point_list=sample_data)