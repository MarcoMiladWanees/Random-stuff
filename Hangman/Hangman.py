from Wordlist import words
import random

hangman = {0: ("   ",
               "   ",
               "   "),
           1: (" 0 ",
               "   ",
               "   "),
           2: (" 0 ",
               " | ",
               "   "),
           3: (" 0 ",
               "/| ",
               "   "),
           4: (" 0 ",
               "/|\\",
               "   "),
           5: (" 0 ",
               "/|\\",
               "/  "),
           6: (" 0 ",
               "/|\\",
               "/ \\")
           }
word = random.choice(words)
word = list(word)
spaces = ["_" for _ in range(len(word))]

guesses = 0
while guesses < 6:
    print("*************************************")
    print("You have ",6 - guesses," guesses left")
    print("*************************************")
    for x in hangman.get(guesses):
        print(x)
    print(" ".join(spaces), end="\n\n")
    guess = input("Guess a letter: ")
    if guess.lower() in word:
        for i, letter in enumerate(word):
            if letter == guess.lower():
                spaces[i] = guess.lower()
        print("Correct!")
    else:
        guesses += 1
        print("Try again!")
    print()
    if spaces == word:
        print("Congratulations! You guessed the word!")
        print("You win!")
        print("The word was", "".join(word))
        break
    elif guesses == 6 and spaces != word:
        for x in hangman.get(guesses):
            print(x)
        print("You lose!")
        print("The word was ", "".join(word))

