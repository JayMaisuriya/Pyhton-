string=input("\nENTER PALINDROME STRING: ")
x=""
for i in string:
    x=i+x
if (string == x) :
    print("STRING IS PALINDROME\n")
else :
    print("STRING IS NOT PALINDROME\n")
    