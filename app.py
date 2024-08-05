"""For coroutine managment import asyncio"""
import asyncio
import threading
import sqlite3
from flask import Flask, render_template
from src.sockets.serve_mouse import serve_socket
from src.mouse.output import mouse_listener
from src.bp.routes import show_data_bp
from src.common.constants import create_table, db_name

app = Flask(__name__)
app.register_blueprint(show_data_bp)
connection = sqlite3.connect(db_name)
cursor = connection.cursor()
cursor.execute(create_table)

socket_thread = threading.Thread(target=asyncio.run, args=(serve_socket(),))
socket_thread.start()
mouse_listener.start()

if __name__ == "__main__":
    app.run()
