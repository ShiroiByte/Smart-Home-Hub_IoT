import pyrebase
import dht11
import time
import board

config = {
  "apiKey": "",
  "authDomain": "",
  "databaseURL": "",
  "storageBucket": ""
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()

instance = dht11.DHT11(pin = 24)

while True:
    result = instance.read()
    data = {
        "Temperature" : result.temperature,
        "Humidity" : result.humidity
    }
    db.update(data)
    time.sleep(10)