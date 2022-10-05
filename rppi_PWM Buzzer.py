from machine import Pin, PWM
from time import sleep

pwm = PWM(Pin(16))
pin_led = machine.Pin(25, machine.Pin.OUT)
pwm.duty_u16(10000)

while True:
    for duty in range(600,5000,200):
        pwm.freq(3000)
        sleep(1)
        pwm.deinit()
        sleep(1)