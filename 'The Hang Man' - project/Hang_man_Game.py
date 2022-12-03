

#All Imports
import random
from replit import clear
from hangman_words import word_list
from hangman_art import logo,stages

#choose a rondom word from the word list and check its length(num of word)
word_list = word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

#Create blanks
display = []
for _ in range(word_length):
    display += "_"
number_of_letter = len(display)

#print the logo of the game
print(logo)
#Testing code
print(f'Pssst, the chosen word have {number_of_letter} letter.\n{display}')


while not end_of_game:
    """
        checking if the input's letter from the user is corect, if yes then add to the blanked lis insted 
        the blanked ('_') in the right position of the letter in the word.
        while all the blanked didnt changed or the lives didnt decrease to 0 the game its still playing! 
    """
    guess = input("Guess a letter: ").lower()

    clear()
    #TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
    if(guess in display):
      print(f"You've alredy guessed {guess}")
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        #TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print(f"You guessed {guess}, that's not in the word. You lose a life. \n\nThe word was: {chosen_word}")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print(f"You win. \nThe word is: {chosen_word}")

    print(stages[lives])