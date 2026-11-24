# Palindrome Checker
# Checks whether a word or phrase reads the same forward and backward.

text = input("Enter a word or phrase: ")
cleaned_text = text.replace(" ", "").lower()

if cleaned_text == cleaned_text[::-1]:
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")
