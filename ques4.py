year=int(input ("enter the year"))
if year%1000==0:
    if year%400==0:
        print("it is a leap year")
    else:
        print("it is not a leap year")
elif year%4==0:
    print("it is a leap year")
else:
    print("it is not a leap year")
