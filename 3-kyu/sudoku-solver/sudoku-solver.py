            for c in range(box_col, box_col + 3):
                if puzzle[r][c] == num:
                    return False
​
        return True
​
    def solve():
        empty = find_empty()
        if not empty:
            return True  # Solved
​
        row, col = empty
        for num in range(1, 10):
            if is_valid(num, row, col):
                puzzle[row][col] = num
                if solve():
                    return True
                puzzle[row][col] = 0
​
        return False
​
    solve()
    return puzzle
​