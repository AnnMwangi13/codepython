#forloops
numbers=[1,2,3,4,5,6,7,8,9,10]
for i in numbers:
    print(i)

for i in "subaru":
    print(i)

#break statement
for x in numbers:
    print(x)
    if x==5:
        break
#5 is not printed
for h in numbers:
    if h==5:
        continue
    print(h)

#range function
for i in range(6):
    print(i)

for i in range(2,10):
    print(i)
#(0,10,3)the last number its a sequence it adds three to every number displayed
for i in range(0,10):
    #print(i)

    if i==5:
        break
    print(i)

#nested forloop
fruits=["mangoes","oranges","Passion","apples"]
spices=["ginger","cinnamon","tumeric","masala"]

for i in fruits:
    for j in spices:
        print(i,j)
#if you dont want to print
for j in spices:
    pass











