
numbers_1=(int(input("enter first number:")))
numbers_2=(int(input("enter second number:")))
numbers_3=(int(input("enter third number:")))

if numbers_1>numbers_2 and numbers_1>numbers_3:
    print(f"{numbers_1} is the largest number")
elif numbers_2>numbers_1 and numbers_2>numbers_3:
    print(f"{numbers_2} is the largest number")
else:
    print(f"{numbers_3} is the largest number")



no_1=(int(input("enter first number:")))
no_2=(int(input("enter second number")))
no_3=(int(input("enter third number:")))
no_4=(int(input("enter fourth number:")))

if no_3<no_1>no_2 and no_1>no_4:
    print(f"{no_1} is the largest number")
elif no_1<no_2>no_3 and no_2>no_4:
    print(f"{no_2}is the largest number")
elif no_2<no_3>no_4 and no_3>no_1:
    print(f"{no_3}is the largest number")
else:
    print(f"{no_4} is the largest number")



temp_taken=(int(input("enter temp:")))
if temp_taken>30:
    print("temp too high")
elif temp_taken>15 and temp_taken<30:
    print("temp normal")
else:
    print("temperature cold")


cor_password="secret123"
password=(input("enter password:"))
if password==cor_password:
    print("access granted")
else:
    print("access denied") 

score=(int(input("enter student score:")))
attendance=(int(input("enter student score:")))
if score>90:
    if attendance>80:
        print("excellent student")
    else:
        print("good score but attendance needs improvement")
            
      