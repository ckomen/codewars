def sum_array(arr):
    if arr is None or len(arr) < 3:
        return 0
    return sum(arr) - min(arr) - max(arr)
​