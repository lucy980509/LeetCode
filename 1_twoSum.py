class Solution(object):
    def twoSum(nums, target):
        prevMap = {} # val : index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
    nums = [2, 11, 7, 15]
    target = 9
    print(twoSum(nums, target))

    
