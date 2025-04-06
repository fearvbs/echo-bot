from api.rest_api import app
from api.websocket_api import socketio
from main_services.twitch_service import TwitchBot

if __name__ == '__main__':
    # Запуск Twitch бота
    twitch_bot = TwitchBot()
    twitch_bot.run()

    # Запуск Flask API
    socketio.run(app, host='0.0.0.0', port=5000)