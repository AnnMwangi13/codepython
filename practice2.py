mycars=["Toyota Hilux","Benz","Audi","Mazda"]
print(mycars)
print(len(mycars))
print(mycars[1])
print(mycars[1:])

mycars[2]="Saloon"
print(mycars)

mycars.insert(2,"Probox")
print(mycars)

mycars.append("Ferrari")
print(mycars)

#adding a list to another
fruits=["mangoes","Passion","Berries","pineapples"]
mycars.extend(fruits)
print(mycars)

#remove
mycars.remove("Passion")
print(mycars)

mycars.pop(1)
mycars.pop()




#tuple...stores multiple items in a single variable
#ordered and unchangeable
houses=("Bungallows",45.9078,"21")
print(houses)
print(houses[0])


#setstores.... multiple items in a single variable
#it disarranges
#no duplicates
rooms={'shops','stores','rentals'}
print(rooms)

#dictionaries
names={"John":69,
       "Saru":70,
       "Pamella":27,
       "Rubi":16}
print(names)
print(names["Pamella"])

#or...
modify=names.get("Rubi")
print(modify)

#shows keys
storeKeys=names.keys()
print(storeKeys)

#shows values
showvalues=names.values()
print(showvalues)

#displays items
display_items=names.items()
print(display_items)

#change value
names["Pamella"]=30
print(names)
#it adds the new name if it does not find it
names["Otieno"]=28
print(names)

#converts the list to a set and vice versa
numbers=[1,2,3,4,5,6]
Set=set(numbers)
print(Set)

Set=list(numbers)
print(Set)
