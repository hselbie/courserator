from tinydb import Query, TinyDB

db = TinyDB('shape_db.json')
client = Query()

o = db.search(client.name =='lower_wilder')
print(type(o[0].get('data')))
def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

def format_point_list(point_list):
    split_comma = point_list.split(',')
    final_split = []
    for point in split_comma:
        if '\n' in point:
            split_point = point.split('\n')
            x0 = split_point[0]
            x1 = split_point[1]
            if is_float(x0):
                final_split.append(x0)
            if is_float(x1):
                final_split.append(x1)
        else:
            final_split.append(float(point))
    zipped = [(final_split[i],final_split[i+1]) for i in range(0,len(final_split),2)]

    return zipped 

def add_to_location_library(data_name, shape_coords, start_coords):
    db.insert({'name': data_name,
               'data':{'polygon': format_point_list(shape_coords), 'start_points': format_point_list(start_coords) }})
    return data_name

def get_all_shape_names():
    all_vals = db.all()
    all_names = [loc.get('name') for loc in all_vals] 
    return all_names

def get_shape_data(location_id, d_type):
    doc = db.search(client.name == location_id)[0]
    if d_type == 'polygon':
        return doc.data.get('polygon')
    elif d_type == 'start_points':
        return doc.data.get('start_points')
