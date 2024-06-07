
import random
 
print("welcome to dice rolling game...players")

name_1=input("player1 enter ur name...")
name_1=name_1.upper()
name_2=input("player2 enter ur name...")
name_2=name_2.upper()

player1_score=0
player2_score=0

for i in range(1,6):
  print(f"=======round-{i}========")

  player1_input=input(f"press enter key to roll ur dice ... {name_1}")
  player1_value=random.randint(1,6)

  player2_input=input(f"press enter key to roll ur dice...{name_2}")
  player2_value=random.randint(1,6)

  if player1_value > player2_value:
    print(f"{name_1} ....u wins this round")
    player1_score+=1

  elif player1_value < player2_value:
    print(f"{name_2} ....u wins this round")
    player2_score+=1

  else:
    print("Ohh....This round is draw")


if player1_score > player2_score:
  print(f"=================congrats  {name_1}...u wins this battle.Your score is  {player1_score}==============")

else:
  print(f"=================congrats  {name_2}...u wins this battle.Your score is  {player2_score}===============")

