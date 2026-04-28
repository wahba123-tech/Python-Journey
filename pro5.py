balance=0
Account_Name=input("Enter your account name:")
choice=['deposit','withdraw','check','balance','exit']
while True:
    user=input("Enter what you want to do:").lower()
    if user=='deposit':
       try:
        add= int(input("Enter the amount you want to deposit:"))
        if add>0:
         balance+=add
         print(f"balance succesfully added :${balance:,}")
        else:
         print("deposit amount must be greater then zero")
       except ValueError:
        print("you entered wrong value")
       
    elif user=='withdraw' :
        try:
         take1=int(input("Enter the amount you want to withdraw:"))
         if take1<=0:
            print("withdraw amount must be greater then zero")
         elif take1>balance:    
            print(f'insufficient balance you hv: ${balance:,}')
         else:
            balance-=take1
            print(f'balance you hv is: ${balance:,}')
        except ValueError:
           print("you entered wrong value")    
    elif user=='check' :
        print(f"balance is: ${balance:,}")          
    elif user=='exit':
        break
    else:
      print("wrong input")

