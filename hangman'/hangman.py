import random
import string
from words import words

def get_valid_word(words):
    word = random.choice(words)
    while " " in word or "-" in word:
        word=random.choice(word)
    return word.upper()

def hangman():
    word =get_valid_word(words)
    word_letters=set(word)
    used_letters=set() #letters gussed by the user
    alphabet=set(string.ascii_uppercase)
    lives=len(word)

    #get a letter from user
    while len(word_letters)>0 and lives>0:
        print(f"You have {lives} lives left and you have gussed ", " ".join(used_letters))

        word_list=[letter if letter in used_letters else "*" for letter in word] #list of letters in the word and gussed correctly
        print("Current word "," ".join(word_list))
        user_letter= input("Guess a letter ").upper()
        
        if user_letter in alphabet-used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives=lives-1
        
        elif user_letter in used_letters:
            print("You have already gussed this letter. Try again ")
        
        else:
            print("Invalid letter Try again ")

    #come here when len(word_letters)==0 or lives = 0
    if lives==0:
        return f"You are dead . Correct word was {word}"
    else:
        return f" Yay!! You have gussed {word} correctly"


print(hangman())