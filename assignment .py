#ADDITIONAL CREATIVITY WAS ADDED TO MY CODE
#I GAVE A CLUE FOR FINDING MY SECRET WORD when the user gives a word that is not the same number of words in my secret word
def generate_hint(secret_word, ques):
    hint =''
    for i in range(len(secret_word)):
        if ques[i] == secret_word[i]:
            hint += ques[i].upper()
        elif ques[i] in secret_word:
            hint += ques[i].lower()
        else:
            hint += '_'
    return hint

def word_guessing_game(secret_word):
    print('💥 Welcome to the WORD GUESSING GAME!💥\n\
      💡Your hint is:', '_' * len(secret_word))
    
    guesses = 0
    while True:
        ques = input('What is your guess? ').lower()
        if len(ques) != len(secret_word):
            print('Your guess should have the same number of letters as the secret word.')
            import time
            time.sleep(2)
            print('hint:💡my name💡')
            continue
        guesses += 1
        if ques == secret_word:
            print('Congratulations! You guessed it!')
            print('it took you', guesses, 'guesses.')
            break
        else:
            hint = generate_hint(secret_word, ques)
            print('Your hint is:', hint)
    

secret_word ='lifegate'

word_guessing_game(secret_word)



