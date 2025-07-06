# Palindrome checker

# todo 1 Ask to the user to write a word
# todo 2 Verify if the word is a palindrome word

word = input("\nIntroduce a word \n")

palindrome = "".join(reversed(word))

if palindrome == word:
    print(f"\nThe word {word} is the same inverted ==> {palindrome}\n")
else:
    print(f"\nThe word {word} is not a palindrome word\n")
