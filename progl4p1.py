s = input("Enter a sentence: ") 
words = s.replace(",", "").replace(".", "").split ()
palindrome_count = 0
for word in words:
    if word.lower() == word[::-1].lower():
        palindrome_count += 1
print("Total number of palindrome words in a sentence: ", palindrome_count)