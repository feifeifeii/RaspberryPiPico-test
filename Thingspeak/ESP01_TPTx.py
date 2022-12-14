from machine import Pin, PWM, I2C, UART, ADC
import os, sys
import utime
import machine

print(os.uname())

sensor_temp=machine.ADC(4)
conversion_factor = 3.3 / 65535
lens = len('GET /update?api_key=WZMTYXRRK1GIBTDM&field1="+temp+"\r\n')
Len = str(lens)
print(lens)
utime.sleep(1)
#functions
def sendCMD_waitResp(cmd, timeout=2000):
    print("CMD: " + cmd)
    uart.write(cmd.encode('utf-8'))
    waitResp(timeout)
    print()
    
def waitResp(timeout=20000):
    prvMills = utime.ticks_ms()
    resp = b""
    while (utime.ticks_ms()-prvMills) < timeout:
        if uart.any():
            resp = b"".join([resp, uart.read(1)])
    print(resp)
    
#print uart info
uart = machine.UART(1,tx=Pin(8),rx=Pin(9),baudrate=115200)
print(uart)
#waitResp() 
sendCMD_waitResp("AT+RST\r\n") #reset the esp8266

sendCMD_waitResp("AT+CWMODE=1\r\n")   #set wifi mode 1:client 2:AP 3: Both

sendCMD_waitResp('AT+CWJAP="FC\'s Galaxy A51","eydg8183"\r\n', 5000) #connecting

sendCMD_waitResp("AT+CIPMUX=0\r\n")  # multi user

print("RPi-PICO with ESP-01")
while True:
    reading=sensor_temp.read_u16() * conversion_factor
    temp = round(27 - (reading - 0.706)/0.00721, 1)
    print(temp)
    temp=str(temp)
    sendCMD_waitResp('AT+CIPSTART="TCP","184.106.153.149",80\r\n',500)
    sendCMD_waitResp("AT+CIPSEND="+Len+"\r\n",500)
    sendCMD_waitResp("GET /update?api_key=WZMTYXRRK1GIBTDM&field1="+temp+"\r\n")
    sendCMD_waitResp("AT+CIPCLOSE\r\n")
    utime.sleep(5)

sendCMD_waitResp("AT+CIPCLOSE=0\r\n")