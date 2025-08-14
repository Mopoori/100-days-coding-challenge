a =list(map(int, input("Enter first sorted array: ").split()))
b=list(map(int, input("Enter second sorted array: ").split()))
i = j = 0
c = []

while i < len(a) and j < len(b):
    c.append(a[i] if a[i] < b[j] else b[j])
    if a[i] < b[j]:
        i += 1
    else:
        j += 1

c += a[i:] + b[j:]
print(c)
