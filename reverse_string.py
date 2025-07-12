# Reverse string

# todo 1 Don't use [::-1]
# todo 2 Find another methods to do the program


# * No parameters
def v1():
    word = input("\nIntroduce a word\n")
    reversed_word = ""
    # * Loop to search the index in the last letter, to stop and decrease to the other letter
    for w in range(len(word) - 1, -1, -1):  # [index,limit,decrease]
        reversed_word += word[w]
    print(f"""\nThe word {word} was reverted into {reversed_word}\n""")
    return reversed_word


# * With parameters
def v2(word):
    reversed_word = ""
    for w in range(len(word) - 1, -1, -1):
        reversed_word += word[w]
    print(f"""\nThe word {word} was reverted into {reversed_word}\n""")
    return reversed_word


# * Changing indexes
def v3(word):
    l = list(word)

    # Initialize pointers
    left, right = 0, len(l) - 1

    while left < right:
        l[left], l[right] = l[right], l[left]
        left += 1  # Increase
        right -= 1  # Decrease
    result = "".join(l)
    print(f"""\nThe word {word} was reverted into {result}\n""")
    return result


# * Recursion
# Return the whole word/phrase by parts
def v4(phrase):
    if len(phrase) <= 1:
        return phrase
    result = phrase[-1] + v4(phrase[:-1])
    print(f"""\n{phrase} was reverted into {result}\n""")
    return result


if __name__ == "__main__":
    v1()
    print("==============================")

    word = input("\nIntroduce a word\n")
    v2(word)
    print("==============================")

    word = input("\nIntroduce a word\n")
    v3(word)
    print("==============================")

    phrase = input("\nIntroduce a word or sentence\n")
    v4(phrase)
