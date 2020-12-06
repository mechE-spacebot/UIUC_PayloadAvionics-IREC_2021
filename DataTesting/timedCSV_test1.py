import time
import csv
import board
import busio
from adafruit_lsm6ds.lsm6dsox import LSM6DSOX
import adafruit_ds3231

i2c = busio.I2C(board.SCL, board.SDA)
sox = LSM6DSOX(i2c)
ds3231 = adafruit_ds3231.DS3231(i2c)

if True:
    t = time.struct_time((2020,12,12,00,00,00,0,-1,-1))
    ds3231.datetime = t
    print("Success, time is:",t)
    print()
    
with open('accel_test1.csv', 'w', newline='') as f:
    writing = csv.writer(f)
    writing.writerow(['Time', '--X--', '--Y--', '--Z--'])
    for i in range(1,100):
        t = ds3231.datetime
        stmpdata = ("T+ {}:{:02}:{:02}".format(t.tm_hour, t.tm_min, t.tm_sec), "%.2f, %.2f, %.2f" % (sox.acceleration))
        writing.writerow(stmpdata)
        time.sleep(0.1)
        i = 1+i
f.close()
