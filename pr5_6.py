a=int(input("\nENTER THE NUMBER:"))
sum=0
for i in range(1,a):
    if a%i==0:
     sum+=i
if a==sum:
    print("NUMBER IS PERFACT\n")
else:
    print("NUMER IS NOT PERFACT\n")