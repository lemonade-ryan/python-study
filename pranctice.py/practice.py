#Write a program that displays a numbers 1 to 50 inside a list.
#From 1 above display the ones divisible by 7 or 5 inside a list.
#Find sum and average of values in the range between 10 to 40.
#Put in a list the first 10 odd numbers between 10 to 50. 
#write a program that takes a number as input and prints its multiplication table up to 10 using a for loop.
#write a program that counts and prints the number of even numbers between 1 and 50 using a for loop
#Display the total quantity of the 3 above.




numbers=list(range(1,51))
print(numbers)
x=[]
for num in numbers:
    if num%7==0 or num%5==0:
        x.append(num)
print(x)

total_num=list(range(10,41))
sum_num=sum(total_num)
print(total_num)

 


