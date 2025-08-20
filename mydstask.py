my_ds=[23,"Jane",560,["Lesson","Maths",{"currency":"KSH"}],987,(76,"John")]
print(my_ds[3][2]["currency"])
print(my_ds[2])
print(my_ds[3][1])
my_ds[3][2]["amount"]=90
print(my_ds)
print(my_ds[4])
number=(my_ds[4])
number_str=str(number)
reversed_number=(number_str[::-1])
print(reversed_number)
my_ds[4]=reversed_number
print(my_ds)
print(my_ds[5])
list_con=list(my_ds[5])
print(list_con)
list_con[1]="Jane"
print(list_con)
list_con=tuple(list_con)
print(list_con)
#my_ds(5)=list_con
#print(my_ds)


