def solution(number):
    if number <= 0:
        return 0
​
    total = 0
    for i in range(1, number):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    return total
​