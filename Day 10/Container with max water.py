container = [3, 2, 1, 1, 4, 2]
left = 0
right = len(container) - 1
max_area = 0

while left < right:
    base = right - left
    min_height = min(container[left], container[right])
    area = base * min_height
    max_area = max(max_area, area)

    if container[left] < container[right]:
        left += 1
    else:
        right -= 1

print(max_area)