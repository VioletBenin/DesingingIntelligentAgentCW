# import random

class coordinate_2d:
    def __init__(self,x,y):
        self.x=x
        self.y=y

class Vehicle:
    def __init__(self,coordinate_2d,canvasp):
        self.coordinate_2d=coordinate_2d
        self.canvasp=canvasp

class TrafficLight:
    def __init__(self,coordinate_2d,canvasp):
        self.coordinate_2d=coordinate_2d
        self.canvasp=canvasp
