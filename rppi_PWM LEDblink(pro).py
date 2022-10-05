from machine import Pin
from time import sleep
pin_led0 = machine.Pin(14, machine.Pin.OUT)
pin_led1 = machine.Pin(15, machine.Pin.OUT)
pin_led2 = machine.Pin(25, machine.Pin.OUT)
button = machine.Pin(11, machine.Pin.IN, machine.Pin.PULL_UP)
sw_time = 0.1
x=0
y=0

pin_led0.value(0)
pin_led1.value(0)
pin_led2.value(0)

Leds = ['pin_led2','pin_led0','pin_led1']

def int_handler(pin):
    global x
    global y
    button.irq(handler=None)
    print("Interrupt Detected!")
    y=1
    x+=1
    if x >= 2:
        x=0
    while button.value() == 0:
        sleep(0.1)
    button.irq(handler=int_handler)

def Delay(T):
    global y
    for i in range (T):
        sleep(0.01)
        if y==1 :
            break
button.irq(trigger=Pin.IRQ_FALLING, handler=int_handler)
    
while True:
    if x == 0:
        for k in range(0,3):
            s = eval(Leds[k%3])
            s.toggle()
            sleep(sw_time)
    else:
        pin_led0.value(0)
        pin_led1.value(0)
        pin_led2.value(0)
        

            
