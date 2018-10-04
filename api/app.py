from flask import Flask

app = Flask(__name__)

import api.views.home
import api.views.stores
import api.views.users
