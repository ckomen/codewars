def sum_strings(a: str, b: str) -> str:
    a = a.lstrip('0') or '0'
    b = b.lstrip('0') or '0'
    max_len = max(len(a), len(b))
    a = a.zfill(max_len)
    b = b.zfill(max_len)
    
    carry = 0
    result = []
    for i in range(max_len - 1, -1, -1):
        total = int(a[i]) + int(b[i]) + carry
        carry = total // 10
        result.append(str(total % 10))
    
    if carry:
        result.append(str(carry))
    return ''.join(result[::-1]).lstrip('0') or '0'
​