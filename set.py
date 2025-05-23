numbers={10,20,30,40,50,10,20}
print(type(numbers))
print(numbers)
numbers.add(1000)
print(numbers)



days={"monday","tuesday","wenesday","thursday","friday","sunday","sunday","sartday"}
print(days)
print(list(days))
days.remove("friday")
print(days)
days.remove("sartday")
print(days)
days.add("sunday")
print(days)




x={1,2,3,4,5,6,7}
y={5,6,7,8,9,10}
#z=x.difference(y)
#z=x.union(y)
#z=x.symmetric_difference(y)
z=x.intersection(y)
print(z)
