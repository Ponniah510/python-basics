#finding the loan eligiblity
salary=int(input("enter your salary :"))
age=int(input("emter your age :"))
if(salary>=2000 or age<=25):
    loanamount=int(input("how much loan you want :"))
    if(loanamount>50000):
        print("not eligible maximum loan amount is 50000")
    else:
        print("you was eligible for loan :")
else:
    print("you not eligible for loan :")
    
    