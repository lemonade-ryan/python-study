#Write a program that:
#Takes a transaction amount and account type ("Standard" or "Premium") as input.
#If the account type is "Standard":
#If it is, print "Transaction exceeds the limit for Standard accounts."
#If not, print "Transaction approved."
#If the account type is "Premium":
#Check if the amount is above 1,000:
#If it is, print "Transaction exceeds the limit for Premium accounts."
#If not, print "Transaction approved."




account_type=(input("enter account type  standard/premium:".casefold()))
if account_type=="standard":
    ammount=(int(input("enter ammount:")))
    if ammount>500:
        print("transaction exceed the limit of standard account")
    else:
        print("transaction approved")

if account_type=="premium":
    ammount=(int(input("enter amount:")))
    if ammount>1000:
        print("transaction exceed the limit for premium account")
    else:
        print("transaction approved")





