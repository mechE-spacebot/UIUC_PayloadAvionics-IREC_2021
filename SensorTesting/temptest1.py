#temptest1.py
#-----------------------------------------------------------------------------------------------------
#Program will simply display RTC Temperature and initialize RTC time to zero.
#-----------------------------------------------------------------------------------------------------
#Acceleration/Gyro Sensor : adafruit LSM6DSOX
#RTC Module : adafruit DS3231
#-----------------------------------------------------------------------------------------------------
#Coded by : Nicholas P. Shay, Mechanical Engineering 2022, npshay2@illinois.edu
#Date : 12/5/2020
#-----------------------------------------------------------------------------------------------------
import time                                    #Library for debugging and buffering
import csv                                     #Library to write data into csv file
import board                                   #Library for CircuitPi to get board info
import busio                                   #Library for CircuitPi bus communication
from adafruit_lsm6ds.lsm6dsox import LSM6DSOX  #Library for CircuitPi accel/gyrosensor
import adafruit_ds3231                         #Library for CircuitPi RTC

i2c = busio.I2C(board.SCL, board.SDA)         #Define i2c connection with circuitPi busio
sox = LSM6DSOX(i2c)                           #Define acceleration sensor for data
ds3231 = adafruit_ds3231.DS3231(i2c)          #Define RTC module for timing

for i in range(1, 10):
    t_RTC = ds3231.temperature
    print(t_RTC)
    time.sleep(1)
t = time.struct_time((2020,12,12,00,00,00,0,-1,-1))                                             #Set RTC Clock to 0 hr/min/s before starting data collection
ds3231.datetime = t
print("Success, time is:",t)            #Used for debugging RTC clockset
print()                                 #Used for debugging RTC clockset