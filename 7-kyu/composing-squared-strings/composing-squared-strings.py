def compose(s1, s2):
    s1_lines = s1.split("\n")
    s2_lines = s2.split("\n")[::-1]  # Reverse lines of s2
    n = len(s1_lines)
​
    result = []
    for i in range(n):
        new_line = s1_lines[i][: i + 1] + s2_lines[i][:(n - i)]
        result.append(new_line)
​
    return "\n".join(result)
​
# Example test cases
s1 = "abcd\nefgh\nijkl\nmnop"
s2 = "qrst\nuvwx\nyz12\n3456"
​
print(compose(s1, s2))
​