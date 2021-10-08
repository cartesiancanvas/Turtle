import turtle
import random


win=turtle.Screen()
win.bgcolor("black")
win.title("Bouncing Ball Simulation")
win.tracer(0)

balls=[]
for i in range(22):
	balls.append(turtle.Turtle())
colors=["Red","Blue","Yellow","Pink","Purple","Orange"]
shapes=["square","triangle","circle","arrow","turtle"]
side=[-1,1]	

for ball in balls:
	ball.color(random.choice(colors))
	ball.shape(random.choice(shapes))
	ball.penup()
	ball.speed(0)
	ball.goto(random.randint(-300,300),random.randint(-20,310))
	ball.dy=0
	ball.dx=((random.randint(0,50))/100.0)*random.choice(side)
	ball.da=((random.randint(1,5))/10)*random.choice(side)

#Forces
gravity=0.015


while True:
	win.update()
	for ball in balls:
		ball.rt(ball.da)
		ball.dy-=gravity
		ball.sety(ball.ycor()+ball.dy)
		ball.setx(ball.xcor()+ball.dx)

		#check for lower edge
		if ball.ycor()<-300:
			ball.sety(-300)
			ball.dy*=-1
			ball.da*=-1
		#check for upper edge
		if ball.ycor()>300:
			ball.sety(300)
			ball.dy*=-1
			ball.da*=-1	
		#check for Right edge
		if ball.xcor()>350:
			ball.dx*=-1
			ball.da*=-1
		#check for Left edge
		if ball.xcor()<-350:
			ball.dx*=-1
			ball.da*=-1
			
		for i in range(0,len(balls)):
			for j in range(i+1,len(balls)):
				if balls[i].distance(balls[j])<30:
					balls[i].setx(balls[i].xcor())
					balls[i].sety(balls[i].ycor())
					balls[j].setx(balls[j].xcor())
					balls[j].sety(balls[j].ycor())
					balls[i].dx,balls[j].dx=balls[j].dx,balls[i].dx
					balls[i].dy,balls[j].dy=balls[j].dy,balls[i].dy

win.mainloop()