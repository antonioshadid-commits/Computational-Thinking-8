cat_points = 0
dog_points = 0
turtle_points = 0

print ("this is a quiz to see what your favorite animal is")
print ("please only use capitalized A B OR C")
input()

answer1 = input("do you look for A loyalty, B honesty, or C good listener. in your friends ")
if answer1 == "A":
    dog_points += 1
elif answer1 == "B":
    cat_points += 1
elif answer1 == "C":
    turtle_points += 1
answer2 = input(" are you allergic to cats A yes, B no ")
if answer2 == "A":
    cat_points -= 9999999
elif answer2 == "B":
    cat_points += 1
answer3 = input(" are you allergic to dogs A yes, B no ")
if answer3 == "A":
    dog_points -= 9999999
elif answer3 == "B":
    dog_points += 1

answer4 = input(" are you allergic to turtles A yes, B no ")
if answer4 == "A":
    turtle_points -= 9999999
elif answer4 == "B" :
    turtle_points += 1
 
answer5 = input("do you like water? A yes, B no")
if answer5 == "A":
    turtle_points +=1
    dog_points+=1 
elif answer5 == "B":
    cat_points+= 2

answer6 = input("do you like peanut butter A yes B no")
C
    dog_points+=1


if turtle_points>cat_points and turtle_points> dog_points:
    print("you are a turtle person you strange strange person")
elif cat_points>= dog_points and cat_points>= turtle_points:
    print ("you a cat person good job")
elif dog_points>cat_points and dog_points > turtle_points:
    print ("you a dooog person fella")














