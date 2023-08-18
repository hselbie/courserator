from tinydb import Query, TinyDB

db = TinyDB('shape_db.json')
client = Query()

o = db.search(client.name =='lower_wilder')
print(o)
print(type(o[0]))
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


# db.insert({'name': 'lower_wilder',
#            'data': {
#                'polygon': [
#                    (36.96115874872806, -122.091210258668),
#                    (36.96205031518519, -122.08417214221292),
#                    (36.97103397911931, -122.07953728503519),
#                    (36.973776871327395, -122.07717694110208),
#                    (36.979673754837854, -122.07378662890726),
#                    (36.98595301731587, -122.07784573093771),
#                    (36.98831830390587, -122.09900299564718),
#                    (36.98845541971369, -122.10677067295431),
#                    (36.98567877643166, -122.11215654865622),
#                    (36.976936830277275, -122.11668411747335),
#                    (36.967439538920225, -122.11337963596701)],
#                'start_points': [
#                    (36.96198357000689, -122.084413643779),
#                    (36.962065010724665, -122.0851512512581)]
#            }})

# db.insert({'name': 'moore_creek',
#            'data': {
#                'polygon': [
#                    (36.97606897102196, -122.06490349816127),
#                    (36.97547911193092, -122.07107941037559),
#                    (36.972159786875366, -122.07106766654603),
#                    (36.968352214696665, -122.06958172275178),
#                    (36.967816463148665, -122.0693801488355),
#                    (36.9664188615254, -122.0690209824666),
#                    (36.965064439931744, -122.06840407439317),
#                    (36.964991574795874, -122.06637095995988),
#                    (36.961896885237124, -122.06543218680467),
#                    (36.961425384095875, -122.06235301085557),
#                    (36.96153683008366, -122.06103872843828),
#                    (36.9654973431245, -122.06000876017656),
#                    (36.96919192169902, -122.06042718478288),
#                    (36.97035340529329, -122.0622671801671),
#                    (36.970691989425426, -122.06123184748735),
#                    (36.97186336977231, -122.06261706170982),
#                    (36.97166903966378, -122.06480097703331)],
#                'start_points': [
#                    (36.96162403168713, -122.06252541500787),
#                    (36.9609253491772, -122.06256296593408)
#                ]
#            }})

# db.insert({'name': 'full_and_upper_campus',
#            'data': {
#                'polygon': [
#                    (36.97745948006836, -122.0538162703273),
#                    (36.980476401324644, -122.05424542376969),
#                    (36.98459019208331, -122.0468639845607),
#                    (36.99000634399805, -122.04042668292496),
#                    (36.99062334949386, -122.03467602679703),
#                    (37.004538921529935, -122.04488987872574),
#                    (37.01187270549231, -122.0607685560939),
#                    (37.01865753893084, -122.07295651385758),
#                    (37.020028138800804, -122.07553143451187),
#                    (37.01619039686118, -122.08299870440933),
#                    (37.01146148399665, -122.06969494769547),
#                    (36.99619352363085, -122.06644722825726),
#                    (36.99218319216145, -122.06752011186322),
#                    (36.988498299484164, -122.06655451661786),
#                    (36.98464182528444, -122.06494519120892)],
#                'start_points': [
#                    (36.978684439891964, -122.05409329894994),
#                    (36.977617363955815, -122.05337983135198)]
#            }})


# db.insert({'name': 'full_wilder',
#            'data': {
#                'polygon': [
#                    (37.02359705231968, -122.09023220440245),
#                    (37.01235793146764, -122.07293732067443),
#                    (37.01132988012019, -122.08027584453917),
#                    (37.00399604378241, -122.0816491355548),
#                    (37.00101432857978, -122.07877380749083),
#                    (36.992171313164285, -122.07551224132872),
#                    (36.983430113075656, -122.07319481273986),
#                    (36.98380720518245, -122.06589920421935),
#                    (36.98195600781535, -122.06568462749816),
#                    (36.98055043899118, -122.06928951641417),
#                    (36.97931625959039, -122.07366688152648),
#                    (36.965156047147495, -122.08426697155333),
#                    (36.96206993697673, -122.08448154827452),
#                    (36.961864191850864, -122.08963138958312),
#                    (36.968996365100466, -122.09250671764708),
#                    (36.97197933552807, -122.09765655895568),
#                    (36.968962077404484, -122.0992444266925),
#                    (36.9645731248093, -122.10005981823302),
#                    (36.97057358241985, -122.10405094524718),
#                    (36.98099610996621, -122.10336429973937),
#                    (36.982333107228484, -122.10495216747618),
#                    (36.981510342462876, -122.11070282360411),
#                    (36.97225362579024, -122.1079991569171),
#                    (36.96889350196617, -122.11289150616027),
#                    (36.98075613361172, -122.13705284496642),
#                    (36.997724024370726, -122.10471613308287),
#                    (37.01031894940147, -122.09215266605712)],
#                'start_points': [(36.96198357000689, -122.084413643779),
#                                 (36.962065010724665, -122.0851512512581)]
#            }})
