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

scl = machine.Pin(6, machine.Pin.OUT, machine.Pin.PULL_UP)
sda = machine.Pin(5, machine.Pin.OUT, machine.Pin.PULL_UP)
oled_i2c = machine.I2C(0, scl=scl, sda=sda, freq=400000)

print("Default I2C:", oled_i2c)

oled_ssd1306 = ssd1306.SSD1306_I2C(128, 64, oled_i2c)
print("Default SSD1306 I2C address:",
      oled_ssd1306.addr, "/", hex(oled_ssd1306.addr))

oled_ssd1306.fill(1)    #all on
oled_ssd1306.show()
time.sleep(1)
oled_ssd1306.fill(0)    #all off
oled_ssd1306.show()
time.sleep(1)

def splitLine(src, cnt):
    return [src[i:i+cnt] for i in range(0, len(src), cnt)]

oled_ssd1306.text('Hello, World!', 0, 0, 1)
oled_ssd1306.text(str(usys.implementation[0]), 0, 20, 1)
oled_ssd1306.text(str(uos.uname()[2]), 0, 30, 1)

line_y = 40
for l in splitLine(str(uos.uname()[4]), 15):
    oled_ssd1306.text(l, 0, line_y, 1)
    line_y += 10

oled_ssd1306.show()
time.sleep(1)

oled_ssd1306.invert(1)
oled_ssd1306.show()
time.sleep(0.5)
oled_ssd1306.invert(0)
oled_ssd1306.show()
time.sleep(0.5)

oled_ssd1306.rect(15, 15, oled_ssd1306.width-30,
                  oled_ssd1306.height-30, 1)
oled_ssd1306.show()
time.sleep(1)

for x in range(oled_ssd1306.width):
    oled_ssd1306.scroll(1, 0)
    oled_ssd1306.show()
    time.sleep_ms(50)

oled_ssd1306.fill_rect(15, 15, oled_ssd1306.width-30,
                  oled_ssd1306.height-30, 1)
oled_ssd1306.show()
time.sleep(0.5)
oled_ssd1306.text('~ bye ~', 55, 55, 1)
oled_ssd1306.show()
time.sleep(0.5)

print("~ bye ~")
