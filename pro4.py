Tasklist=[]
while True:
 print("To-Do list Menu:")
 print("1.Add a task\n2.View a task\n3.Deleta a task\n4.Exit")
 user=int(input("Enter your choice:"))
 if user==1:
  ask=input("enter your task name:")
  Tasklist.append(ask)
 elif user==2:
  print(Tasklist)
 elif user==3:
   if Tasklist:
    ask1=input("enter what you want to remove:") 
    Tasklist.remove(ask1) if ask1 in Tasklist else print ("Task not found!")
   else:
    print("no task to remove")
 
 elif user==4:
  break
 else:
  print("invalid input")
 
 choice=input("Do you want to play again (y/n):").lower()
 if choice=='n':
  break