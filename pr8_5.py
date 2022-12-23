def GDC(a,b):
    if a==b:
        return a
    elif a<b:
        return GDC(b,a)
    else:
        return GDC(b,a-b)
a=int(input("ENTER FIRST NUMBER: "))
b=int(input("ENTER SECOND NUMBER: "))
print(GDC(a,b))