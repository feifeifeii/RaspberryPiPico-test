from machine import Pin, PWM, I2C, UART, ADC
from time import sleep

pin_led = machine.Pin(25, machine.Pin.OUT)
i2c = I2C(0, sda = Pin(12), scl = Pin(13), freq = 100000)
#I2C.start()
print('Scan i2C bus...')
devices = i2c.scan()

if len(devices) == 0:
    print('No i2c device!')
else:
    print('i2c device found:', len(devices))
    
for device in devices:
    print('Decimal address:', device, '| Hexa address:', hex(device))