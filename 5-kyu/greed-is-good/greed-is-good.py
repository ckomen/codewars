def score(dice):
    points = 0
    counts = {i: dice.count(i) for i in range(1, 7)}
    if counts[1] >= 3:
        points += 1000
        counts[1] -= 3
    for i in range(2, 7):
        if counts[i] >= 3:
            points += i * 100
            counts[i] -= 3
    points += counts[1] * 100
    points += counts[5] * 50
    
    return points
​