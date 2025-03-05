# Output: [2,3]
nums = [2,7,11,15]
target = 26
class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        hashmap = {}
        for i, k in enumerate(nums):
            complement = target - nums[i] 
            if complement in hashmap:           
                return [hashmap[complement], i]
            hashmap[k] = i     

solution = Solution()
print(solution.twoSum(nums, target))

