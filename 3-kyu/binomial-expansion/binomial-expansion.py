​
    for k in range(n + 1):
        c = comb(n, k) * (a ** (n - k)) * (b ** k)
        p = n - k  # power of variable
​
        if c == 0:
            continue
​
        # Build term
        # Coefficient formatting
        if p == 0:
            term = str(c)
        else:
            # coefficient part
            if c == 1:
                coeff = ""
            elif c == -1:
                coeff = "-"
            else:
                coeff = str(c)
​
            # variable part
            if p == 1:
                term = coeff + var
            else:
                term = coeff + var + "^" + str(p)
​
        terms.append(term)
​
    # Combine with correct +/− handling
    result = terms[0]
    for t in terms[1:]:
        if t.startswith("-"):
            result += t
        else:
            result += "+" + t
​
    return result
​