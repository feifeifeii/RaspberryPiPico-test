from machine import Pin, PWM
from time import sleep

pwm = PWM(Pin(14))
pwm1 = PWM(Pin(15))
pwm2 = PWM(Pin(25))
pwm.freq(50)

while True:
    for duty in range(1000,20000,1):
        pwm.duty_u16(duty)
        sleep(0.0001)
        pwm1.duty_u16(duty)
        sleep(0.0001)
        pwm2.duty_u16(duty)
        sleep(0.0001)
    sleep(0.3)
    for duty in range(20000,1000,-1):
        pwm.duty_u16(duty)
        sleep(0.0001)
        pwm1.duty_u16(duty)
        sleep(0.0001)
        pwm2.duty_u16(duty)
        sleep(0.0001)
    sleep(0.3)