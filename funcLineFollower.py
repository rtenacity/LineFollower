from ev3dev2.motor import OUTPUT_B, OUTPUT_C, MoveTank, SpeedPercent, follow_for_ms
from ev3dev2.sensor.lego import ColorSensor
from time import sleep
import sys
from ev3dev2.button import *
import csv
tank = MoveTank(OUTPUT_B, OUTPUT_C)
tank.cs = ColorSensor()
col= ColorSensor()
col.mode = 'COL-REFLECT'
btn = Button()

konstantP = 1
konstantI = 0
konstantD = 0
kSpeed = 15
kms = 15

tank = MoveTank(OUTPUT_B, OUTPUT_C)
tank.cs = ColorSensor()

print("start!")
while True:
    tank.stop()
    if btn.right:
        tank.stop()
        print("Reading file and starting")
        f = open("pid.csv")
        for row in csv.reader(f):
            konstantP = float(row[0])
            konstantI = float(row[1])
            konstantD = float(row[2])
            kSpeed = int(row[3])
            kms = int(row[4])
            print(str(konstantP)+ " " + str(konstantI)+ " " + str(konstantD)+ " " + str(kSpeed)+ " " + str(kms))
        tank.follow_line(kp=konstantP, ki=konstantI, kd=konstantD, speed=SpeedPercent(kSpeed), 
        follow_left_edge=True, target_light_intensity=55, white=100, off_line_count_max=1000, sleep_time=0.01, 
        follow_for=follow_for_ms, ms=kms)