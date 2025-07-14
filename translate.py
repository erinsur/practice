vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in vowels:
            translation += 'g'
        else:
            translation += letter
    return translation

        
    

phrase = input("Enter a phrase to be translated: ")
trans = translate(phrase)
print(phrase + " -->  "+ trans)
