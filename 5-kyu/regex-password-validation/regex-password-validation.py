import re
​
regex = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{6,}$'
​
passwords = ["Abc123", "abc123", "ABC123", "Abc!23", "Ab1"]
​
for pwd in passwords:
    if re.match(regex, pwd):
        print(f"{pwd}: ✅ Valid")
    else:
        print(f"{pwd}: ❌ Invalid")
​