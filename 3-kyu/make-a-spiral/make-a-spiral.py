def spiralize(n):
    grid = [[0]*n for _ in range(n)]
​
    dirs = [(0,1),(1,0),(0,-1),(-1,0)]
    d = 0
    r, c = 0, 0
    grid[r][c] = 1
​
    def can_move(nr, nc):
        if not (0 <= nr < n and 0 <= nc < n): 
            return False
        if grid[nr][nc] == 1:
            return False
​
        # anti-touching rule
        # check 4-neighbors except the cell we're coming from
        for dr, dc in dirs:
            ar, ac = nr + dr, nc + dc
            if 0 <= ar < n and 0 <= ac < n and grid[ar][ac] == 1:
                # allow only **if** it’s the previous cell (r,c)
                if not (ar == r and ac == c):
                    return False
        return True
​
​
    while True:
        nr, nc = r + dirs[d][0], c + dirs[d][1]
​
        if not can_move(nr, nc):
            # turn right
            d = (d + 1) % 4
            nr, nc = r + dirs[d][0], c + dirs[d][1]
            if not can_move(nr, nc):
                break
​
        r, c = nr, nc
        grid[r][c] = 1
​
    return grid
​