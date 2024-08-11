name=input("Enter your name ")
print("Hello",name)
print("Enter values for a and b ")
a=int(input())
b=int(input())
print("Original values: a={},b={}".format(a,b))
temp=a
a=b
b=temp

print("New values: a={},b={}".format(a,b))