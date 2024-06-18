a=input("enter the coversion method:'f'for celsius to fahrenheit and vice versa")
if a=='f':
    x=int(input("enter the  number"))
    print("the coverted value is",((9//5)*x)+32)
elif a=='c':
    y=int(input("enter the  number"))
    print("the coverted value is",((y-32)*5)//9)
else:
    print("invalid input")
