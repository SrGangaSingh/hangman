from random_word import RandomWords
from turtle import right
from arts import stages, title

print(title)

word_list = ["ardvark", "baboon", "camel"]

lives = 7

# choose a random word
chosen_word = RandomWords().get_random_word()
# for testing purpose
print(f"psst, the chosen word is {chosen_word}")

# create blank display
display = ["_"]*len(chosen_word)
print(" ".join(display) + "\n")

while True:
    # check if player has won
    if "_" not in display:
        print("\nYour won!")
        break

    # check if player has lost
    if not lives:
        print("\nYou Lost!")
        break

    # ask the user for a letter
    guess = input("Guess a letter: ").lower()

    # if player guessed wrong
    if guess not in chosen_word:
        print(stages[7 - lives])
        lives -= 1
        continue

    # if player has already guessed the letter
    if guess in display:
        print("\n" + "You have already guessed this letter. Try something new" + "\n")
        continue

    # if player guessed right
    for i, letter in enumerate(chosen_word):
        if letter == guess:
            display[i] = letter
    print("\n" + " ".join(display) + "\n")
