
print("WELCOME TO FLAMES GAME....!")
def flames_game(name1, name2):
   
    name1 = name1.lower().replace(" ", "")
    name2 = name2.lower().replace(" ", "")

    unique_letters = set(name1 + name2)

    total_letters = len(unique_letters)

    flames = "FLAMES"
    result_index = (total_letters % len(flames)) - 1

    
    relationship_status = flames[result_index]
    

    return relationship_status


name1 = input("enter first name...:")
name2 =input("enter second name...:")


result = flames_game(name1, name2)
if result=='E':
    result="enimeis"
elif result=='F':
    result="friends"
elif result=='L':
    result="Love"
elif result=='M':
    result="marriage"
elif result=='s':
    result="sister"
elif result=='A':
    result="affection"

print(f"The relationship status between {name1} and {name2} is: {result}")
  
