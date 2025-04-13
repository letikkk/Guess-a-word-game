import random

ranwords = ["word", "magic", "animal"]
word = random.choice(ranwords)

symbols = []
unique_letters = set(word)

while set(symbols) != unique_letters:
    guess = input("Enter a letter: ").lower()

    if guess in word and guess not in symbols:
        symbols.append(guess)

    for letter in word:
        if letter in symbols:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print()

print(f"\n🎉 You have won! Your word was: {word}")
