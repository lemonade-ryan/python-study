rtemp=56.8926
result=round(temp)
print(result)


temp=56.8926
result=round(temp, 2)
print(result)


temp=56.8926
result=round(temp, 3)
print(result)


temp=56.8926
temp=str(temp)
temp=temp[3:]

print(temp)

#result=+ temp
#print(result)
#result=


temp1=111.0789
temp1=str(temp1)
temp_corr=temp1[5:]
print(temp_corr)
result=temp_corr[0:2] + "." + temp_corr[2:]
print(result)
