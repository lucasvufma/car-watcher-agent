from tkinter import *
from random import randint
import time


game_size = 400
left_wall = 10
right_wall = left_wall+game_size
top_wall = 10
bot_wall = top_wall+game_size
directions = ["north", "south", "east", "west"]
car_size = 10 # half the width of the car

#-------------------------------------------------------
class Car:

    # Constructor. Creates a car at a random position  and direction in the game
    def __init__(self, xpos, ypos, dir):
        self.x = xpos
        self.y = ypos
        self.direction = dir
        self.crashed = False

    # is the car in a crashed state
    def is_crashed(self):
        return self.crashed

    # is the position (x, y) on the car
    def on(self, x, y) :
        left = self.x - car_size
        right = self.x + car_size
        top = self.y - car_size
        bot = self.y + car_size
        return x >= left and x <= right and y >= top and y <= bot

    # Move the car forward one pixel
    def move(self):
        if self.crashed :
            return
        if self.direction=="north" :
            self.y -= 1
        elif self.direction=="south" :
            self.y += 1
        elif self.direction=="east" :
            self.x += 1
        elif self.direction=="west" :
            self.x -= 1
        # check if crashed
        if self.y-car_size < top_wall or self.y+car_size > bot_wall or self.x-car_size < left_wall or self.x+car_size > right_wall :
            self.crashed = True
        
    # Draw the car
    def draw(self, canvas):
        left = self.x - car_size
        right = self.x + car_size
        top = self.y - car_size
        bot = self.y + car_size
        if self.crashed :
            canvas.create_rectangle(left, top, right, bot, fill="black")
        else :
            canvas.create_rectangle(left, top, right, bot, fill="red")
            if self.direction=="north" :
                top -= 4
            elif self.direction=="south" :
                bot += 4
            elif self.direction=="east" :
                right += 4
            elif self.direction=="west" :
                left -= 4
            canvas.create_rectangle(left, top, right, bot, fill="")
        
    def turn_left(self) :
        if self.direction=="north" :
            self.direction = "west"
        elif self.direction=="south" :
            self.direction = "east"
        elif self.direction=="east" :
            self.direction = "north"
        elif self.direction=="west" :
            self.direction = "south"

    def turn_right(self) :
        if self.direction=="north" :
            self.direction = "east"
        elif self.direction=="south" :
            self.direction = "west"
        elif self.direction=="east" :
            self.direction = "south"
        elif self.direction=="west" :
            self.direction = "north"

#-------------------------------------------------------
class CarGame:

    def __init__(self):
        self.cars = []
        window = Tk()
        Button(window, text="Restart", command=self.start).pack()
        self.canvas = Canvas(window, height=game_size+20, width=game_size+20, bg="white")
        self.canvas.pack()
        self.canvas.bind("<ButtonRelease-1>", self.do_left)
        self.canvas.bind("<ButtonRelease-3>", self.do_right) 
        self.redraw() 
        window.mainloop()

    def redraw(self):
        self.canvas.delete(ALL)
        self.canvas.create_rectangle(10, 10, 10+game_size, 10+game_size)
        for car in self.cars :
            car.draw(self.canvas)
        self.canvas.update()

    # set the list of cars to contain just one car then loop,
    # moving the cars, then redrawing until there are no cars left
    def start(self) :
        self.cars = []
        self.cars.append(self.make_new_car())
        self.redraw()
        speed = 10
        while True :
            for car in self.cars:
                car.move()
            self.redraw()
            num_live = 0
            for car in self.cars:
                if not car.crashed :
                    num_live += 1
            if num_live <= 0:
                return
            speed += 0.1/num_live   # make the speed a little bit bigger
            time.sleep(1/speed)
            
    # If clicked on car, make it turn left. Otherwise, make a new car at a random place
    def do_left(self, event):
        for car in self.cars :
            if car.on(event.x, event.y) :
                car.turn_left()
                return
        car = self.make_new_car()
        self.cars.append(car)

    # If clicked on car, make it turn right. Otherwise, make a new car at a random place
    def do_right(self, event):
        for car in self.cars :
            if car.on(event.x, event.y) :
                car.turn_right()
                return
        # if not clicked on any car, make a new one
        car = self.make_new_car()
        self.cars.append(car)

    def make_new_car(self):
        xpos = randint(left_wall + car_size, right_wall - car_size)
        ypos = randint(top_wall + car_size, bot_wall - car_size)
        dir = directions[randint(0,3)]
        return Car(xpos, ypos, dir)


#This is necessary to start the program
CarGame()