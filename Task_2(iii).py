# Count the number of vowels and consonants in a string
string = input("Enter a string: ")
string_lower = string.lower()  
vowel_count = 0
consonant_count = 0
for c in string_lower:
    if c in 'aeiou': 
        vowel_count += 1
    elif c.isalpha():
        consonant_count += 1
print("Vowels:", vowel_count)
print("Consonants:", consonant_count)
