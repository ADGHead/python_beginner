def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
        
    return translation

print(translate(input("Enter a phrase")))
    
word = input("Enter a Phrase")
letter = ""

for i in word:
    if i in "AEIOUaeiou":
        letter = letter + "g"
        
    else:
        letter = letter + i
    
print(letter)
