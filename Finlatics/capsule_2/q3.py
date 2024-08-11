list=[]
for i in range(6):
    name=input("Enter name {}: ".format(i+1))
    list.append(name)
for name in list:
    if(name[0].lower()=='a'):
        print(name,end="\n")