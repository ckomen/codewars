def rot13(text):
    result = []
    
    for char in text:
        if 'A' <= char <= 'Z':  
            shifted = chr((ord(char) - ord('A') + 13) % 26 + ord('A'))
            result.append(shifted)
        elif 'a' <= char <= 'z': 
            shifted = chr((ord(char) - ord('a') + 13) % 26 + ord('a'))
            result.append(shifted)
        else:
            result.append(char)
    
    return ''.join(result)
​
​