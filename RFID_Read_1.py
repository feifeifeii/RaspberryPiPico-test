from mfrc522 import MFRC522
from machine import Pin
from machine import Pin, PWM
import utime

import tm1637
from time import sleep_ms,sleep

tm = tm1637.TM1637(clk=Pin(13), dio=Pin(12))

green_led = Pin(25, Pin.OUT) 
red_led  = Pin(15, Pin.OUT)

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
    
# 將卡號由 2 進位轉換為 16 進位的字串
def uidToString(uid):
    mystring = ""
    for i in uid:
        mystring = "%02X" % i + mystring
    return mystring
              
reader = MFRC522(spi_id=0,sck=2,miso=4,mosi=3,cs=26,rst=10)
print("..... 請將卡片靠近感應器.....")

try:
    while True:
        (stat, tag_type) = reader.request(reader.REQIDL)   # 搜尋 RFID 卡片
        if stat == reader.OK:      # 找到卡片
            (stat, uid) = reader.SelectTagSN()
            if stat == reader.OK:
                card_num = uidToString(uid)
                print(".....卡片號碼： %s" % card_num)
                if  card_num == '202E30A0':#'7A811D60':
                    tm.write([0b00000000, 0b00111101, 0b00111111, 0b00000000])
                    for degree in range(0, 180, 1):
                        servo(degree)
                        sleep(0.01)
                    print('....Welcome....')
                    green_led.value(1)   # 讀到授權的卡號後點亮綠色 LED
                    utime.sleep(2)       # 亮 2 秒鐘
                    green_led.value(0)

                else:
                    tm.write([0b01101101, 0b01110100, 0b00000110, 0b01111000])
                    print(".....卡片錯誤.....")
                    red_led.value(1)    # 讀到非授權的卡號後點亮紅色 LED
                    utime.sleep(2)      # 亮 2 秒鐘
                    red_led.value(0)
            else:
                print(".....授權錯誤.....")

except KeyboardInterrupt:
    print(".....Bye.....")