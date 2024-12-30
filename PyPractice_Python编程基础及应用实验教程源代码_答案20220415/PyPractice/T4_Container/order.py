fruits = ['grape','pear','apple','water melon']
fruitsSorted = sorted(fruits,reverse=True)
print("fruitsSorted:",fruitsSorted)
print("fruits:",fruits)
fruits.reverse()
print("reversed fruits:",fruits)
fruits.sort(key=len)
print("sorted fruits by len:",fruits)