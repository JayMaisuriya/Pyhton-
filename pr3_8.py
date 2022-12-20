from math import sin


a=int(input("ENTER THE VALUE ANGLE: "))
h=int(input("ENTER THE VALUE OF HEIGHT : "))
pie=3.14

angler=((pie/180)*a)
print("ANGLER = ",angler)

lenght=float(h/sin(angler))
print("LENGHT = ",lenght)