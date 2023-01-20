file=input("\nENTER FILE NAME : ")
f=open(file,'r')
data=f.read()  #data read i file
word=data.split()
line=data.split(".")
words,sant=0,0

for i in word:
    words+=len(i)

for k in line:
    sant+=len(k)

avgwrd=words/(len(word))
avgline=sant/(len(line))

print("AVERAGE WORDS : ",avgwrd)
print("AVERAGE LINES : ",avgline)

