vowels = ['a', 'e', 'i', 'o', 'u']
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
punctuation = [',', ';', '.', '?', '!']

#Receive input
char = input('Please enter a character: ').lower()

if char in vowels:
    print(f"The character '{char}' is a vowel")

elif char in digits:
    print(f"The character '{char}' is a digit")

elif char in punctuation:
    print(f"The character '{char}' is punctuation")

else:
    print(f"The character '{char}' is a consonant")