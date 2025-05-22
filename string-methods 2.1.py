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

sentence=input("enter a sentense: ")
words=sentence.split(' ')
words_counted=len(words)
print(words_counted)
capitalized_sentence=sentence.title()
print(capitalized_sentence)
reversed_sentence=sentence[::-1]
print(reversed_sentence)




text="BAD habits are hard to break!"
correction=text.replace("BAD","good")
print(correction)


email="   John.Doe@GMAIL.com  "
non_spaced=email.strip()
print(non_spaced)
cleaned=non_spaced.lower()
print(cleaned)
final=cleaned.split('@')[1]
print(final)




first="john"
last="DOE"
hobby="  reaading book"
correct_first=first.capitalize()
correct_last=last.capitalize()
correct_hobby=hobby.strip()
formatted=f"My name is {correct_first} {correct_last} and I Love {correct_hobby}."
# formatted="My nam is "+correct_first+" "+
print(formatted)