import random

languages = ["python", "c", "c++", "java", "javascript", "sql", "r", "assemblylanguage", "ruby", "fortran"]
ice_cream = ["chocolate", "moosetracks", "vanilla", "strawberry", "chocolatechip", "blackberry", "peanutbutter", "raspberry", "caramel", "butterpecan"]
flowers = ["rose", "tulip", "lily", "iris", "sunflower", "lotus", "rosemary", "jasmine", "dahlia", "daisy"]

words = languages + ice_cream + flowers
random_word = random.choice(words)

print("Welcome to the word guessing game!")

if random_word in languages:
    print("Hint: it is a programming language!")
elif random_word in ice_cream:
    print("Hint: it is an ice cream flavor")
else:
    print("Hint: it is a flower")

chances = 5
user_guess = ''

while chances > 0:
    wrong_guess = 0
    for ch in random_word:
        if ch in user_guess:
            print(ch, end='')
        else:
            wrong_guess += 1
            print('_', end='')

    if wrong_guess == 0:
        print("\nCongrats! You Won The Game...")
        play_again = input('Do you want to play again? Enter 1 to play again, 0 to quit: ')
        if play_again == '1':
            random_word = random.choice(words)
            chances = 5
        elif play_again == '0':
            quit()

    user_guesses = input("Enter your guess: ")
    user_guess += user_guesses.lower()

    if user_guesses not in random_word:
        chances -= 1
        print(f'Wrong! You have {chances} more chances')
        if chances == 0:
            print(f'Game over! You lose the game. \nThe word was: {random_word}')
            play_again = input('Do you want to play again? Enter 1 to play again, 0 to quit: ')
            if play_again == '1':
                random_word = random.choice(words)
                chances = 5
            elif play_again == '0':
                quit()
