pasword="admin123"
attempts=4
for x in range(1,attempts+1):
    password=input("enter password")
    if password==pasword:
        print("access granted")
        break

    else:
        remaining_attempt=(attempts-x)
        if remaining_attempt>0:
            print(f"try again{remaining_attempt} remaining attempt")
        else:
             print("account bloacked")   