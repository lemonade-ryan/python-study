# Using Python or PHP or Java or Ruby or JavaScript
#Write that prompts the user to input student marks. The input should be between 0 and 100.Then output the correct grade: 
#A > 79 , B - 60 to 79, C  > 49 to 59, D - 40 to 49, E - less 40
student_marks=(int(input("enter student marks (should be between 0-100):")))
if student_marks>79:
    print("A")
elif student_marks>=60 and student_marks<=79:
    print("B")
elif student_marks>49 and student_marks<=59:
    print("C")
elif student_marks>=40 and student_marks<=49:
    print("D")
else:
    print("E")                