from nec import NEC_16

from machine import Timer

from machine import Pin

  

led = Pin(15, Pin.OUT)
_data = 0
def callBack(data, addr, ctrl):

    global _data, _addr

    _data = ir_key[data]

    _addr = addr

    if data > 0:

        #print("data: {:02x} addr: {:04x}".format(data, addr))

        print(_data)
        if _data == "1":

            led.on()
            print('on')

        elif _data == "2":

            led.off()
            print('off')

ir = NEC_16(Pin(28, Pin.IN), callBack)

  

ir_key = {

    0x45: '1',
    0x46: '2',
    0x47: '3',
    0x44: '4',
    0x40: '5',
    0x43: '6',
    0x07: '7',
    0x15: '8',
    0x09: '9',
    0x16: '*',
    0x19: '0',
    0x0D: '#',
    0x0C: '1',
    0x18: 'UP',
    0x5E: '3',
    0x08: 'LEFT',
    0x1C: 'OK',
    0x5A: 'RIGHT',
    0x42: '7',
    0x52: 'DOWN',
    0x4A: '9'    
}

