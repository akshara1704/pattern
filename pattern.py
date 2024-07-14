l1=[]
l2=[]
elements=int(input("enter number of elements appears in both list= "))
for i in range(0,elements):
    numbers=int(input("enter the numbers= "))
    l1.append(numbers)
for j in range(0,elements):
    names=input("enter the names= ")
    l2.append(names)
print("numbers list= ",l1,end=" ")
print("and names list= ",l2)
for k in range(0,elements):
    for m in range(1,l1[k]+1):
        print(l2[k],m)
'''lnum=[]
lname=[]
elements=int(input("enter number of elements"))
def number(elements):
    if elements>0:
        numb=int(input("enter numbers="))
        lnum.append(numb)
        elements=elements-1
        number(elements)
number(elements)
def name(elements):
    if elements>0:
        names=input("enter names=")
        lname.append(names)
        elements=elements-1
        name(elements)
name(elements)
print("number list= ",lnum,"name list= ",lname)
def pattern(elements,i,k):
    if elements>0:
        if lnum[i]>0:
            print(lname[i],k)
            i=i-1
            k=k+1
        elements=elements-1
        pattern(elements,i,k)
pattern(elements,0,0)

