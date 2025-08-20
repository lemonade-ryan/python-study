fruits=('apple','banana','orange')
for i in fruits:
    print(i)
    #iterate through numbers from 20 to 40
numbers=list(range(0,101))
print(numbers)

for i in (range(20,41)):
    print(i)



numbers=list(range(20,41))
for num in numbers:
    if num%2==0:
        print(num)


numbers=list(range(100,201))
for num in numbers:
    if num%2!=0:
       print(num)

#store even numbers in 100 to 200 in a listfor i in range(100,201)
even_numbers=[]
numbers=list(range(100,201))
for num in numbers:
    if num%2==0:
        even_numbers.append(num)
print(even_numbers)



odd_numbers=[]
for i in range(200,301):
    if i%2!=0:
        odd_numbers.append(i)
print(odd_numbers)     



for i in range(1,50):
    if i==40:
        break
    print(i)        



    


