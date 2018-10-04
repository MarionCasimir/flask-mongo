import os

from flask_mongoengine import MongoEngine

from api.main import app

db_user = os.environ.get('FM_DB_USER', 'root')
db_pass = os.environ.get('FM_DB_PASS', 'root')
db_name = os.environ.get('FM_DB_NAME', 'test_db')
db_host = os.environ.get('FM_DB_HOST', 'localhost')
db_port = os.environ.get('FM_PORT', 4000)

mongo_uri = 'mongodb://{user}:{passw}@{host}:{port}/{name}?authSource=admin'.format(
    user = db_user,
    passw = db_pass,
    host = db_host,
    port = db_port,
    name = db_name
)

app.config['MONGODB_SETTINGS'] = {
    'host': mongo_uri
}
db = MongoEngine(app)
