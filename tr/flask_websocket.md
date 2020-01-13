# Bu dökümantasyon flask ile websocket progralanması giriş seviyesinde anlatılmaktadır.

## gerekli olan kütüphanelerin kurulması 
* ihtiyacımız olan kütüphanaler flask-socketio ,Adafruit_DHT, eventlet ve python-socketio[client]. İlk olarak kütüphanelerimizi kuruyoruz.

```bash
pip install flask-socketio
pip install eventlet
pip install "python-socketio[client]"
pip install Adafruit_DHT

```
# socketio nasıl çalışır?
* socketio tamamiyle "event" ler üzerinden çalışmaktadır. Bu sayede client ile server arasında iletişim sağlanmaktadır. Socketio sistemi server-client ilişkisiyle çalışmaktadır. Her event'in iki özelliği vardır; veri al ve veri at. Ancak başlı başına hiçbir ek komut göndermeksizin herbir event veri tutabilir bu yüzden veri aktaracağımız zaman belirli başlı komutlar kullanmamız yeterli.

* sistemin flask tarafındaki server kodu:

```python
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
```
* sistemin javascript arayüz client kodu:
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Document</title>
</head>
<body>
  <script src="{{ url_for('static', filename='socket.io.js') }}"></script>
  <script>
    var socket = io("http://10.11.22.179:5000")
    socket.on('connect',function(){
      socket.send("user has connected")
    });
    socket.on('message',function(msg){
      document.getElementById("demo").innerHTML = msg;
    });
    
  </script>
  <p id="demo">hello</p>
</body>
</html>
```
* burada önemli bir nokta var socketio kütüphanesine ihtiyacımız var : https://github.com/socketio/socket.io-client/blob/master/dist/socket.io.js linkinden socketio javascript kütüphanemizi indirip static klasörün içine atıyoruz.

* şimdi ise client python kodları:

```python
import socketio
import time
import Adafruit_DHT
DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4 # bcm! gpio değil ! 

humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
sio = socketio.Client()
connected = False
time.sleep(5)
while not connected:
    try:
        sio.connect("http://10.11.22.179:5000")
        connected = True
    except:
        print("baglaniliyor")
        time.sleep(0.3)
sayac = 0
succes = False

while True:
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    msg="sayac = {0} nem = {1} , sicaklik = {2}".format(sayac,humidity,temperature)
    sio.emit("message",msg)
    sayac = sayac + 1
    time.sleep(1)
    if sayac == 101:
        
        break
exit()
        
```
* en son olarak flask projesini başlatın daha sonra client scriptini aktif hale getirin.
