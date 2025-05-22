fruits=["apple","banana","oranges","lemons","grapes"]
print(fruits[3])
print(fruits[1:4])


my_list=[10,20,30,'python','HTML']
my_list[3]='java'
print(my_list)
print(len(my_list))

my_list.append('200')
print(my_list)

my_list.append(1000)
print(my_list)

#my_list.clear()


x=my_list.copy()
print(x)
my_list.insert(1,99)
print(my_list)
y=[567,223,453]
my_list.extend(y)
print(my_list)
my_list.remove(20)
print(my_list)

my_list.pop(3)
print(my_list)

my_list.reverse()
print(my_list)
m=[44,55,66,77]
m.sort()
print(m)
m.sort