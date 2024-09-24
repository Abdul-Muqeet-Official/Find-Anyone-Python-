n=''
print("Lets Find Someone :")
print("="*30)
l=[]
find=input("Whome do you want to find :")
print("="*30)
while n!=find:
    n=input("enter name :")
    l.append(n)
print(l)
print("found the (",l[-1],')')