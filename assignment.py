n=1
while n<=10:
    print(n)
    n+=1


numbers=(10,20,200,5,8,150)
largest=numbers[0]

for i in numbers:
    if i>largest:
        largest=i
print(largest)
