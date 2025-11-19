def fib(n):
    if n == 0:
        return 0
​
    # Handle negative index using F(-n) = (-1)^(n+1) * F(n)
    if n < 0:
        n_pos = -n
        f = fib(n_pos)
        return -f if (n_pos % 2 == 0) else f
​
    return _fib_fast_doubling(n)[0]
​
​
def _fib_fast_doubling(n):
    if n == 0:
        return (0, 1)
​
    a, b = _fib_fast_doubling(n >> 1)
    c = a * ((b << 1) - a)
    d = a * a + b * b
​
    if n & 1 == 0:
        return (c, d)
    else:
        return (d, c + d)
​