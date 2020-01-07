from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

class WheelchairLady:
    def  __init__(self, robot):
       self.robot=robot
    def run(self):
        # self.robot.turnleft(10,25)
        # self.robot.forward(50,4)
        # self.robot.DogGearA(20,0.3,-1)
        # self.robot.forward(40,0.05)
        # self.robot.DogGearA(20,0.3,1)
        # self.robot.forward(50,2.5)
        # self.robot.turnright(20,30)html/

        # self.robot.driveStraight(200,8,0)

        self.robot.resetGyro()
        self.robot.reset()
        self.robot.DogGearHold(0,0,-1)
        self.robot.driveStraight(200,0.2,0)
        self.robot.findLine(20,Color.BLACK,1)
        self.robot.backward(20,.018)
        self.robot.turnright(10,90)
        self.robot.driveStraight(200,3.3,90)

        # self.robot.DogGearHold(0,0,-1)
        # self.robot.forward(50,4)
        self.robot.DogGearA(15,0.25,-1)
        self.robot.forward(20,0.2)
        self.robot.DogGearA(20,0.3,1)
        self.robot.driveStraight(200,.7,90)
        self.robot.findLine(20,Color.WHITE,2)
        self.robot.findLine(20,Color.BLACK,2)
        self.robot.turnLeftNoReset(10,26)
        self.robot.driveStraight(200,2.18,25)
    
        self.robot.backward(20,.2)
        self.robot.DogGearHold(15,0.15,-1)
        self.robot.backward(15,0.2)
        self.robot.findLine(-20,Color.WHITE,1)
        self.robot.turnright(10,59)
        self.robot.driveStraight(200,1.5,58)
        self.robot.DogGearHold(15,.01,-1)
        self.robot.backward(20,1.5)
        self.robot.findLine(-20,Color.WHITE,1)
        self.robot.findLine(-20,Color.BLACK,1)
        self.robot.turnLeftNoReset(10,0)
        self.robot.Align(20)

       
      
        

        # self.robot.turnright(10,10)
        # self.robot.forward(20,0.2)
        # self.robot.DogGearHold(10,0.05 ,-1)
        # self.robot.turnright(10,60)

        # self.robot.forward(100,3)
    