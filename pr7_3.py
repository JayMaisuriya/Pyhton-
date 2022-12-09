student={"en_no":44, "name":"JAY", "sem":3, "batch":"B2", "dept":"computer"}
print("\n-------------------------CREATE A DICTIONARY------------------------")
print(student,"\n")

print("\n----------------------PRINT DICTIONARY ITEMS-----------------------")
for i in student.items():
    print(i)

print("\n----------------ADD KEY-VALUE PAIR IN DICTIONARY -----------------")
student["address"]="sachin"
print(student,"\n")

print("\n----------------REMOVE KEY-VALUE PAIR IN DICTIONARY -----------------")
del student["batch"]
print(student,"\n")

key=str(input("ENTER THE KEY YOU WANT TO FIND:"))
if key in student:
  print("YES",key,"KEY IS IN THE DICTIONARY\n")
else:
   print("NO",key,"KEY IS NOT IN THE DICTIONARY\n")

print("\n-------------ITERATE THROUGH A DICTIONARY -------------")
for i in student:
   print(student[i])

print("\n----------------CONCATENATE DICTIONARY -----------------")
student1={"s_id":1, "s_name": "akash"}
student.update(student1)
print(student)