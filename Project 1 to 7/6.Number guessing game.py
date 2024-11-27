
import random

random_number=random.randint(0,30)
name=input("Enter Your Name:")
print(f"Wlcome to Number Guessing Game {name}.... ")

print("guess the number between 0 to 30...")

if random_number < 15:
  print("guess the number between 0 to 15")

elif random_number >= 15 and random_number <20:
  print("guess the number 15 and above ...")

elif random_number >=20 and random_number < 25:
  print("guess the number  20 and above....")

elif random_number >= 25:
  print("guess the number  25 and above....")

chances=5
guess=int(input("enter the ur guess.. "))


while chances > 0:


   if guess > random_number:
       
       print(f"u need to guess lower....guess below the number ....{guess}")
       guess=int(input("enter the ur guess.. "))
       chances=chances-1
       print(f"u have only {chances} more chances....")
       


   if guess < random_number:
       
       print(f"u need to guess higher....guess above  the number ....{guess}")
       guess=int(input("enter the ur guess.. "))
       chances=chances-1
       print(f"u have only {chances} more chances....")
       


   if guess == random_number:
       break

if guess == random_number:
  chances=str(chances)
  print(f"congrats ! {name} u guessed the number in {chances} chance... ")

if guess != random_number:
  guess=str(guess)
  print(f"ohhh... {name} u  loose the game ...The  number is {random_number} .... ")

