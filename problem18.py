#count the no which are divisble by 3 and 5
count=0
for i in range(1,100):
    if(i%3==0 or i%5==0):
        count=count+1
print("count :",count)