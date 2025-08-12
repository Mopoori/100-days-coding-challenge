st = input("Enter a string: ")
checked = ""
print("Duplicate letters are:", end=" ")
for i in range(len(st)):
    count = 0
    if st[i] not in checked:
        for j in range(len(st)):
            if st[i] == st[j]:
                count += 1
        if count > 1:
            print(st[i], end=" ")
        checked += st[i]
print()