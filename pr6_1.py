from audioop import reverse


list=[1,2,8,6,4,3,5]
print("\n-----CREATING LIST-----\n",list)
list.append(9)
print("\n-----ADDIND ELEMENT-----\n",list)
del(list[7])
print("\n-----REMOVE ELEMENT-----\n",list)
list.sort()
print("\n-----SORT THE LIST-----\n",list)
list.reverse()
print("\n----REVERSE THE LIST----\n",list)
print("\n--ACCESS ELEMENT OF LIST USING INDEX--\n",list[4])
print("\n--GET THE NUMBER OF ELEMENT--\n",len(list))






