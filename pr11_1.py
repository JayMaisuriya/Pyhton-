#create text file and write a string
f=open("file.txt","w")
f.write("HELLO")
if f:
    print("\nFILE IS CREATED.\n")
f.close()

#read text file
f=open("file.txt","r")
print(f.read())
f.close()

#read text file line by line
f=open("file.txt","r")
print(f.readline())
print(f.readline())
print(f.readline())
f.close()

#write a list of string to a file
f=open("file.txt","w")
t=("HELLO!!\nMY NAME IS JAY\n")
f.writelines(t)
f.close()

#count line and words
f=open("file.txt")
line,word=0,0
for i in f:
    line+=1
    word+=len(i.split())
print("LINE=",line)
print("WORDS=",word)
f.close()
