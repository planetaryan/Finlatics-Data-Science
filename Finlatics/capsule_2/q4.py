integers_string=input("Enter 10 numbers: ")

list=list(map(int,integers_string.split()))

for i in list:
    if i==0:
        print("Invalid number",end="\n")

    elif i%2==0:
        print(i**2,end="\n")
    else:
        print(i**3,end="\n")
    
