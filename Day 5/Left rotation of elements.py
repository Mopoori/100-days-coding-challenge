nums = list(map(int, input("Enter 10 numbers: ").split()))
n = int(input("Left rotations: ")) % len(nums)
nums = nums[n:] + nums[:n]
print("Left rotated:", nums)