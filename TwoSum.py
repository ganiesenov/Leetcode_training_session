
# Output: [0,1]
class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        for i in range(len(nums)):
            for j in range(len(nums)): 
                if i!=j and nums[i] + nums[j] == target: 
                    return[i,j]
        return []
    
    
    
    
    
    
    
nums = [2,7,11,15]
target = 26
solution = Solution()
print(solution.twoSum(nums, target))