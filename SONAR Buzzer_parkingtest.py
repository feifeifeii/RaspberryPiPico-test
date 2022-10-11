import time
from machine import Pin
import HC_SR04

pwm = PWM(Pin(16))
pwm.duty_u16(10000)

trig = Pin(10, Pin.OUT)
echo = Pin(4, Pin.IN)

distance = round(ping()/58)
while distance <= 15 :
    for duty in range(600,5000,200):
        pwm.freq(3000)
        
def ping():
    trig.value(1)
    time.sleep_us(10)
    trig.value(0)
    count = 0
    timeout = False
    start = time.ticks_us()
    while not echo.value():
        time.sleep_us(10)
        count+=1
        if count > 100000:
            timeout = True
            break


