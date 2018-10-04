from api.utils.mongo import db

class User(db.Document):
    _id = db.IntField(required=True)
    name = db.StringField(required=False, max_length=50)
    meta = {'collection': 'users'}
