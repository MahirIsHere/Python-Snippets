import turtle
turtle.title("My Torto!!")
t = turtle.Turtle()
t.speed(1) 
t.color("green")
t.shape("turtle") 

t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.home()

c = t.clone()
t.color("black")
c.color("blue")
t.circle(100)
c.circle(60)

# Write text
txt()

# To hide turtle
pen.ht()

turtle.Screen().exitonclick()
