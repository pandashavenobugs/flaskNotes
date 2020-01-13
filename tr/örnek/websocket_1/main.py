from flask import Flask, render_template
from flask_socketio import SocketIO, send
import eventlet

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
eventlet.monkey_patch(socket=True) # eventletin aktif edilmesi
#socketio = SocketIO(app)
socketio = SocketIO(app,async_mode="eventlet",log_output=True) #terminalde olayların gösterilmesi için log_output=True yapıldı
#aysnc_mode = "eventlet" projenin eventlet üzerinde koşması için
app.debug = True
@app.route("/")
def index():
	return render_template("index.html")
@socketio.on('message') # message eventi olduğu zaman çalışacak fonksiyon
def handleMessage(msg): # handleMessage fonskiyonunun ismi önemli değil önemli olan yukarıdaki event
#fonsiyonda tutulan msg socketio nun getirdiği en büyük özelliklerden birisi
# bu sayede hiçbir ek kod yazmadan msg değişkenini client'dan alabiliyor
	print('Message: ' + msg)
	send(msg, broadcast=True) # alınan verinin yayınlanabilmesi için broadcast =True yaptık

if __name__ == '__main__':
	socketio.run(app,host ="10.11.22.179")