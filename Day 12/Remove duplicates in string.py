# Input string
s = "programming"

# Convert to list of characters
chars = list(s)

# Two-pointer technique to remove duplicates in-place
n = len(chars)
if n > 1:
    write = 0  # pointer for position to write next unique char
    for read in range(n):
        duplicate = False
        for j in range(write):  # check if chars[read] already exists in written part
            if chars[read] == chars[j]:
                duplicate = True
                break
        if not duplicate:
            chars[write] = chars[read]
            write += 1

# Truncate extra elements
chars = chars[:write]

# Convert back to string if needed
result = "".join(chars)
print("After removing duplicates:", result)
