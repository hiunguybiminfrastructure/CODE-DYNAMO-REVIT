nums = [1,2,3,4, "a", "b", "c", "d", "e", "f"]
#       0 1 2 3   4    5    6    7    8    9
#                       -4     -3     -2     -1

#index
lastSign = nums[len(nums) - 1]

newSigns = nums[3:-1]

#loop

for i in nums:
    print(i)