import socketio
import time
import Adafruit_DHT
DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4 #

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
        