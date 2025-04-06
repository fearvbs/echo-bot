from flask_socketio import SocketIO

socketio = SocketIO()

@socketio.on('message')
def handle_message(msg):
    # Логика обработки сообщений
    print('Received message: ' + msg)
    socketio.send('Echo: ' + msg)