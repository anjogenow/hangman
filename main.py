import random
from words import words
import string
def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word or not word.isascii():
        word = random.choice(words)
    return word

def print_gallows(lives):
    gallows = [
    '''''',
    '''
      +---+
      |   |
          |
          |
          |
          |
    =========''',
    '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''',
    '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''',
    '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''',
    '''
      +---+
      |   |
      O   |
     /|\\  |
          |
          |
    =========''',
    '''
      +---+
      |   |
      O   |
     /|\\  |
     /    |
          |
    =========''',
    '''
      +---+
      |   |
      O   |
     /|\\  |
     / \\  |
          |
    ========='''
    ]
    print("\n" + gallows[7-lives])

def hangman():
    word = get_valid_word(words).upper()
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 7
    while len(word_letters)>0 and lives > 0:
        print_gallows(lives)
        print(f"\nDu hast noch {lives} Leben und Du hast diese Buchstaben verwendet:", " ".join(used_letters))

        # What current Word is ( W _ R D )
        word_list = [letter if letter in used_letters else "_" for letter in word]
        print("Gesuchtes Wort:", " ".join(word_list))

        user_letter = input("Rate einen Buchstaben: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1
                print("Buchstabe ist nicht im Wort!")
        elif user_letter in used_letters:
            print("Du hast den Buchstaben schon geraten!")
        else:
            print("Keine valide Eingabe!")
    if lives == 0:
        print_gallows(lives)
        print("Oh nein, du hängst :(( \nDas Wort war:", word)
    else:
        print("Du hast das Wort richtig erraten, es war", word)

hangman()

