import socketio
import time
import Adafruit_DHT
DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4 #

humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
sio = socketio.Client() # client açma işlemi
connected = False
time.sleep(5)
while not connected:
    try:
        sio.connect("http://10.11.22.179:5000") #socketio ya bağlanılması
        connected = True
    except:
        print("baglaniliyor")
        time.sleep(0.3)
sayac = 0
succes = False

while True:
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)# sensör değerinin alınması
    msg="sayac = {0} nem = {1} , sicaklik = {2}".format(sayac,humidity,temperature)
    sio.emit("message",msg)#emit send gibi bir komut ve emit sayesinde istenilen event'e veri gönderebiliyoruz
    #msg nin olduğu yere callback fonsiyonu da gelebilir aslında biz sadece değişken değil fonksiyon da gönderebiliyoruz
    sayac = sayac + 1
    time.sleep(1)
    if sayac == 101:
        
        break
exit()
        