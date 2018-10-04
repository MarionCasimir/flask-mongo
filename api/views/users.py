import json

from flask import request

from api.main import app
from api.controllers.users import get_users, get_user_by_id, post_user

@app.route('/users', methods=['GET', 'POST'])
def users(id=None):
    if request.method == 'GET':
        return get_users(request.args)
    elif request.method == 'POST':
        return post_user(request.form)

@app.route('/users/<int:id>', methods=['GET'])
def get_user_by_id(id):
    return get_user(id, request.args)
