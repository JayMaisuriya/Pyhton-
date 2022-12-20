from cmath import sqrt


b=int(input("ENTER THE VALUE OF B : "))
a=int(input("ENTER THE VALUE OF A : "))
c=int(input("ENTER THE VALUE OF C : "))

delta=(b**2-4*a*c)
print("DELTA =",delta)

root=(-2 + sqrt(delta)/2*a)
print("REAL ROOT=",root)



