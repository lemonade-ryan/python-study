student={
          "name":"Alex",
          "email":"alex@gmail.com",
          "age":30,"name":"brian"}


print(type(student))
print(student)
#accessing values in a dictioonary
print(student["name"])
student["name"]="ryan"
print(student)
student["occupation"]="engineer"
print(student)
student["location"]={"town":"nakuru","address":1020,"street":"kimathi"}
print(student)
print(student["location"]["street"])
student["skills"]=["leadership","coding","teamplayer"]
print(student)
print(student["skills"][1])