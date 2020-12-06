import time
import board
import busio
from adafruit_lsm6ds.lsm6dsox import LSM6DSOX

i2c = busio.I2C(board.SCL, board.SDA)
sox = LSM6DSOX(i2c)

while True:
    print("Acceleration: X:%.2f, Y:%.2f, Z:%.2f m/s^2" % (sox.acceleration))
    #print("Gryo: x:%.2f, y:%.2f, z:%.2f degrees/s" % (sox.gyro))
    print("")
    time.sleep(0.5)