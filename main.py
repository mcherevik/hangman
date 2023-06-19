from random import *

word_list = ['beet', 'revolution', 'yard', 'affair', 'vanity', 'license', 'depth', 'soap', 'television', 'people', "center",
             'gulf', 'zebra', 'eagle', 'tinker', 'faint', 'oak', 'maelstrom', 'narcissus', 'whale', 'kernel']


def get_word():
    return choice(word_list).upper()


# function to get current stage
def display_hangman(tries):
    stages = [  # final stage: head, body, two arms, two legs
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # head, body, two arms, one leg
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # head, body and two arms
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # head, body and one arm
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # head and body
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # head
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # initial stage
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]


def check_letter():
    while True:
        guess = input()
        if not guess.isalpha():
            print('This is not a letter! Try again')
        else:
            return guess


def play(word):
    word_completion = '_' * len(word)  # string with _ symbols for each letter of the hidden word
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6

    print("Let's play Hangman!")
    print(display_hangman(tries))
    print(word_completion)
    while not guessed:
        print("Enter a letter")
        guess = check_letter().upper()
        if guess in guessed_letters:
            print("You have already guessed this letter")
            continue
        elif guess in word:
            print("Hooray! There is such a letter in this word")
            guessed_letters.append(guess)
            for i in range(len(word)):
                if word[i] == guess:
                    word_completion = word_completion[:i] + guess + word_completion[i + 1:]
            print(word_completion)
            if '_' not in word_completion:
                print("Congratulations! You have guessed the word")
                guessed_words.append(word)
                guessed = True
        else:
            print("Ooops! We don't have such a letter in this word")
            guessed_letters.append(guess)
            tries -= 1
            print(display_hangman(tries))
            if tries == 0:
                print("Oh no! You lose!")
                print(f'We guessed the word {word}')
                break


def check_answer():
    while True:
        print('Do you want to play once more? Y/N')
        answer = input().upper()
        if answer == 'Y':
            return True
        elif answer == 'N':
            print('It was nice to play with you! Bye!')
            return False
        else:
            print("We don't understand your answer. Please try again")
            continue


while True:
    play(get_word())
    if check_answer():
        continue
    else:
        break
