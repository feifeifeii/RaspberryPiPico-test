import machine
from time import sleep
button = machine.Pin(28,machine.Pin.IN)
pin_led = machine.Pin(25,machine.Pin.OUT)#主板槽位25
pin_led1 = machine.Pin(14,machine.Pin.OUT)#擴充槽位14
pin_led2 = machine.Pin(15,machine.Pin.OUT)#擴充槽位15
x=0

while True:
    if button.value() == 0:
        x=1 #只閃一輪
        for i in range(x):
            pin_led.on()
            sleep(0.1)
            pin_led1.on()
            sleep(0.1)
            pin_led2.on()
            sleep(0.1)
            pin_led.off()
            sleep(0.1)
            pin_led1.off()
            sleep(0.1)
            pin_led2.off()
            sleep(0.1)
            
            pin_led2.on()
            sleep(0.1)
            pin_led1.on()
            sleep(0.1)
            pin_led.on()
            sleep(0.1)
            pin_led2.off()
            sleep(0.1)
            pin_led1.off()
            sleep(0.1)
            pin_led.off()
            sleep(0.1)
            
        else:
            pin_led.off()
            sleep(0.1)