import random
while True:
 print("1 for snake,2 for water ,3 for gun")
 comp=random.randint(1,3)
 user=int(input("Select any one option:"))

 def game(comp,user):
  
  if comp==user:
   print(" naheeda its tie")
  elif comp==3 and user==1:
    print('user lost')
  elif comp==2 and user== 3:
    print(' naheeda user lost')
  elif comp==1 and user==2:
   print('user lost')
  else:
    print("user won")

 print("comp:",comp)
 print("user:",user) 


 game(comp,user)
 choice=input("Do you want to play again (y/n):").lower()

 if choice=='n':
  quit





