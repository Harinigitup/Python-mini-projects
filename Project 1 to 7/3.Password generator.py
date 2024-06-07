print("password generator....")
import random 
length = int(input("enter length of the password u need: "))
name=input("enter your name:") 
lower="qwertyuioplkjhgfdsaazxcvbnm" upper="QWERTYUIOPLKJHGFDSAZXCVBNM"
splchar="!@#$%^&*()_+?><:""}"
number="1234567890" 
all=name+lower+upper+splchar+number
password="".join(random.sample (all, length))
print("ur password is:", password) 
print("do u want another password ...?")
print("type 'yes' or 'no' ") 
while 1: 
  again=input("enter ur choice: ") 
  if again=='yes':
    password="".join(random.sample (all, length)) 
    print("ur password is:", password)
    print("do u want another password ...?")
    print("type 'yes' or 'no' ") 
  else:
    quit()
    break
