def list():
    l=[1,2,3,4,5,6,1,3,6,2,7,8,5,9,8,7,2,1]
    l1=[]
    for i in (l):
        if i not in l1:
            l1.append(i)
    print("\n",l1,"\n")
list()
        