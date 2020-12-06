import time
import csv
import board
import busio
from adafruit_lsm6ds.lsm6dsox import LSM6DSOX

i2c = busio.I2C(board.SCL, board.SDA)
sox = LSM6DSOX(i2c)

with open('accel_test1.csv', 'w', newline='') as f:
    writing = csv.writer(f)
    writing.writerow(['Time', '--X--', '--Y--', '--Z--'])
    start = time.time()
    for i in range(1,10):
        end = time.time()
        stmpdata = (sox.acceleration)
        writing.writerow(stmpdata)
        time.sleep(0.1)
        i = 1+i
f.close()