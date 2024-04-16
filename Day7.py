#Step 1 
import random
from hangman_words import word_list
logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

levels = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

print(logo)
the_end = False
chosen_word = random.choice(word_list)
lives = 6
print(levels[6])

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#creating blanks
display = []
for letter in chosen_word:
    display += ["_"]


while not the_end:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(0 , len(chosen_word)):
        letter = chosen_word[position]

        if guess == letter:
            display[position] = letter

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            the_end = True
            print("You lose.")


    if "_" not in display:
        the_end = True 
        print("You win.")
    print(levels[lives])

    #Join all the elements in the list and turn it into a string.
    print(f"{' '.join(display)}")
