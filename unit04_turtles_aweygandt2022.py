############################################################################
#     Aidan Weygandt                        3.15.2021                      #
#     Unit 4 Problems                                                      #
#     Turtle Circle Overlap                                                #
############################################################################
import turtle
c1 = input("Enter circle 1's x-, y-coordinates, and radius: ").split() #User Input for x, y and radius of circles
c2 = input("Enter circle 2's x-, y-coordinates, and radius: ").split() #turns string unto list
t = turtle
counter = 0 #used in for loop to keep track of list index
for item in c1: #converts all strings in these lists into integers
  c1[counter] = int(item)
  c2[counter] = int(c2[counter])
  counter += 1
dist = ((((c2[0]-c1[0])**2)+((c2[1]-c1[1])**2))**0.5) #distance between the two circles
if dist > (c1[2])+(c2[2]): #if theres more space between the circles than their radius' combined
  message = "The Circles are not overlapping"
else: #If theres less space between the circles than their radius's combined
  message = "The Circles are overlapping"
  if min(c1[2], c2[2])*2 > dist: #If smaller circle is inside the other one
    if min(c1[2], c2[2]) == c1[2]: #finds out which one is on the inside
      message = "Circle one is inside circle two"
    else: message = "Circle two is inside circle one"
t.goto(0,-250)
t.pendown()
t.goto(0,250)
t.penup()
t.goto(-250, 0)
t.pendown()
t.goto(250, 0)
t.penup()
t.goto(0, -2)
t.fillcolor("red")
t.begin_fill()
t.circle(2)
t.end_fill()
t.circle(2)
t.penup
t.goto(c1[0], c1[1]-(c1[2]))
t.pendown()
t.circle(c1[2])
t.penup()
t.goto(c2[0], c2[1]-(c2[2]))
t.pendown()
t.circle(c2[2])
t.penup()
t.goto(c1[0]-(max(c1[2], c2[2])*1.5), c1[1]-(max(c1[2], c2[2])*1.5))
t.pendown()
t.write(message)