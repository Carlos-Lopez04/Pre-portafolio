# Vowel Counter

# todo 1 Ask a word to the user
# todo 2 Count each vowel in the word


# * Version 1
def v1():
    word = input("\nIntroduce a word ").lower()
    vowels = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}

    for letter in word:
        if letter in vowels:
            vowels[letter] += 1

    print(f"\nAmount of vowels in the {word}")
    for vowel, amount in vowels.items():
        print(f"{vowel} => {amount}")
    print("")


# * Version 2
def v2():
    word = input("\nIntroduce a word ").lower()

    vowels = {"a", "e", "u", "i", "o"}

    count = 0
    for letter in word:
        if letter in vowels:
            count += 1

    print(f"\nThe word {word} has {count} vowels\n")


if __name__ == "__main__":
    v1()
    print("==============================")
    v2()
