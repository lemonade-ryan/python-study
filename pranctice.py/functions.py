def triangle_area(height,base):
    area=height*base*0.5
    print(area)
height=int(input("enter height:"))
base=int(input("enter base:"))

triangle_area(height,base)

def check_number(x):
    if x%2==0:
        print("even")
    else:
        print("odd")
x=int(input("enter x:"))         
check_number(x)
#create a function that checks if a number is even or odd

def area_rectangle(length,width):
    area=length*width
    print(area)
area_rectangle(20,30)    

#create a function that displays the largest number
def largestnum_check(num1,num2,num3):
    if num1>num2 and num1>num3:
        results=num1
    elif num2>num1 and num2>num3:
        results=num2
    else:
        results=num3
    print(f"{results} is the largest number")    

largestnum_check(10,20,30)                