from machine import Pin, PWM
from time import sleep

servoPin = PWM(Pin(16))
servoPin.freq(50) #50Hz(20msec...定值，超過會亂動)

def servo(degrees):
    if degrees > 180: degrees = 180
    if degrees < 0: degrees = 0
    #20ms/65535 = 0.0003
    maxDuty = 9000 #9000: 0.0003 x 9000 = 0.9ms
    minDuty = 1000 #1000: 0.0003 x 1000 = 0.3ms
    newDuty = minDuty+(maxDuty-minDuty)*(degrees/180)
    servoPin.duty_u16(int(newDuty))
    
while True:
    for degree in range(0, 180, 1):
        servo(degree)
        sleep(0.01)