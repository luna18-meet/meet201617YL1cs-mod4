import turtle
from rectangle import Rectangle

class Square(Rectangle):
    def __init__(self,length,height):
       if lenghth>=0 :
          self.length=length
       else :
          self.length=0

       if height>=0:
          self.height=0
       else :
          self.height=0

       self.turtle=turtle.clone()
       turtle.speed(0)
       self.has_been_drawn=False

def set_length(self,new_lenght):
    if new_lenght>=0:
        self.lenght=new_length
        if self.has_been_drawn:
            self.draw_shape()

def set_height(self,new_height):
    if new_height>=0 :
        self.height=new_height
        if self.has_been_drawn : 
           self.draw_shape()

    def get_area(self):
        return self.length*self.height

    def draw_shape(self):
        self.turtle.clear() 
        self.turtle.penup()
        self.turtle.goto(0,0)
        self.turtle.pendown()
        self.turtle.goto(self.length,0)
        self.turtle.goto(self.length,self.height)
        self.turtle.goto(0,self.height)
        self.turtle.goto(0,0)
        self.turtle.penup()
        self.has_been_drawn=True


