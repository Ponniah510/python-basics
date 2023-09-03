#print n natural number and their sum
naturalno=[]
print("enter the no :")
for i in range(1,8):
    num=int(input())
    naturalno.append(num)
print(naturalno)
sum=0
for i in naturalno:
    sum=sum+i
print(sum)