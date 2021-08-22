#!flask/bin/python
from app import socketio, app

socketio.run(app, host='localhost', port=5000)