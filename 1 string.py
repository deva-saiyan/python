word = "hellow world"

print(len(word))
print(type(word))

cap= word.upper()

print(cap.lower())
print(cap.capitalize())

c = word.replace('hellow' , 'how')

print(c.strip(),'\n',len(c))

print(word[0:2].upper())
print(word[1:-1])




# Take input from the user
text = "Enter a sentence "


words = " ".join(text.split()[::-1])

print(words[0:5].title())
print(words[1:-1].upper())


