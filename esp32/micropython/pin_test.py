import time
from machine import Pin

pin = Pin(2, Pin.OUT)
while True:
    pin.on()
    time.sleep_ms(500)
    pin.off()
    time.sleep_ms(500)

