#Mert Oğuzhanasilturk

def isPrimeNumber(number: int): # Is "Prime Number" return False - Is not "Prime Number" retrun True
    flag = False
    if number == 2:
        return False
    if number == 1:
        return True
    if number > 1:
        for i in range(2,number):
            if (number % i) == 0:
                flag = True

    if flag:
        return True
    else:
        return False

def readFile():
    line = []
    #print("Main Worked")
    with open("text.txt","r") as file:
        line= file.readlines()
        for i in range(len(line)):
            if "\n" in line[i]:
                line[i]=line[i][:-1]
            line[i]=line[i].split(" ")
        file.close()
        for i in range(len(line)):
            for j in range(len(line[i])):
                line[i][j]=int(line[i][j])
                
    return line

def main():
    line = []
    backup=[]
    print("Main Worked")
    line=readFile()
    backup=readFile()

    for i in range(len(line)):
        for j in range(len(line[i])):
            if isPrimeNumber(int(line[i][j]))==False:
                line[i][j]=0

    flag=1
    for i in range(len(line)-1):

        for j in range(len(line[i])):
            if line[i][j]!=0:
                if line[i+1][j]!=0:
                    if backup[i+1][j]+line[i][j]>line[i+1][j]:
                        line[i+1][j]=line[i][j]+backup[i+1][j]
                if line[i+1][j+1]!=0:
                    if backup[i+1][j+1]+line[i][j]>line[i+1][j+1]:
                        line[i+1][j+1]=line[i][j]+backup[i+1][j+1]
        if sum(line[i])==0:
            print(line[i-1])
            print(max(line[i-1]))
            flag=0
    if flag==1:
        print(line)
        print(max(line[-1]))
if __name__=="__main__":
    main()