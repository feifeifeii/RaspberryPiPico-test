import time
from machine import Pin
import HC_SR04

trig = Pin(10, Pin.OUT)
echo = Pin(4, Pin.IN)

def ping():
    trig.value(1)
    time.sleep_us(10)
    trig.value(0)
    count = 0
    timeout = False
    start = time.ticks_us()
    while not echo.value(): #wait for HIGH
        time.sleep_us(10)
        count+=1
        if count > 100000: #over 1s timeout
            timeout = True
            break