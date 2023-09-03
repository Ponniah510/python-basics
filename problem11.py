maths=int(input("enter your maths mark :"))
ip=int(input("enter your ip mark :"))
ml=int(input("enter your ml mark :"))
gis=int(input("enter your gis mark :"))
ooad=int(input("enter your ooad mark :"))
totalmarks=maths+ip+ml+gis+ooad
print("total marks :",totalmarks)
averagemarks=totalmarks/5
print("average marks :",averagemarks)
if(averagemarks<35):
    print("extra class is required :")
else:
    print("you are good to go :")