arr = list(map(int, input("Enter list: ").split()))
x, y = map(int, input("Enter element and index: ").split())
arr = arr[:y] + [x] + arr[y:]
print("After insertion:", arr)