import busio
import board
import adafruit_ds3231
import time

i2c = busio.I2C(board.SCL, board.SDA)
ds3231 = adafruit_ds3231.DS3231(i2c)

if True:
    t = time.struct_time((2020,12,12,00,00,00,0,-1,-1))
    ds3231.datetime = t
    print("Success, time is:",t)
    print()

while True:
    t = ds3231.datetime
    print("T+ {}:{:02}:{:02}".format(t.tm_hour, t.tm_min, t.tm_sec))
    time.sleep(0.1)
