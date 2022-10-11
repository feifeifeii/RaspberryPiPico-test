
import machine
import utime
pin_led = machine.Pin(25,machine.Pin.OUT)

uart0 = machine.UART(0,baudrate=115200)  #at-command

def sendCMD_waitResp(cmd, uart=uart0, timeout=100):
    pin_led.on()
    sleep(0.1)
    uart.write(cmd)


    
def waitResp(uart=uart0, timeout=100):
    global data
    prvMills = utime.ticks_ms()
    resp = b""
    while (utime.ticks_ms()-prvMills)<timeout:
        if uart.any():
            pin_led.off()
            sleep(0.1)
            
print(uart0)
print("- uart0 -")
sendCMD_waitResp("start\r\n")

while True :
    waitResp()
    sendCMD_waitResp('123\r\n')
    utime.sleep(1)
