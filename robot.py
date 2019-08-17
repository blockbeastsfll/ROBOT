
from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

class Robot:
    def __init__(self,motorA,motorB,motorC,motorD,sensor1,sensor2,sensor3,sensor4):
        self.motorA = motorA
        self.motorB=motorB
        self.motorC=motorC
        self.motorD=motorD
        self.sensor1=sensor1
        self.sensor2=sensor2
        self.sensor3=sensor3
        self.sensor4=sensor4

    def forward(self,speed,distance):
        self.motorB.run(speed)
        self.motorC.run(speed)
        while self.motorC() < distance:
            wait(10)
        self.motorB.run(0)
        self.motorC.run(0)