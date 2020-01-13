from flask import Flask, render_template
from flask_socketio import SocketIO, send
import eventlet

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
eventlet.monkey_patch(socket=True)
#socketio = SocketIO(app)
socketio = SocketIO(app,async_mode="eventlet",log_output=True)
app.debug = True
@app.route("/")
def index():
	return render_template("index.html")
@socketio.on('message')
def handleMessage(msg):
	print('Message: ' + msg)
	send(msg, broadcast=True)

if __name__ == '__main__':
	socketio.run(app,host ="10.11.22.179")