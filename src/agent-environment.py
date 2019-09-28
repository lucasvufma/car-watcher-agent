
from enum import Enum;
import random;
import time;
from tkinter import *


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
        self.previousInformation={}
        self.presenceSensor=presenceSensor

    """a ideia aqui é ter um dicionario com chaves representando as percepções e ele vá agindo perante a elas"""
    def actuate(self,canvas,vectorPark,agentFisico):
        for e in self.perceptions.copy():
            if self.perceptions[e]==self.previousInformation[e]:
                del(self.perceptions[e])
                pass
            else:
                print("Change canvas", e,self.perceptions[e])
                if self.perceptions[e]=="FREE":
                    canvas.itemconfig(vectorPark[e],stipple="gray50",outline="blue")
                    canvas.itemconfig(agentFisico,fill="blue")
                    canvas.update()
                    time.sleep(0.5)
                    canvas.itemconfig(vectorPark[e],stipple="",outline="black")
                    canvas.itemconfig(agentFisico,fill="white")
                    canvas.update()
                else:
                    canvas.itemconfig(vectorPark[e],stipple="gray50",outline="blue")
                    canvas.itemconfig(agentFisico,fill="blue")
                    canvas.update()
                    time.sleep(0.5)
                    canvas.itemconfig(vectorPark[e],stipple="",outline="black")
                    canvas.itemconfig(agentFisico,fill="white")
                    canvas.update()
                del(self.perceptions[e])
    def percept(self):
        self.previousInformation=self.presenceSensor.getInformation()
        self.perceptions=self.presenceSensor.getinformationChange().copy()

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
      self.updateinformationChange()
      return self.informationChange
    def updateInformation(self):
        self.information=self.environment.park.copy()

    def getInformation(self):
        return self.information


class Environment:
  def __init__(self):
    self.things = []
    self.park= {0:"FREE",1:"FREE",2:"FREE",3:"FREE",4:"FREE",5:"FREE",6:"FREE",7:"FREE"}
  def setState(self,index,state):
    self.park[index]=state
  def getState(self,index):
    return self.park[index]

Environment1=Environment()
presenceSensor1=presenceSensor(Environment1)
Agent1=Agent(Environment1,presenceSensor1)
Environment1.setState(0,"FREE")


class carBehaviour():
  def __init__(self,environment):
    self.environment=environment
  def randomPark(self):
    return random.randint(0,7)
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
def AgentProgram(Agent,presenceSensor,canvas,vectorPark,agentFisico):
    Agent.percept()
    Agent.actuate(canvas,vectorPark,agentFisico)
def EnvironmentSimulate(seconds,Environment,canvas,vectorPark,Agent,presenceSensor,agentFisico):
  carsNumbers=[]
  for x in range(0,8):
    carsNumbers.append("car"+str(x))
  Car0=car(carsNumbers[0],Environment)
  Car1=car(carsNumbers[1],Environment)
  Car2=car(carsNumbers[2],Environment)
  Car3=car(carsNumbers[3],Environment)
  Car4=car(carsNumbers[4],Environment)
  Car5=car(carsNumbers[5],Environment)
  Car6=car(carsNumbers[6],Environment)
  Car7=car(carsNumbers[7],Environment)

  carObjects=[Car0,Car1,Car2,Car3,Car4,Car5,Car6,Car7]
  print("Car going parking \n")
  canvas.update()
  for Car in carObjects:
    Car.cargoPark()
    print("Car parked ",Car.getPosition())
    canvas.itemconfig(vectorPark[Car.getPosition()],fill="red",stipple="")
    canvas.update()
    AgentProgram(Agent,presenceSensor,canvas,vectorPark,agentFisico)
    time.sleep(random.randint(0,3))
    if (bool(random.getrandbits(1))):
      print("Environment situation ",Environment.park)
      print("Car leaving ")
      canvas.itemconfig(vectorPark[Car.getPosition()],fill="green",stipple="")
      Car.carleavePark()
      carObjects.remove(Car)
      print("Environment situation ",Environment.park)
      canvas.update()
      AgentProgram(Agent,presenceSensor,canvas,vectorPark,agentFisico)
  for Car in carObjects:
    print("Car leaving ")
    if Car.getPosition() is not None:
      print("in Conditional Environment situation ",Environment.park)
      canvas.itemconfig(vectorPark[Car.getPosition()],fill="green")
      Car.carleavePark()
      carObjects.remove(Car)
      canvas.update()
      AgentProgram(Agent,presenceSensor,canvas,vectorPark,agentFisico)
      print(Environment.park)
  
master = Tk()

canvas_width = 400
canvas_height = 400
w = Canvas(master, 
           width=canvas_width,
           height=canvas_height)

p0=w.create_rectangle(0,0,100,100,fill="green")
p1=w.create_rectangle(0,100,100,200,fill="green")
p2=w.create_rectangle(0,200,100,300,fill="green")
p3=w.create_rectangle(100,0,200,100,fill="green")
agentFisico=w.create_rectangle(100,100,200,200,fill="white")
p4=w.create_rectangle(100,200,200,300,fill="green")
p5=w.create_rectangle(200,0,300,100,fill="green")
p6=w.create_rectangle(200,100,300,200,fill="green")
p7=w.create_rectangle(200,200,300,300,fill="green")

vectorPark =[p0,p1,p2,p3,p4,p5,p6,p7]
w.pack()
master.after(1000,EnvironmentSimulate(5,Environment1,w,vectorPark,Agent1,presenceSensor1,agentFisico))
master.mainloop()



