a=input("enter your calculation you want to performed:('+','-','*','/'):")
if (a=='+'):
    x=int(input("enter first no"))
    y=int(input("enter second no"))
    print(x+y)
elif(a=='-'):
    p=int(input("enter first no"))
    q=int(input("enter second no"))
    if(p>q):
        print(p-q)
    else:
        print(q-p)
elif(a=='*'):
    
    j=int(input("enter first no"))
    t=int(input("enter second no"))
    print(j*t)
elif(a=='/'):
    d=int(input("enter first no"))
    g=int(input("enter first no"))
    print(d//g)
else:
    print("invalid input")
            
            
