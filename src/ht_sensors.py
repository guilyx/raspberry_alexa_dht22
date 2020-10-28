import time
import board
import adafruit_dht

period = 5 # in seconds
device = adafruit_dht.DHT22(board.D4)

def get_temperature():
    return device.temperature

def get_humidity():
    return device.humidity

if __name__ == "__main__":
    start_time = time.time()
    while True:
        if time.time() - start_time > period:
            t = get_temperature()
            h = get_humidity()
            print(f'Temperature ===> {t:.2f}...\nHumidity ===> {h:.2f}%...\n')
            start_time = time.time()

