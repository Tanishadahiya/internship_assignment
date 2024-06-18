n=input("enter the string with punctuation")
punc='''!()-[]{};:' "\,<>./?@#$%^&*_~'''
for i in n:
    if i in punc:
        n=n.replace(i,"")
print(n)
