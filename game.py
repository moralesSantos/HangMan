import random

stages = ['''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========
''','''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========
''',
'''
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========
''',
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
  |   |
      |
      |
=========
''',
'''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''',
'''
  +---+
  |   |
      |
      |
      |
      |
=========
''',
]

words = ["apple","banana","target"]
chosen_word = random.choice(words)
placeholder = []
guessed_letters = set()
word_length = len(chosen_word)

for i in range(word_length):
    placeholder.append("_")

lives = 6

def validate(guess, guessed_letters):
    if guess in guessed_letters:
        return False,"You already guessed that: Try a different letter"
    if not guess.isalpha():
        return False, "Only try letter no numbers please."
    if not len(guess) == 1:
        return False,"Please only type 1 letter"
    return True,""


def display_hangman(lives):
    print(stages[lives])

def update_placeholder(guess):
    for i ,letter in enumerate(chosen_word):
        if letter == guess:
            placeholder[i] = guess




while lives > 0:
    print(' '.join(placeholder))

    guess_letter = (input("Guess a letter: ")).lower()

    is_valid, feedback = validate(guess_letter,guessed_letters)
    if not is_valid:
        print(feedback)
        continue
    guessed_letters.add(guess_letter)
    update_placeholder(guess_letter)


    if guess_letter not in chosen_word:
        lives -= 1
        print(f"Unlucky: You now have {lives} left.")
    else:
        print(f"Good guess: \"{guess_letter}\" is in the word")

    print("Guessed letters so far : " + ",".join(guessed_letters))


    if "_" not in placeholder:
        print(f"You won!!! Congrats the word was: {chosen_word} ")
        break
    display_hangman(lives)

if lives == 0:
    print(f"You lost! The word was '{chosen_word}'. Better luck next time!")

