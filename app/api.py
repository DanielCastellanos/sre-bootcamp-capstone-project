"""Main start script for API"""
from flask import Flask
from _config import Config
from routes.health_check import health_check
from routes.login import login
from routes.networking import networking

app = Flask(__name__)

app.register_blueprint(health_check)
app.register_blueprint(login)
app.register_blueprint(networking)

if __name__ == '__main__':
    app.run(
        debug=Config.DEBUG,
        host=Config.API_HOST,
        port=Config.API_PORT
    )
