sentence = input("Enter a sentence: ")
alphabet = "abcdefghijklmnopqrstuvwxyz"


missing_letters = [char for char in alphabet if char not in sentence]

if not missing_letters:
    print("Your sentence is a pangram!")
else:
    print("Missing letters:", (missing_letters))
    print("Here's a pangram: ", sentence , (missing_letters))
