#Write a program that takes input of 2 values and adds them. The program should only accept numbers and floats
# # only or otherwise display an error “invalid character entered” and take the user to re-enter the inputs .



while True:
    try:
        input1=float(input("enter first number:"))
        input2=float(input("enter second number:"))
        sum=(input2+input1)
        print(f"sum of the two numbers is {sum}")
        break

    except:
        print(f"invalid character try again")   