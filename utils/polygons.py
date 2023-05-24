import json
from shapely.geometry import Polygon, Point
import numpy as np

def load_polygons(json_path):
    with open(json_path) as file:
        poly_json = json.load(file)
    poly_json_shapes = poly_json['shapes']

    polygons = {}
    
    for shape in poly_json_shapes:
        points = shape['points']
        polygons[shape['label']] = {'poly': Polygon(points), 'draw_coords': np.array(points, dtype=int).reshape(-1,1,2)}

    return polygons

def point_in_polygon(polygon, point):
    point = Point(point)
    return polygon.intersects(point)