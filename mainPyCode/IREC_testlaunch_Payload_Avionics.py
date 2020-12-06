#IREC_testlaunch_Payload_Avionics.py
#-----------------------------------------------------------------------------------------------------
#Program will record timestamped acceleration, temperature, and gyroscope data to a csv file for post processing.
#Will run when power is connected to unit on boot sequence.
#-----------------------------------------------------------------------------------------------------
#Raspberry Pi 2B v1.1 terminal command: sudo python3 /home/pi/IREC_testlaunch_Payload_Avionics.py
#To initiate program into boot sequence:
#                              1) Open terminal and run : sudo nano /home/pi/.bashrc
#                              2) Add at end of script following code:
#                                         echo Running Program
#                                         sudo python3 /home/pi/IREC_testlaunch_Payload_Avionics.py
#                              3)Ctrl+X to exit, save changes, and reboot!
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
    
with open('accel_test2.csv', 'w', newline='') as f:     #Create .csv file and define
    writing = csv.writer(f)                             #Open writing connection with csv file
    writing.writerow(['Time', 'Temperature', '--a_x--', '--a_y--', '--a_z--', '--g_x--', '--g_y--', '--g_z--'])    #Write Headers to each column
    t = time.struct_time((2020,12,12,00,00,00,0,-1,-1))                                             #Set t to zero time for RCT initialization
    ds3231.datetime = t                      #Set RTC Clock to 0 hr/min/s before starting data collection
    #print("Success, time is:",t)            #Used for debugging RTC clockset
    #print()                                 #Used for debugging RTC clockset
    
    for i in range(1,100):
        (a_x, a_y, a_z) = sox.acceleration   #Unpack LSM6DSOX acceleration data
        (g_x, g_y, g_z) = sox.gyro           #Unpack LSM6DSOX gyroscope data
        t_RTC = ds3231.temperature           #Define t_RTC ad current RTC temperature
        t = ds3231.datetime                  #Define t as current RTC time
        stmpdata = ("T+ {}:{:02}:{:02}".format(t.tm_hour, t.tm_min, t.tm_sec), t_RTC, a_x, a_y, a_z, g_x, g_y, g_z)  #Write following data into tuple: RTC time, accel x, accel y, accel z, gyro x, gyro y, gyro z
        writing.writerow(stmpdata)           #Write tuple into .csv file
        time.sleep(0.1)                      #Sleep
f.close()                                    #Close .csv file to save data and end program
