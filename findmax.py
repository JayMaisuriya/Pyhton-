a=int(input("ENTER THE VALUE OF A :"))
b=int(input("ENTER THE VALUE OF B :"))
c=int(input("ENTER THE VALUE OF c :"))

ANSWER = (a if(a>b and a>c) else b if(b>a and b>c) else c)
print("MAXIMUM VALUE =",ANSWER)
