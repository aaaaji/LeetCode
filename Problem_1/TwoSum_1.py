class Solution:
    def twoSum(self, nums, target):
        D = {}
        for i,num in enumerate(nums):
            n = target - num
            if n not in D:
                D[num] = i
                print(i,num,D)
            else:
                return [D[n], i]
