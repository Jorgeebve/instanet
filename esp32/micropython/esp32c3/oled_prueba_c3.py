# Display DHT22 readings in 0.96 OLED display
# Date: October 1, 2020

# Import the machine module to access the pins
import machine
# Import the time module for the intervals
import time
# OLED display initializations
import ssd1306

scl = machine.Pin(6, machine.Pin.OUT, machine.Pin.PULL_UP)
sda = machine.Pin(5, machine.Pin.OUT, machine.Pin.PULL_UP)
i2c = machine.I2C(0, scl=scl, sda=sda, freq=400000)
print("Default I2C:", i2c)
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

print("Default SSD1306 I2C address:", oled, "/", hex(oled.addr))

oled.text('Hola, Mundo!', 0, 0, 1)
oled.show()

