#get input of a and b and print the range of a to b inside the function
a=int(input())
b=int(input())
def printrange():
    for i in range(a,b):
        print(i,end=" ")
printrange()