a=int(input("Enter any one value:"))
b=int(input("Enter any other value:"))
c=input("Enter the operator:")

if c=='+':
   print(a+b)
elif c=='-':
   print(a-b) 
elif c=='*':
   print(a*b)
elif c=='/':
   print(a/b) 
elif c=='//':
   print(a//b) 
else:
   print("you entered wrong operator")        
