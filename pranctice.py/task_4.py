#Using Python or PHP or Java or Ruby or JavaScript
#Write a program which accepts email as form input or from terminal. Validate the email by checking if it's a valid email. 
email=(input("enter email:"))
if "@" in email and "." in email:
    print("correct email")
else:
    print("incorrect email")    