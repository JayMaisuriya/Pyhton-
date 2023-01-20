import string
def main():
    file=input("\nENTER FILE NAME : ")
    inputfile=open(file,'r')
    files=input("ENTER FILE NAME : ")
    outputfile=open(files,'w')
   
    for i in inputfile:
        words =i.split() 
        for word in words:
            count=0
            for j in word:
                if not j in string.punctuation:
                    count+=1
            if count==4:
                if "." in word:
                    word="****."
                elif "," in word:
                    word="****,"
                elif "!" in word:
                    word="****!"
                else:
                    word="****"
            print(word +" ",file = outputfile,end=" ")
    inputfile.close()
    outputfile.close()

if __name__=="__main__":
    main()


