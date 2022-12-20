num=[]
n=int(input("ENTER THE NUMBER OF ELEMENT : "))
for i in range(0,n):
    int(input("ENTER ELEMENT :"))
    num.append(n)
    print(num)


p,ng,z=0,0,0    
 
if i>0:
        p=p+1
elif i<0:
        ng+=1
else:
        z+=1

print("POSITIVE NUMBERS :",p)
print("NEGATIVE NUMBERS :",ng)
print("ZERO :",z)


