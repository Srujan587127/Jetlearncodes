def is_pangram(sentence):
    
    letter_set = set()
    
    
    alphabet_set = set("abcdefghijklmnopqrstuvwxyz")
    
    
    for char in sentence.lower():
        if 'a' <= char <= 'z':  
            letter_set.add(char)
    
   
    if letter_set == alphabet_set:
        print("The sentence is a pangram.")
    else:
        print("The sentence is NOT a pangram.")


sentence = input("Enter a sentence: ")
is_pangram(sentence)
