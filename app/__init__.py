
import random

from service import JWT, data_base, theards, user_server_data
from settings import env


from flask import *
from flask_cors import CORS
from flask_socketio import SocketIO, emit, join_room, leave_room, send, rooms
DB = data_base.DB


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.debug = True
CORS(app)
socketio = SocketIO(app)
socketio.run(app)
from app import views, api, errors, socket_f