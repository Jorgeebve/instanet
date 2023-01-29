import uos
import usys
import machine
import time
import ssd1306

scl = machine.Pin(6, machine.Pin.OUT, machine.Pin.PULL_UP)
sda = machine.Pin(5, machine.Pin.OUT, machine.Pin.PULL_UP)


# Read and display /boot.py file
def readBoot():
    print("========================")
    fileBoot = "/boot.py"
    print(fileBoot)
    print("========================")
    with open(fileBoot, "r") as f:
        line = f.readline()
        while line != '':
            line = line.rstrip() #strip trailing whitespace
            print(line)
            oled_ssd1306.scroll(0, -10)
            oled_ssd1306.text(line, 0, 46, 1)
            oled_ssd1306.show()
            time.sleep(0.5)
            line = f.readline()
    print("========================")

print("====================================")
print(usys.implementation[0], uos.uname()[3],
      "\nrun on", uos.uname()[4])
print("====================================")

oled_i2c = machine.I2C(0, scl=scl, sda=sda, freq=400000)
print("Default I2C:", oled_i2c)

oled_ssd1306 = ssd1306.SSD1306_I2C(128, 64, oled_i2c)
print("Default SSD1306 I2C address:",
          oled_ssd1306.addr, "/", hex(oled_ssd1306.addr))
oled_ssd1306.text('Hello, World!', 0, 0, 1)
oled_ssd1306.show()

readBoot()

print("~ bye ~")