numbers=[]
numbers.append(int(input("enter first number: ")))
numbers.append(int(input("enter second number: ")))
numbers.append(int(input("enter third number: ")))

largest=max(numbers)
print(largest)

x=int(input("enter value for x:"))
y=int(input("enter value for y: "))
conditions=[10<=x<=20,y>100]
if all(conditions):print("condition met")
else:print("conditions not met")