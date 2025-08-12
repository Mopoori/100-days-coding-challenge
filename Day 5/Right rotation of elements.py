nums = list(map(int, input("Enter 10 numbers: ").split()))
n = int(input("Right rotations: ")) % len(nums)
nums = nums[-n:] + nums[:-n]
print("Right rotated:", nums)