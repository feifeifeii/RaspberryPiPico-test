import array, time
from machine import Pin
from time import sleep
#import rp2
 
# Configure the number of WS2812 LEDs, pins and brightness.
NUM_LEDS = 8
PIN_NUM = 28
brightness = 1


@rp2.asm_pio(sideset_init=rp2.PIO.OUT_LOW, out_shiftdir=rp2.PIO.SHIFT_LEFT, autopull=True, pull_thresh=24)
def ws2812():
    T1 = 2
    T2 = 5
    T3 = 3
    wrap_target()
    label("bitloop")
    out(x, 1).side(0)[2]
    jmp(not_x, "do_zero").side(1)[1]
    jmp("bitloop").side(1)[4]
    label("do_zero")
    nop().side(0)[4]
  
# Create the StateMachine with the ws2812 program, outputting on Pin(28).#wrap()  
sm = rp2.StateMachine(0, ws2812, freq=8000000, sideset_base=Pin(PIN_NUM))
 
# Start the StateMachine, it will wait for data on its FIFO.
sm.active(1)
 
# Display a pattern on the LEDs via an array of LED RGB values.
ar = array.array("I", [0 for _ in range(NUM_LEDS)])
 
def pixels_show(br):
    dimmer_ar = array.array("I", [0 for _ in range(NUM_LEDS)])
    for i,c in enumerate(ar):  #enumerate
        r = int(((c >> 8) & 0xFF) * br)
        g = int(((c >> 16) & 0xFF) * br)
        b = int((c & 0xFF) * br)
        dimmer_ar[i] = (g<<16) + (r<<8) + b
    sm.put(dimmer_ar, 8)
    time.sleep_ms(10)

def pixels_set(i, color):
    ar[i] = (color[1]<<16) + (color[0]<<8) + color[2]

BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
WHITE = (255, 255, 255)
COLORS = (BLACK, RED, YELLOW, GREEN, CYAN, BLUE, PURPLE, WHITE)


while True:
    for i in range(NUM_LEDS):
        print(i)
        pixels_set(i, GREEN)
        pixels_show(0.01) 
        time.sleep(0.1)
    for i in range(NUM_LEDS):
        print(i)
        pixels_set(i, BLACK)
        pixels_show(0.01) 
        time.sleep(0.1)
        pixels_set(i, BLACK)
        pixels_show(0.01) 
        time.sleep(0.1)
    pixels_set(i, BLACK)
    pixels_show(1) 
    pixels_set(4, YELLOW)
    pixels_set(5, RED)
    pixels_set(6, YELLOW)
    pixels_set(7, RED)
    pixels_show(0.01)
    sleep(1)
    pixels_set(7, BLACK)
    pixels_set(6, BLACK)
    pixels_set(5, BLACK)
    pixels_set(4, BLACK)
    pixels_show(1) 
    
