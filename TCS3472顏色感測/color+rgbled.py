import tcs34725
import time
import utime
from machine import I2C, Pin
from machine import Pin
import rp2,ws2812
from neopixel import Neopixel

numpix = 8
red = (255, 0, 0)
orange = (255, 50, 0)
yellow = (255, 100, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
indigo = (100, 0, 90)
violet = (200, 0, 100)
colors_rgb = [red, orange, yellow, green, blue, indigo, violet]

delay = 0.3

def handler(pin):
    print("interrupt!")
    sensor.interrupt(False)
i2c = I2C(0, sda=Pin(12), scl=Pin(13))
sensor = tcs34725.TCS34725(i2c)
sensor.active(True)
sensor.gain(4)  #1,4,16,60
#sensor.integration_time(402)    
int_pin = Pin(11, Pin.IN, Pin.PULL_UP)
int_pin.irq(handler=handler, trigger=Pin.IRQ_FALLING)
#sensor.threshold(1, 10000, 30000)


time.sleep_ms(500)

while True:
    sensor_data = sensor.read(10)
    if sensor_data[0] > sensor_data[1] and sensor_data[0] > sensor_data[2]:
        colors_rgb[0]
        print("R = ", sensor_data[0])
    elif sensor_data[1] > sensor_data[0] and sensor_data[1] > sensor_data[2]:
        colors_rgb[3]
        print("G = ", sensor_data[1])
    print("B = ", sensor_data[2])
    print("Brightness = ", sensor_data[3])
    print("===================================")
    sensor.threshold(1, 10000, 30000)
    time.sleep_ms(200)