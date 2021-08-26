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