import turtle
import math
import random

win=turtle.Screen()
win.bgcolor("White")
win.title("Fractals")
win.tracer(10)					
	
Choices=[0,1]

def trees(x1,y1,angle,length,pen):
	pen.penup()
	pen.goto(x1,y1)
	pen.pendown()
	x2=x1+length*math.cos((math.pi/180.0)*angle)
	y2=y1+length*math.sin((math.pi/180.0)*angle)
	pen.goto(x2,y2)

	if length>15:
		#left branch
		trees(x2,y2,angle+random.randint(5,30),length*((random.randint(7,9))/10),pen)
		#Right branch
		trees(x2,y2,angle-random.randint(5,30),length*((random.randint(7,9))/10),pen)
		
		if random.choice(Choices)==1:
			#Right Right branch
			trees((x1+x2)/2,(y1+y2)/2,angle-random.randint(5,35),length*0.8,pen)
			#Left Left branch
			trees((2*x1+3*x2)/5,(2*y1+3*y2)/5,angle+random.randint(5,35),length*0.8,pen)


pen=turtle.Turtle()
pen.shape("arrow")
pen.color("Green")
pen.speed(3)
pen.turtlesize(stretch_wid=0.01, stretch_len=0.01, outline=None)

trees(0,-250,90,100,pen)
pen.hideturtle()

while True:
	win.update()

win.mainloop()
