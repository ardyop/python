a= int(input("Enter your first number  :\n"))
b= int(input("Enter your Second Number : \n"))
d= int(input("Chose your choise :\n"))
if d==1:
  c=a + b
  print("Addition Value is : ",c)
elif d==2:
  c= a - b
  print("Substraction value is : ",c)
elif d==3:
  c= a * b
  print("Multiplication value is : ",c)
elif d==4:
  c= a // b
  print("division of value is :",c)
else:
  print("Value is not defined Ok !!!")