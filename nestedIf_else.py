"""age=int(input("Enter your age: "))
if age<13:
    print("You are a child")
elif  age>13 and age<20:
    print('You are a teenager')

else:print("You are an adult")"""

#shorthand
a=89
b=67
c=45
print("a ")if a<b  else print("a is equal to b")if a==b  else print("b")
#finding the largest number
if a>b and a>c:
    print("a is the largest number")
elif b>a and b>c:
    print("b is the largest number")

elif c>a and c>b:
    print("c is the largest number")

else :
    print("The numbers are equal")

#buit_in function for(maximum)
print (max(a,b,c))



a= int(input("Enter any number:"))
if a>=1 :
    print("This is a positive number")
else:
    print("It is zero")

