import random
count=0
while True:
 comp=random.randint(1,100)
 user=int(input('Guess the num and enter:'))
 
 def guess(comp,user):

   if user>comp:
    print("Too high!Try again")
   elif user<comp:
    print("Too low! Try again")  
   elif user==comp:
    print("Congratulations!You won")
  

 print("computer:",comp)
 print("user:",user)
 guess(comp,user) 
 count += 1
 
 print(count)   

 choice=input("Do you want to play again (y/n):").lower()
 if choice=='n':
   break

