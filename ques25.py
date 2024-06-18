a=open("abc.txt",'r')
b=open("def.txt",'w')
for i in a:
    b.write(i)
