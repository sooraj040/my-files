first_word = input("First word: ").lower().replace(" ", "")
second_word = input("Second word: ").lower().replace(" ", "")

if sorted(first_word) == sorted(second_word):
    print("The words are anagrams.")
else:
    print("The words are not anagrams.")
