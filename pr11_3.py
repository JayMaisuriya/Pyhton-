f=open("file1.txt")
num=0
f.readline()
for i in f:
    for a in i:
        if a.isdigit() == True:
            num+=1
            print("NUMBER=",a)
print("TOTAL NUMBERS= ",num)
         