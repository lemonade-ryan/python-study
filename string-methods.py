text=" learn python"
format=text.strip().title()
print(format)

text="hello"
reverse=text[::-1]
print(reverse)

sentense="python is fun"
replaced=sentense.replace(" ","_")
print(replaced)

text="biovolt is very important"
vowels="aeiouAEIOU"
count=sum(1 for char in text if char in vowels)
print(count)

text="electricity"
last_three=text[-3:]
print(last_three)

sentense=input("enter a sentense: ")
words=sentense.split()
words_counted=len(words)
print(words_counted)
capitalized_sentense=sentense.title()
print(capitalized_sentense)
reversed_sentense=sentense[::-1]