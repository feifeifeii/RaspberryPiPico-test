from machine import Pin, PWM
import time
from time import sleep
servoXPin = PWM(Pin(16))
servoYPin = PWM(Pin(17))
servoXPin.freq(50)
servoYPin.freq(50)

x=machine.ADC(26)
y=machine.ADC(28)

time.sleep(0.01)
x_zero = x.read_u16()/400
y_zero = y.read_u16()/400


def servo(degrees):
    if degrees > 180: degrees = 180
    if degrees < 0: degrees = 0
    maxDuty = 9000 
    minDuty = 1000 
    newDuty = minDuty+(maxDuty-minDuty)*(degrees/180)
    servoXPin.duty_u16(int(newDuty))
    servoYPin.duty_u16(int(newDuty))
    return newDuty

while True:
    reading=x.read_u16()
    x_data = round(x_zero-reading/400)
    
    print('X= ',x_data)
    if x_data > 5 or x_data < -5:
        for degree in range(0, 180, 1):
            servo(degree)
            sleep(0.01) 
    
    reading=y.read_u16()
    y_data = round(y_zero-reading/400)
    
    print('Y= ',y_data)
    if y_data < -5 or y_data > 5:
        for degree in range(0, 180, 1):
            servo(degree)
            sleep(0.01)
    time.sleep(0.01)
