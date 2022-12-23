def fibonnacci(n):
    
    if n<=1:
        return n 
    else:
        return fibonnacci(n-1)+fibonnacci(n-2)

num=int(input("Enter Number You Will be Find:"))
fibonnacci(num)
for i in range(num):
    print(fibonnacci(i))

