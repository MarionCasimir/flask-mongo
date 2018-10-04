from flask_api import status
from mongoengine.errors import ValidationError

from api.schemas import User
from api.utils.mongo import db

def get_users(request_args=None):
    result = User.objects.get_or_404(**request_args.to_dict())
    return result.to_json()

def get_user_by_id(id, request_args=None):
    result = User.objects.get_or_404(_id=id, **request_args.to_dict())
    return result

def post_user(request_args=None):
    try:
        user = User(**request_args.to_dict())
        result = user.save()
        return result.to_json(), status.HTTP_200_OK
    except ValidationError as e:
        return str(e), status.HTTP_400_BAD_REQUEST
