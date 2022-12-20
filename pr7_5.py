india={"GUJRAT":"GANDHINAGAR", "MAHARASTRA":"MUMBAI", "MADHYAPRADES":"BHOPAL", "UTTARPRADES":"LUCKNOW", "RAJASTHAN":"JAIPUR"}
print("\n",india,"\n")

for i in india:
    print("---------------------------------")
    print(i)
    x=input("WHAT IS CAPITAL OF? : ")    
    if x==india[i]:
     print("YOUR ANSWER IS CORRECT")
     print("---------------------------------\n")

    else:
      print("YOUR ANSWER IS INCORRECT")
      print("---------------------------------\n")

