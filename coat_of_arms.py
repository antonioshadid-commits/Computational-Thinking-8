# Section 1 - Your code
from utils import *
set_background("black")

s1 = create_sprite("image1.gif", 0, 0)
s2 = create_sprite("book.gif", -200, 100)
s3 = create_sprite("pc.gif", 200, 100)
#s4 = create_sprite("cardinal", 100, -100)

message1 = create_sprite("alien",-90,225)
message1.color("red")
message1.write("Antonio",font = ("Arial", 40, "normal"))
message1.hideturtle()

message2 = create_sprite("alien",-370,-250)
message2.color("red")
message2.write(" dont borrow trouble from the future", font = ("Arial", 30, "normal"))
message2.hideturtle()


######################################################################


# Section 2 - Keeping the window open (DON'T CHANGE!!)
window.update()
turtle.exitonclick()