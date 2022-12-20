#OS=int(input("ENTER MARKS OF OS:"))
#DS=int(input("ENTER MARKS OF DS :"))
#RDBMS=int(input("ENTER MARKS OF RDBMS :"))
#PY=int(input("ENTER MARKS OD :"))
#RWPD=int(input("ENTER MARKS :"))
#total=(OS+DS+RDBMS+PY+RWPD)/5
#print("AVERAGE IS =",total)

Num=int(input("ENTER THE NUMBER OF SUBJECT :"))
total=0
for n in range(Num):
    marks=int(input("ENTER THE MARKS :"))
    total+=marks
    avrg=total/Num
print("AVERAGE OF",Num ,"IS =",avrg)