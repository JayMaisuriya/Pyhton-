import datetime
y=int(input("ENTER YEAR: "))
m=int(input("ENTER MONTH: "))
d=int(input("ENTER DAY: "))

today=datetime.date(y,m,d)
print(today)
formatdate=datetime.date.strftime(today,"%m-%d-%Y")
print(formatdate,"\n")