from app import *
import random


@socketio.on('my event bar')
def test_message(message):
    print(message)
    emit('Hah')


@socketio.on('test repka')
def test_message(message):
    print(message)
    re = DB.GET('select * from rooms')
    
    print(re)
    emit('repka', {'data': {'name':"Amal",'lastName':'Agishev', 'message':random.randint(0, 515)}})


@socketio.on('send_room')
def send_room(data):
    print(data)
    emit('room_senders', data, room=data['room'])

@socketio.on('join')
def on_join(data):
    print(data)
    username = data['username']
    room = data['room']
    join_room(room)
    send(username + ' has entered the room.', to=room)

@socketio.on('leave')
def on_leave(data):
    username = data['username']
    room = data['room']
    leave_room(room)
    send(username + ' has left the room.', to=room)