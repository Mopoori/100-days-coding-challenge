text = input("Enter a sentence: ")
words = text.split()
reversed_words = words[::-1]
result = " ".join(reversed_words)
print("Reversed Sentence:", result)