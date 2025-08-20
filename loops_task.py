#Write a program that displays a numbers 1 to 50 inside a list.
#From 1 above display the ones divisible by 7 or 5 inside a list.
#Find sum and average of values in the range between 10 to 40.
#Put in a list the first 10 odd numbers between 10 to 50. 
#write a program that takes a number as input and prints its multiplication table up to 10 using a for loop.
#write a program that counts and prints the number of even numbers between 1 and 50 using a for loop
#ls1 = [ (“Jay”, 20), (“Mo”, 30), (“Mya”, 32) ]
#Display the total quantity of the 3 above.



#number=(list(range(1,51)))
#print(number)
#final=[]
#for i in number:
#    if i%7==0 or i%5==0:
#        final.append(i)
#print(final)

#Write a program that displays a numbers 1 to 50 inside a list.
#From 1 above display the ones divisible by 7 or 5 inside a list.
#Find sum and average of values in the range between 10 to 40.

numbers=list(range(10,41))
sum=0
for num in numbers:
    sum=sum+num
print(sum)
avarage=sum/len(numbers)
print(avarage)




    






#Put in a list the first 10 odd numbers between 10 to 50. 
#numb=list(range(10,51))
#lst=[]
#for i in numb:
#    if i%2!=0:
#        if len(i)==10:
#            break
#        lst.append(i)

        


#print(lst)










#write a program that takes a number as input and prints its multiplication table up to 10 using a for loop.
number=(int(input("enter number")))
table=(number)
for i in range(1,11):
    table=table*i
print(table)



#write a program that counts and prints the number of even numbers between 1 and 50 using a for loop
#ls1 = [ (“Jay”, 20), (“Mo”, 30), (“Mya”, 32) ]
#Display the total quantity of the 3 above.


