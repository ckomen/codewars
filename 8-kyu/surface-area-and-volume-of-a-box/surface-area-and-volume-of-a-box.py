def get_size(w, h, d):
    surface_area = 2 * (w * h + h * d + d * w)
    volume = w * h * d
    return [surface_area, volume]  # Returning as a list
​
# Example usage:
print(get_size(2, 3, 4))  # Output: [52, 24]
​