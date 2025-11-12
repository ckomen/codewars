from functools import lru_cache
​
@lru_cache(None)
def exp_sum(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    total = 0
    k = 1
    while True:
        g1 = k * (3 * k - 1) // 2
        g2 = k * (3 * k + 1) // 2
        if g1 > n:
            break
        total += (-1) ** (k + 1) * exp_sum(n - g1)
        if g2 <= n:
            total += (-1) ** (k + 1) * exp_sum(n - g2)
        k += 1
    return total
​
print(exp_sum(10))  # 42
print(exp_sum(100)) # 190569292
​