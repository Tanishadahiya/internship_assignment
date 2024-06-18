n=int(input("enter the no"))
sum=0

while n>0:
    result=n%10
    sum=sum+result
    n=n//10
    print(sum)
      
