from tinydb import TinyDB, Query

db = TinyDB('shape_db.json')
db_client = Query()
print(db.all())