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

def get_bound_category(number, bounds_list):
    bounds_list.sort()

    lower_bound = bounds_list[0]
    upper_bound = bounds_list[-1]
    middle_bound = (lower_bound + upper_bound) / 2

    if number < lower_bound:
        return 1
    elif lower_bound <= number < middle_bound:
        return 5
    elif number == middle_bound:
        return 5
    elif middle_bound < number <= upper_bound:
        return 5
    elif number > upper_bound:
        return 9
    else:
        return "Out of Bounds"

def download_pts_kml(points: dict, caltopo=False):
    kml = simplekml.Kml()
    geodata = json.loads(points)
    features = geodata.get('features')
    distance_list = [data['properties'].get('distance_from_start') for data in features]
    S1 = [data for data in features if data['properties'].get('shape_name') in ['S1']]
    F1 = [data for data in features if data['properties'].get('shape_name') in ['F1']]
    course_name = features[0]['properties'].get('course_name')
    if caltopo:
        kml.newpoint(name='S1', coords = S1[0].get('geometry').get('coordinates'))
        for point in features:
            point_data = point['properties']
            point_name = point_data.get('shape_name')
            if point_name not in ['S1','F1']:
                point_value = get_bound_category(bounds_list=distance_list, number=point_data.get('distance_from_start'))
                flip = [point.get('geometry').get('coordinates')]
                kml.newpoint(name=f'{point_value}', coords=flip)
        kml.newpoint(name='F1', coords = F1[0].get('geometry').get('coordinates'))
        kml.save(f'output/cal_topo_{course_name}.kml')
    else:
        kml.newpoint(name='S1', coords = flip_lat_lng(S1[0].get('geometry').get('coordinates')))

        for point in features:
            point_data = point['properties']
            point_name = point_data.get('shape_name')
            if point_name not in ['S1','F1']:
                point_value = get_bound_category(bounds_list=distance_list, number=point_data.get('distance_from_start'))
                flip = flip_lat_lng(point.get('geometry').get('coordinates'))
                kml.newpoint(name=f'{point_value}', coords=flip)
        kml.newpoint(name='F1', coords = flip_lat_lng(F1[0].get('geometry').get('coordinates')))
        kml.save(f'output/{course_name}.kml')
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