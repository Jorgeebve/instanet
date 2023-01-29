"""
MicroPython/ESP32C3 exercise run on ESP32-C3-DevKitM-1,
work with SSD1306 I2C OLED.
HelloWorld! with something.

"""
import uos
import usys
import machine
import time
import ssd1306

print("====================================")
print(usys.implementation[0], uos.uname()[3],
      "\nrun on", uos.uname()[4])
print("====================================")

oled_i2c = machine.I2C(0)
print("Default I2C:", oled_i2c)
