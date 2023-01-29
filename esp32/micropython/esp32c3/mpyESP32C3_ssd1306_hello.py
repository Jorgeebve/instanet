"""
MicroPython/ESP32C3 exercise run on ESP32-C3-DevKitM-1,
work with SSD1306 I2C OLED.
And,catch exception of ENODEV.

"""
import uos
import usys
import machine
import time
import ssd1306
from machine import I2C

print("====================================")
print(usys.implementation[0], uos.uname()[3],
      "\nrun on", uos.uname()[4])
print("====================================")

scl = machine.Pin(6, machine.Pin.OUT, machine.Pin.PULL_UP)
sda = machine.Pin(5, machine.Pin.OUT, machine.Pin.PULL_UP)
oled_i2c = machine.I2C(0, scl=scl, sda=sda, freq=400000)

oled_i2c = machine.I2C(0)
print("Default I2C:", oled_i2c)
"""
oled_ssd1306 = ssd1306.SSD1306_I2C(128, 64, oled_i2c)
print("Default SSD1306 I2C address:",
          oled_ssd1306.addr, "/", hex(oled_ssd1306.addr))
oled_ssd1306.text('Hello, World!', 0, 0, 1)
oled_ssd1306.show()

"""
try:
    oled_ssd1306 = ssd1306.SSD1306_I2C(128, 64, oled_i2c)
    print("Default SSD1306 I2C address:",
          oled_ssd1306.addr, "/", hex(oled_ssd1306.addr))
    oled_ssd1306.text('Hello, World!', 0, 0, 1)
    oled_ssd1306.show()
except OSError as exc:
    print("OSError!", exc)
    if exc.errno == errno.ENODEV:
        print("No such device")

print("~ bye ~")