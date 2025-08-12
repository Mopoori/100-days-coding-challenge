arr = list(map(int, input("Enter list: ").split()))
i = int(input("Enter index to delete: "))
arr = arr[:i] + arr[i+1:]
print("After deletion:", arr)
