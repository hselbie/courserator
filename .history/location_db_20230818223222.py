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
def remove_character_every_other(list, character):
  for i in range(0, len(list), 2):
    list[i] = list[i].replace(character, '')
  return list

def format_point_list(point_list):
    split_space = point_list.split(' ')
    clean_split_space = remove_character_every_other(split_space, ',')
    final_split = [is_float(point) for point in clean_split_space]
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
        return doc['data'].get('polygon')
    elif d_type == 'start_points':
        return doc['data'].get('start_points')
