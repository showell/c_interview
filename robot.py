def compute_spiral_area(movements):
    i = 0
    max_x = 0
    min_x = 0
    max_y = 0
    min_y = 0
    x = 0
    y = 0
    while True:
        if i >= len(movements): break
        x += movements[i]
        if x > max_x: max_x = x
        i += 1
        if i >= len(movements): break
        y += movements[i]
        if y > max_y: max_y = y
        i += 1
        if i >= len(movements): break
        x -= movements[i]
        if x < min_x: min_x = x
        i += 1
        if i >= len(movements): break
        y -= movements[i]
        if y < min_y: min_y = y
        i += 1
    return (max_x - min_x) * (max_y - min_y)

input = [4,3,5,4,10]
print compute_spiral_area(input)
