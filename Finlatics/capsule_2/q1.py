year=int(input("Enter year: "))

if year%4==0 and (year%400==0 or year%100!=0):
    print("{} is a leap year.".format(year))
else:
    print("{} is NOT a leap year.".format(year))