"""class Thing:
    self.position= None
    def display(self , canvas, x, y, width, heigth):
        pass
    def position(self):
        return self.position

class car(Thing):
    self.position=None
    self.behaviour=None
    def __init__(behaviour):
        self.behaviour=behaviour
    def setPosition(position):
        self.position=position"""
from enum import Enum;
import random;
import time;
from tkinter import *
from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool

class Park(Enum):
  BUSY= True
  FREE= False
  def getPark(boolean):
    if boolean==True:
      return Park.BUSY
    else:
      return Park.FREE

class Agent:
    x=0
    y=0
    def __init__(self,environment,presenceSensor):
        self.perceptions= {}
        self.environment=environment
        self.presenceSensor=presenceSensor

    """a ideia aqui é ter um dicionario com chaves representando as percepções e ele vá agindo perante a elas"""
    def actuate(self):
        for e in self.perceptions:
            if self.perceptions[e]==self.environment.getState(e):
                del(self.perceptions[e])
                pass
            else:
                self.environment.setState(e,self.perceptions[e])
                del(self.perceptions[e])
    def percept(self):
        self.perceptions=self.presenceSensor.getInformation()

class presenceSensor:
    def __init__(self,environment):
        self.environment=environment
        self.information = environment.park.copy()
        self.informationChange = {}

    def updateinformationChange(self):
        for e in self.environment.park:
            if e in self.informationChange and self.information[e]==self.environment.park[e]:
                del(self.informationChange[e])
            elif self.information[e] != self.environment.park[e]:
                self.updateInformation()
                self.informationChange[e]=self.information[e]

    def getinformationChange(self):
        return self.informationChange
    def updateInformation(self):
        self.information=self.environment.park.copy()

    def getInformation(self):
        self.updateInformation()
        return print(self.information)


class Environment:
  def __init__(self):
    self.things = []
    self.park= {0:"FREE",1:"BUSY",2:"FREE",3:"BUSY"}
  def setState(self,index,state):
    self.park[index]=state
  def getState(self,index):
    return self.park[index]

Environment1=Environment()
presenceSensor1=presenceSensor(Environment1)
Agent1=Agent(Environment1,presenceSensor1)
Environment1.setState(0,"BUSY")


class carBehaviour():
  def __init__(self,environment):
    self.environment=environment
  def randomPark(self):
    return random.randint(0,3)
  def goPark(self,carNumber):
    randomParkBehaviour=self.randomPark()
    while (self.environment.park[randomParkBehaviour]==Park.BUSY.name):
      time.sleep(2)
      randomParkBehaviour=self.randomPark()
    self.environment.park[randomParkBehaviour]=Park.BUSY.name
    return randomParkBehaviour
  def leavePark(self,position):
    time.sleep(2)
    self.environment.park[position]=Park.FREE.name


class car(carBehaviour):
    def __init__(self,carNumber,environment):
      super().__init__(environment)
      self.carNumber=carNumber
      self.position= None
    def setPosition(self,position):
      self.position=position
    def getPosition(self):
      return self.position
    def getcarNumber(self):
      return self.carNumber
    """def parking(self):"""
    def cargoPark(self):
      self.position=self.goPark(self.carNumber)
    def carleavePark(self):
      self.leavePark(self.position)
      self.setPosition(None)

    
def EnvironmentSimulate(seconds,Environment,canvas,vectorPark):
  for x in range(0,4):
    carsNumbers.append("car"+str(x))
  Car0=car(carsNumber[0],Environment)
  Car1=car(carsNumbers[1],Environment)
  Car2=car(carsNumber[0],Environment)
  Car3=car(carsNumbers[1],Environment)
  carObjects=[Car0,Car1,Car2,Car3]
   print("Car going parking \n")
  canvas.update()
  for car in carObjects:
    car.cargoPark()
    print("Car parked ",car.getPosition())
    canvas.itemconfig(vectorPark[car.getPosition()],fill="red")
    canvas.update()
    time.sleep(random.randint(0,3))
    if (bool(random.getrandbits(1))):
      print("Environment situation ",Environment.park)
      print("Car leaving ")
      canvas.itemconfig(vectorPark[car.getPosition()],fill="green")
      car.carleavePark()
      carObjects.delitem(car)
      canvas.update()
  for car in carObjects:
    print("Car leaving ")
    canvas.itemconfig(vectorPark[car.getPosition()],fill="green")
    car.carleavePark()
    carObjects.delitem(car)
    canvas.update()
  
  
'''
def EnvironmentSimulate(seconds,Environment,canvas,vectorPark):
  print("Simulation going started \n")
  pool = ThreadPool(4)
  for x in range(6):
    count=0
    carNumber="car"+str(count)
    canvas.update()
    Car=car(carNumber,Environment)
    print("Car going parking \n")
    Car.cargoPark()
    print("Car parked ",Car.getPosition())
    canvas.itemconfig(vectorPark[Car.getPosition()],fill="red")
    canvas.update()
    print("Environment situation ",Environment.park)
    time.sleep(random.randint(0,seconds))
    print("Car leaving ")
    canvas.itemconfig(vectorPark[Car.getPosition()],fill="green")
    Car.carleavePark()
    canvas.update()
    print("Environment situation ",Environment.park)
'''



master = Tk()

canvas_width = 400
canvas_height = 400
w = Canvas(master, 
           width=canvas_width,
           height=canvas_height)

p0=w.create_rectangle(0,0,100,100,fill="green")
p1=w.create_rectangle(0,100,100,200,fill="green")
p2=w.create_rectangle(0,200,100,300,fill="green")
vectorPark =[p0,p1,p2]
w.pack()
master.after(100000,EnvironmentSimulate(5,Environment1,w,vectorPark))
master.mainloop()






