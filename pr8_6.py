amt=int(input("\nENTER LOAN AMOUNT: "))
y=int(input("ENTER NUMBER OF YEAR: "))
rate=int(input("ENTER INTEREST RATE: "))

def EMI():
    INTEREST=(amt*y)/rate
    print("\n--------------------------")
    print("INTEREST=",INTEREST)
    total=INTEREST+amt

    e=(total/(12*y))
    print("EMI=",e)

    ttlamt=amt+INTEREST
    print("TOTAL PAYMENT= ",ttlamt)
    print("---------------------------\n")

EMI()
