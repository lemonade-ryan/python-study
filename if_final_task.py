#1.Assume start_date = '2024-01-01' and end_date = '2024-12-31'. Write a conditional statement that checks:
#If start_date comes before end_date, print "Valid period",
#If start_date is after end_date, print "Invalid period".
#If both dates are the same, print "One-day period".
#2.Given two strings str1 and str2, write a conditional statement that checks:
#If str1 is longer than str2, print "str1 is longer".
#If str2 is longer than str1, print "str2 is longer".
#If both have equal length, print "Both are of equal length".


start_date="2024-01-01"
end_date="2023-12-31"
if start_date<end_date:
    print("valid period")
elif start_date>end_date:
    print("invalid period")
else:
    print("one day period")


str_1=(input("enter string 1:"))
str_2=(input("enter string 2:"))
if (len(str_1))>(len(str_2)):
    print("str_1 longer")
elif (len(str_1))<(len(str_2)):
    print("str_2 longer")
else:
    print("equal length")


  #  3.Given a list vali3.Given a list valid_ids = [101, 102, 103] and a variable user_id = 105, write a conditional statement that:

#Prints "Access Granted" if user_id is in valid_ids.
#Prints "Access Denied" if user_id is not in valid_ids.
#4.Given a variable value that could be of any type, write a conditional statement that:
#Prints "String Detected" if value is a string.
#Prints "Integer Detected" if value is an integer.
#Prints "Unknown Type" for any other type.
#5.Given x = 7 and y = 14, write nested conditional statements that print:
#"x and y are both even" if both x and y are even numbers.
#"Only y is even" if only y is even.
#"Neither x nor y are even" if both are odd.

valid_ids=[101,102,103]
user_id=105
if user_id in valid_ids:
    print("access accepted")
else:
    print("access denied")

input_entered=(type(85))
if input_entered==str:
    print("string detected")
elif input_entered==int:
    print("integer detected")
else:
    print("unknown type")

x=7
y=7
if y%2==0:
    if x%2==0:
        print("both y and x even")
    else:
        print("only y is even") 
else:
    if y%2==0:
        print("y is only even")
    else:
        print("neither y or x is even")           7