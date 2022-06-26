############################################################################
#     Aidan Weygandt                        3.15.2021                      #
#     Unit 4 Problems                                                      #
#     Sort 3 sort three numbers, divisible by 5 and/or 6                   #
#     Rock, Paper, or Scissors,  Pick a card                               #
#     Palindrome Number                                                    #
############################################################################
import random
import turtle


numbers = ""
print ("Problem #1 - Sort three numbers")
numberstr = sorted(input("Input three numbers divided by spaces: ")) #User input. Also sorts numbers
for character in numberstr: #Adds each number one by one to a string
    numbers =numbers + character + " "
numbers = numbers.replace("    ", "") 
print ("The numbers sorted are", numbers)


print ("\n\nProblem #2 - Divisible by 5 and/or 6")
integer = int(input("Enter an integer: ")) #user input
if integer//5 == integer/5 and integer//6 == integer/6: #If divided by 5 and 6 is the number still whole
  print (integer, "is divisible by 5 and 6.")
elif integer//5 == integer/5 or integer//6 == integer/6: ##If divided by 5 or 6 is the number still whole
  print (integer, "is divisible by 5 or 6.")
else: print (integer, "is not divisible by 5 or 6.")


print ("\n\nProblem #3 - Rock paper, or scissors")
list = ["rock.", "paper.", "scissors.", "You win.", "You lose.", "You tied.", "gun."]
player = int(input("Select rock(0), paper(1), or scissors(2): ")) #user choice
computer = random.randint(0, 2) #computer's choice
if player == 0 and computer == 1: #All game possibilities
  print ("The computer played", list[computer], "And you played", list[player], list[4])
elif player == 1 and computer == 2:
  print ("The computer played", list[computer], "And you played", list[player], list[4])
elif player == 2 and computer == 0:
  print ("The computer played", list[computer], "And you played", list[player], list[4])
elif player == 0 and computer == 0:
  print ("The computer played", list[computer], "And you played", list[player], list[5])
elif player == 1 and computer == 1:
  print ("The computer played", list[computer], "And you played", list[player], list[5])
elif player == 2 and computer == 2:
  print ("The computer played", list[computer], "And you played", list[player], list[5])
elif player == 0 and computer == 2:
  print ("The computer played", list[computer], "And you played", list[player], list[3])
elif player == 1 and computer == 0:
  print ("The computer played", list[computer], "And you played", list[player], list[3])
elif player == 2 and computer == 1:
  print ("The computer played", list[computer], "And you played", list[player], list[3])
elif player == 6: #Becuase win
  print ("The computer played", list[computer], "And you played", list[player], list[3])
else: print ("Please enter a 0, 1, or 2")


card = random.randint (0, 12) #selects random card
suite = random.randint (0, 3) #selects random suite
cards = ["ace", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "jack", "queen", "king"]
suites = ["clubs", "spades", "hearts", "diamonds"]
print ("\n\nProblem #4 - Pick a card", "\nYour card was", cards[card].capitalize(), "of", suites[suite].capitalize()) #combines card and suite


print ("\n\nProblem #5 - Palindrome Number")
number5 = input ("Enter a number: ") #user input
reverse5 = number5 [::-1] #reverses number
if number5 == reverse5: #if the number is the same backwards
  print (number5, "is a palindrome")
else: print (number5, "isn't a palindrome")