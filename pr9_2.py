import random
r=0
p=1
s=2
computer_choice=random.randint(0,2)
user_choice=int(input("enter your choice ( rock-0 , paper-1 , scissor-2 ):"))
print("computer choice:",computer_choice)
if computer_choice == user_choice:
    print("tie")
elif computer_choice == 0 and user_choice == 1:
    print("wins")
elif computer_choice == 0 and user_choice == 2:
    print("wins")
elif computer_choice == 1 and user_choice == 0:
    print("loses")
elif computer_choice == 1 and user_choice ==2:
    print("wins")
elif computer_choice == 2 and user_choice == 0:
    print("loses")
elif computer_choice == 2 and user_choice == 1:
    print("loses")
 