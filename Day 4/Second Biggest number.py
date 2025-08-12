n = list(map(int, input("Enter numbers with space: ").split()))
largest = second_largest = float("-inf")
for i in n:
    if i> largest:
        second_largest = largest
        largest = i
    elif i > second_largest and i != largest:
        second_largest = i
print("Second biggest number is:", second_largest)
