from machine import Pin, I2C, UART, ADC
from ssd1306 import SSD1306_I2C
import time

comm=machine.UART(1,115200)
uart=UART(0,tx=Pin(0),rx=Pin(1))

i2C=I2C(0,sda=Pin(12),scl=Pin(13),freq=40000)
oled=SSD1306_I2C(128,32,i2C)
oled.fill(0)
for i in range(0,11,1):
    disp = str(i)
    oled.text(disp,10,12)
    oled.show()
    time.sleep(0.5)
    oled.fill(0)


oled.text("IT Training",10,12)  


oled.show()