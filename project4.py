import turtle, time, random
from utils import *
#the object of this game is to save the hostage before the bomb blows or he gets to scared to escape
# Section 1 - setup
# TODO - set a background using set_background()
set_background("hostage.gif")
create_sprite("bomby.gif")
# TODO - create at least two variables and set their starting value. ex: cookies = 0
fear = 25
bomb_timer = 20
rope = 100
last_duck_time = 0
# OPTIONAL: use this invisible alien to say a message
message_sprite = create_sprite("alien", -200,200)
message_sprite.hideturtle()
message_sprite1 = create_sprite("alien", -200,150)
message_sprite1.hideturtle()
message_sprite2 = create_sprite("alien", -200,100)
message_sprite2.hideturtle()
# Section 2 - controls

# TODO - define an action. ex: def my_control()
def get_fear():
    global fear, last_duck_time, i,rope
    if i > last_duck_time + 100:
        fear += 1
        x = random.randint (-200,200)
        y = random.randint (-200,200)    
        create_sprite("ducky.gif",x,y)
        #last_duck_time = i   
        
# TODO - choose a key to do the action. ex: window.onkeypress(my_control, "space")
window.onkeypress(get_fear,"space")
#when you press space you will give the hostage more fear bar keeping him calm
# TODO - make a second control
def get_rope():
    global rope,get_rope,fear
    fear += -1
    rope += -1
    if rope <= 0:
        create_sprite("win.gif", 0,0)
    elif fear <= 0:
        create_sprite("lose.gif")
    elif bomb_timer <= 0:
        create_sprite("lose.gif")
#saw the rope bringing the rope down
window.onkeypress (get_rope,"Up")







# Section 3 - game loop
window.listen()
for i in range(1000000000):
    # TODO - put any repeating actions here
    if i% 100 == 0:
        bomb_timer -=1
        fear -= 1 
    time.sleep(0.01)
    window.update()
        # OPTIONAL - use the message sprite to say a message
    message_sprite.clear()
    message_sprite.write(f" bomb {bomb_timer}")
    message_sprite1.clear()
    message_sprite1.write(f" fear {fear}")
    message_sprite2.clear()
    message_sprite2.write(f" rope {rope}")
