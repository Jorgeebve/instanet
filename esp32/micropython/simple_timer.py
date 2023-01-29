import machine
from machine import Pin

led = Pin(19, Pin.OUT)

tim0 = machine.Timer(0)

def handle_callback(timer):
    led.value(not led.value())
    
tim0.init(period=500, mode=machine.Timer.PERIODIC, callback = handle_callback)