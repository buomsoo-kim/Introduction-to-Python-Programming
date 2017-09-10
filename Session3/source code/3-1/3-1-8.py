heights = []
total_heights = 0
for i in range(9):
    height = int(input())
    heights.append(height)
    total_heights += height

import itertools
combinations = itertools.combinations(heights, 2)
for combination in combinations:
    height_sum = total_heights
    for i in combination:
        height_sum -= i
    if height_sum == 100:
        for i in combination:
            heights.remove(i)
        break

heights.sort()
for height in heights:
    print(height)