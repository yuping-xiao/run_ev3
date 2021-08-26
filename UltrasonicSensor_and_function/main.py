#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

# Write your program here
""" brick.sound.beep()
 """

# STEP2:コードを書いてみよう
""" 
def beep_disp(value, tune): #関数「beep_disp」を使えるようにする（定義する）
    brick.display.text(value,(80,60)) #引数「value」の値を表示
    wait(1000)
    brick.display.clear()
    brick.sound.beep(tune, 1000, 20) #(周波数Hz, ミリ秒ms, 音量%)

text = "abcdefg"
num = 1234567
pitch_high = 1000
pitch_low = 100

beep_disp(text, pitch_high) #関数の呼び出し（１回目：textを引数にあたえる）
beep_disp(num, pitch_low) #関数の呼び出し（２回目：numを引数にあたえる）
beep_disp(text, pitch_high)
 """

# mission challenge
""" 
left = Motor(Port.B) #ロボットを動かす準備
right = Motor(Port.C) #ロボットを動かす準備
robot = DriveBase(left, right, 56, 55)

def forward_drive(pow, time): #関数「drive_def」を使えるようにする（定義）
    robot.drive_time(pow, 0, time)
    brick.sound.beep()
    robot.stop()

go = 1000
back = -1000
long = 5000
short = 500

forward_drive(back, long) 
"""

# STEP2:コードを書いてみよう
""" 
brick.light(Color.ORANGE) # オレンジ色に点灯
wait(2000)

brick.light(Color.GREEN) # 緑色に点灯
wait(2000)

brick.light(Color.RED) # 赤色に点灯
wait(2000)

brick.light(None)
wait(2000)
 """

# mission challenge
""" 
while True:
    brick.light(Color.RED)
    wait(1000)
    brick.light(None)
    wait(1000)
    brick.light(Color.GREEN)
    wait(1000)
    brick.light(None)
    wait(1000)
     """

# STEP2:コードを書いてみよう
ultrasonic_sensor = UltrasonicSensor(Port.S4) # 超音波ｾﾝｻｰを使えるようにする

while True: # 無限に繰り返す
    if ultrasonic_sensor.distance() < 50: # 5cm以下になったら
        for i in range(3): # 3回繰り返す
            brick.sound.beep()
            brick.light(Color.RED)
            wait(2000)
            brick.light(None)
            wait(2000)
    else:
        brick.light(None)
        
