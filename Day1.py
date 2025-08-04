# Linear search
def linearSearch(arr, targetVal):
  for i in range(len(arr)):
    if arr[i] == targetVal:
      return i
  return -1

mylist = [3, 7, 2, 9, 5, 1, 8, 4, 6]
x = 4

result = linearSearch(mylist, x)

if result != -1:
  print("Found at index", result)
else:
  print("Not found")


# Binary search
# def binarySearch(arr, targetVal):
#   left = 0
#   right = len(arr) - 1
#
#   while left <= right:
#     mid = (left + right) // 2
#
#     if arr[mid] == targetVal:
#       return mid
#
#     if arr[mid] < targetVal:
#       left = mid + 1
#     else:
#       right = mid - 1
#
#   return -1
#
# mylist = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
# x = 11
#
# result = binarySearch(mylist, x)
#
# if result != -1:
#   print("Found at index", result)
# else:
#   print("Not found")
