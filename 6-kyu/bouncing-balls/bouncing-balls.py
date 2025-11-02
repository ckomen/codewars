def bouncing_ball(h, bounce, window):
    # Check conditions
    if not (h > 0 and 0 < bounce < 1 and window < h):
        return -1
    
    count = 1  # The first fall
    height = h * bounce
    
    while height > window:
        count += 2  # One going up, one coming down
        height *= bounce  # Next bounce height
    
    return count
​