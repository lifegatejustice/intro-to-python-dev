print('💥 Welcome to the word guessing game!💥\n\
      💡Your Hint is _ _ _ _ _ _ _ _')

secret = 'lifegate'
l = 

ques = input('What is your guess? ')

while ques != secret.lower():
    print(f'Your guess was not correct.\n\
          💡Your Hint is _ _ _ _ _ _ _ _')
    ans = input('What is your guess ')
for letter in secret:
    print(f'Your Hint is _ _{ques}')

for letter in secret:
    if letter.lower() == ques.lower():
        print(letter.upper(), end="")
    else:
        print(letter.lower(), end="")
for letter in secret:
    if letter.lower() == ques.lower():
        print("_", end="")
    else:
        print(letter.lower(), end="")
print()        


print()