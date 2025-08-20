#TASK 5: Using Python or PHP or Java or Ruby or JavaScript
#Implement a program that takes 3 users  inputs from the terminal or the Browser, and stores them in three variables. Return the largest of the three. Do this without using the the inbuilt max () function!
#The goal of this exercise is to think about some internals that programs normally take care of for us. 

num1=(int(input("enter first number:")))
num2=(int(input("enter second number:")))
num3=(int(input("enter third number:")))
if num1>num2 and num1>num3:
    print("num 1 is the largest number")
elif num2>num1 and num2>num3:
    print("num 2 is the largest number")
else:
    print("num 3 is the largest number")
        