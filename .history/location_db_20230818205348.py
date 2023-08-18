from tinydb import TinyDB, Query

db = TinyDB('shape_db.json')
db_client = Query()
db.insert({'type': 'apple', 'count': 7})
db.insert({'type': 'peach', 'count': 3})
print(db.all())