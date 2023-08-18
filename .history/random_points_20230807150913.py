import numpy as np
import random
from shapely.geometry import Polygon, Point

poly = Polygon([(37.75850848099701, -122.50833008408812), (37.75911919711413, -122.49648544907835),(37.751620611284935, -122.4937388670471),(37.74863453749236, -122.50742886185911)])

def polygon_random_points (poly, num_points):
    min_x, min_y, max_x, max_y = poly.bounds
    points = []
    while len(points) < num_points:
            random_point = Point([random.uniform(min_x, max_x), random.uniform(min_y, max_y)])
            if (random_point.within(poly)):
                points.append(random_point)
    return points

if __name__ == '__main__'
# Choose the number of points desired. This example uses 20 points. 
points = polygon_random_points(poly,20)
# Printing the results.
for p in points:
    print(p.x,",",p.y)