import machine
import time
import math

sensor_temp = machine.ADC(4)
conversion_factor = 3.3/65535

while True:
    reading = sensor_temp.read_u16()*conversion_factor
    temp = round(27-(reading-0.706)/0.001721,2)
    print(temp)
    time.sleep(0.1)
    