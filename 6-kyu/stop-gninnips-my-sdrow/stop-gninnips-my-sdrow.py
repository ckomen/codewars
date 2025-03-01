def spin_words(sentence):
    return " ".join([word[::-1] if len(word) >= 5 else word for word in sentence.split()])
​
# Example test cases
print(spin_words("Hey fellow warriors"))  # "Hey wollef sroirraw"
print(spin_words("This is a test"))       # "This is a test"
print(spin_words("This is another test")) # "This is rehtona test"
​