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

   """ def updateInformation(self):
        for e in self.environment.park:
            if e in self.information and self.information[e]==self.environment.park[e]:
                del(self.information[e])
            elif e in self.information and self.information[e]!=self.environment.park[e]:
              self.information[e]=self.environment.park[e]
            else:
              self.information = self.environment.park.copy() """
    def getInformation(self):
        self.updateInformation()
        return print(self.information)


class Environment:
  def __init__(self):
    self.things = []
    self.park= {0:"free",1:"busy",2:"free",3:"busy"}
  def setState(self,index,state):
    self.park[index]=state
  def getState(self,index):
    return self.park[index]

Environment1=Environment()
presenceSensor1=presenceSensor(Environment1)
Agent1=Agent(Environment1,presenceSensor1)
Environment1.setState(0,"busy")


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

def EnvironmentSimulate(carNumber,seconds,Environment):
  print("Simulation going started \n")
  car1=car(carNumber,Environment)
  print("Car going parking \n")
  car1.cargoPark()
  print("Car parked ",car1.getPosition())
  print("Environment situation ",Environment.park)
  time.sleep(random.randint(0,seconds))
  print("Car leaving ")
  car1.carleavePark()
  print("Environment situation ",Environment.park)


EnvironmentSimulate("5",3,Environment1)