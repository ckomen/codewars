def count(s):
    s = str(s)  # Convert input to string just in case
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count
​