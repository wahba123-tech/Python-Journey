print("Unit conversion type:")
options=print('1:length\n''2:temperature\n''3:weight')
user=input("Which type of conversion you want:")

if user=='length':
  print('1:kilometers to Miles\n''2:Miles to kilometer')
  choice=int(input("Enter your choice:"))
  if choice==1:
    try:
      enter=float(input("Enter the value:"))
      print(f"{enter*0.621371}miles")
    except ValueError:
       print("wrong value") 
  elif  choice==2:
    try:
      enter=float(input("Enter the value:"))
      print(f"{enter/0.621371}kilo")
    except ValueError:
      print("you enterd wrong value")
elif user=='temperature' :
  print('1:Celsius to Farenheit\n''2:Farenheit to Celsius')
  choice1=int(input("Enter your choice:"))
  if choice1==1:
    celsius=int(input("Enter the value:"))
    print(f'{(celsius*9/5)+32}farenheit')
  if choice1==2:
    farenhiet=int(input("Enter the value:"))
    print(f"{(farenhiet-32)*5/9}celsius") 
elif user=='weight':
  print("1:kilogram to pounds\n2:pounds to kilograms")
  choice2=int(input("Enter choice:"))
  if choice2==1:
   kilogram=float(input("Enter your value"))
   print(f"{kilogram*2.20462}pounds")
  elif choice2==2:
    pounds=float(input('Enter the value:'))
    print(f"{pounds/2.20462}kilogram")
else:
  print("wrong input")  


