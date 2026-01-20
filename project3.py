import turtle, time, random
from utils import *

# Section 1 - Variables
# TODO - add starting values for all the variables
#wallywast
x1 =-200
y1 =1
#snail red
x2 =-200
y2 =100
x3 =-200
y3 =-100
x4 =-200
y4 =-200


# Section 2 - Setup
# # TODO - use your own background, and set your four turtles to images of your choice
set_background("speed.gif")
t1 = create_sprite("wally.gif",x1,y1)
t2 = create_sprite("redsnail.gif",x2,y2)
t3 = create_sprite("turbo.gif",x3,y3)
t4 = create_sprite("quickster.gif",x4,y4)


# # Section 3 - Racing
# # TODO - set how much each variable changes by and increase the number of repeats to at least 30
# # TODO - explain here which sprites are faster or slower
for i in range(100):
     x1 +=10
     x2 +=10
     x3 +=15
     x4 +=20
     #the quickster will win becuase he has the fastest speed 

     t1.goto(x1, y1)
     t2.goto(x2, y2)
     t3.goto(x3, y3)
     t4.goto(x4, y4)

     window.update()
     time.sleep(0.1)


# # Section 4 - Winner
# # TODO - complete the elif for player 2 winning
# # TODO - write another elif for player 3 and player 4
if x1 >= x2 and x1 >= x3 and x1 >= x4:
     print("player 1 wins!")
elif x2 >= x1 and x2 >= x3 and x2 >= x4:
     print("player 2 wins!")
elif x3 >= x1 and x3 >= x2 and x3 >= x4:
    print("player 3 wins!")
elif x4 >= x1 and x4 >= x3 and x4 >= x2:
    print("player 4 wins!")

turtle.exitonclick()