# Trolls are attacking your comment section!
# A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.
# Your task is to write a function that takes a string and return a new string with all vowels removed.
# For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".

def disemvowel(string):
    new_string = ""
    vowels = "aeiou"
    for char in string: # Iterate through every character in the string
        is_vowel = False
        for vowel in vowels: # Compare every character in the string to every vowel
            if char.lower() == vowel: # If the character is a vowel, end the loop
                is_vowel = True
                break
        if is_vowel: # If the character is a vowel continue to the next character 
            continue
        else: 
            new_string += char #Otherwise add that character to the new string
    return new_string

print(disemvowel("This website is for losers LOL!"))

# Bounus: Don't create new string
def disemvowel(string):
    vowels = "aeiou"
    for vowel in vowels:
        string = string.replace(vowel.lower(), "")
    return string

print(disemvowel("This website is for losers LOL!"))
